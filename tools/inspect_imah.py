"""Read-only IMaH v2 header/digest inspection. Does not authenticate or decrypt.

Layout reference: o-gs/dji-firmware-tools, ImgPkgHeader in dji_imah_fwsig.py.
Usage: python tools/inspect_imah.py FILE > metadata.json
       python tools/inspect_imah.py --self-test
"""
import hashlib
import io
import json
import struct
import sys
from pathlib import Path


def inspect(stream):
    stream.seek(0, 2)
    length = stream.tell()
    stream.seek(0)
    head = stream.read(192)
    if len(head) != 192 or head[:4] != b"IM*H":
        raise ValueError("Not a complete IMaH header")
    u32 = lambda offset: struct.unpack_from("<I", head, offset)[0]
    version, size = u32(4), u32(8)
    header_size, signature_size, payload_size = u32(16), u32(20), u32(24)
    if version != 2:
        raise ValueError("This inspector supports header version 2 only")
    if header_size != 192 + 32 * u32(156):
        raise ValueError("Header size does not match chunk count")
    payload_start = header_size + signature_size
    if size != length or payload_start + payload_size != length:
        raise ValueError("Declared image regions do not match file length")
    stream.seek(payload_start)
    payload_hash = hashlib.sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b""):
        payload_hash.update(block)
    stream.seek(0)
    file_hash = hashlib.sha256()
    for block in iter(lambda: stream.read(1024 * 1024), b""):
        file_hash.update(block)
    text = lambda start, end: head[start:end].split(b"\0", 1)[0].decode("ascii", "strict")
    return {
        "file_sha256": file_hash.hexdigest(), "byte_length": length,
        "magic": "IM*H", "header_version": version,
        "header_size": header_size, "signature_size": signature_size,
        "payload_size": payload_size, "chunk_count": u32(156),
        "module": text(64, 96), "type": text(96, 100),
        "auth_key_id": text(40, 44), "enc_key_id": text(44, 48),
        "module_version_hex": f"0x{u32(100):08x}",
        "date_field_hex": f"0x{u32(104):08x}",
        "payload_sha256": payload_hash.hexdigest(),
        "payload_digest_matches_header": payload_hash.digest() == head[160:192],
        "signature_validation": "not_performed", "decryption": "not_performed",
        "product_identity": "not_authenticated",
    }


def self_test():
    head = bytearray(192)
    head[:4] = b"IM*H"
    for offset, value in ((4, 2), (8, 195), (16, 192), (24, 3)):
        struct.pack_into("<I", head, offset, value)
    head[160:192] = hashlib.sha256(b"abc").digest()
    assert inspect(io.BytesIO(head + b"abc"))["payload_digest_matches_header"]
    assert not inspect(io.BytesIO(head + b"abd"))["payload_digest_matches_header"]
    for invalid in (b"IM*H", head + b"ab", head + b"abcd"):
        try:
            inspect(io.BytesIO(invalid))
        except ValueError:
            pass
        else:
            raise AssertionError("Malformed input accepted")
    print("self-test passed")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        self_test()
    elif len(sys.argv) == 2:
        with Path(sys.argv[1]).open("rb") as source:
            print(json.dumps(inspect(source), indent=2))
    else:
        raise SystemExit(__doc__)
