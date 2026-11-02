# Question: validating a candidate Goggles N3 ZV30 / 2805 IMaH v2 module (384-byte signature)

I am trying to identify and validate a candidate Goggles N3 firmware module from an existing DJI Assistant 2 cache. I would appreciate guidance on format/tool support before interpreting any decrypted output. This is not a confirmed complete N3 update package or a demonstrated bug in the tool.

Observed metadata:

```text
size:          295949920 bytes
SHA-256:       8ab8884075939fec7339dc48e439789e416ff3862d9acd43726190834b7a872c
magic:         IM*H
header_version: 2
header_size:   224
signature_size: 384
payload_size:  295949312
chunk_count:   1
name / type:   2805 / ZV30
auth / enc:    PRAK / UFIE
version field: 0x0a00430f
date field:    0x20261019
payload SHA:   68834b017b2f012a43acdeaaa370f15a8e470090eb2bc86b307215be083d77c1
```

The payload SHA-256 matches the value stored in the header. I understand this only checks internal consistency and does not authenticate the header or establish N3/product-version identity.

Local environment: Windows, Python, isolated PyCryptodome dependency. The script identifies as `dji_imah_fwsig.py` v0.3.2; its SHA-256 is `534680d1fb0ced5f6425b276fcd421456a45a513cf625d73566b2150c2ed6760` (retrieved from master during the investigation, not a pinned upstream commit).

What I tried:

- `python dji_imah_fwsig.py -u -i <local-candidate-file>` stopped with image-header signature verification failure; no forced extraction was used.
- Among the eight local PRAK labels, only PRAK-2021-09 had a modulus length compatible with a 384-byte signature. No signature verification succeeded. I am not counting incompatible key sizes as equivalent RSA-3072 tests.
- A separate bounded first-4096-byte experiment with six historical UFIE keys did not yield selected common file prefixes. This was inconclusive; it did not establish valid plaintext or rule out every key/format variant.

I read issue #292 and its discussion about a different product's 384-byte signatures. The suggested forced extraction there does not establish authenticity or N3 applicability, so I have not treated it as a validated solution.

Questions:

1. Is ZV30 / 2805 known to use a supported IMaH variant, or are there header/signature details I should check first?
2. Is there a public verifier/key-generation identifier or reference sample that would help distinguish missing key coverage from a parsing or sample-integrity issue? I am not asking for private signing keys.
3. What non-sensitive metadata or reproducible read-only checks would be most useful to supply next?

My broader goal is to assess whether N3 could support direct O3 linking, but this question is limited to module identification/validation. No working N3–O3 firmware, plaintext N3 code, or safe recovery method has been established, and no modified firmware has been flashed in this research.

Notes were assisted by AI/REA and are preliminary. Firmware files, credentials, account details, and device identifiers are not attached.
