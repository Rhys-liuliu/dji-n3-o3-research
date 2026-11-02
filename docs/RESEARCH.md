# Evidence and open questions

Prepared 2026-11-02 from local research performed on 2026-11-01. These are historical observations, not a claim about the latest vendor release.

## Candidate firmware module

Source: an existing DJI Assistant 2 firmware cache on the research computer. It was not obtained through a documented complete-package manifest. The source filename is a cache identifier, not proof of product/version identity.

The candidate was copied locally and hash checked. Its IMaH header identifies type ZV30, module 2805, auth key identifier PRAK, encryption identifier UFIE, and a 384-byte signature. The encrypted payload digest matches the digest in the header. This is internal consistency only: the header itself has not been authenticated.

The header date field decodes to 2026-10-19. An Assistant release-list cache also associated that date with product version V01.00.1300. This supports a candidate association, not a verified mapping of this module to that product release or a complete update package. The module version is not the product version.

Public `dji_imah_fwsig.py` v0.3.2 was examined (SHA-256 `534680d1fb0ced5f6425b276fcd421456a45a513cf625d73566b2150c2ed6760`). Of eight available PRAK labels, only one public key had a modulus length compatible with this 384-byte signature. No successful signature verification was obtained. Do not describe this as eight equivalent RSA-3072 verification tests.

A bounded first-4096-byte trial with six historical UFIE keys did not produce selected common file signatures. This is an inconclusive heuristic, not proof that every key is incorrect or that decryption is impossible. No forced extraction result is treated as valid plaintext.

## Assistant static analysis

Target: DJI Assistant 2 (Consumer Drones Series) 2.1.42, `DJIGlsService.dll`, 6,875,136 bytes, SHA-256 `2dff0ad378e623d9ec5c8f1b6508b3750a0cd40628a9db571301b3904f80a808`. REA/Ghidra decompilation produced these preliminary interpretations; addresses are provider-reported virtual addresses for this binary, not portable offsets:

| Entry address | Interpretation |
| --- | --- |
| `0x10153090` | GetFirmwareFile: checks cached file size and a digest against metadata, otherwise enters a request path |
| `0x1013f630` | Builds `/getfile/firmware` requests with product/module/version and authentication fields |
| `0x101405e0`, `0x10141320` | Build `/getfile/getallfile` requests; a logged “download URL” does not by itself identify a direct file URL |
| `0x101529e0` | GetFirmwareData: resolves selected package and invokes module processing |
| `0x10154330` | GetSingleFirmData: iterates modules and uses cache/download callbacks |

These findings do not establish a safe standalone download-only invocation. The complete callback path has not been resolved. No authenticated API request, injection, firmware transfer, or device mutation was executed through these functions. Raw decompilation remains local; this repository publishes a derived summary rather than redistributing proprietary code.

Assistant UI historically showed current N3 firmware V01.00.1300. USB enumeration showed DJI VID 2CA3 / PID 0020, including network, storage, and libusb interfaces. ADB listed no device. Enumeration alone does not provide access to firmware partitions or prove recovery capability.

## Other explored paths

- REA native-Windows firmware extraction requires additional Linux-host tools for its supported firmware workflow; no Linux distribution was installed. Resolving this environment gap would not resolve encryption or signature validation.
- Assistant's packaged ASAR could not be parsed reliably with the attempted tools. No valid JavaScript application extraction was obtained.
- A signed upstream DankDroneDownloader release was inspected as a .NET single-file bundle. Static code references authenticated catalog/download requests. It did not yield firmware files. A process-local runtime compatibility launch produced no usable window and was closed; the cause was not established. No paid access or authentication bypass was attempted.

## What has not been established

No hardware equivalence, O3-capable N3 RF stack, feasible port, signature acceptance of modified images, bootloader unlock, USB recovery after a failed modified boot, or safe flashing procedure has been established. Do not flash Goggles 3 images to N3 on the basis of this repository.

## References

- [DJI firmware tools](https://github.com/o-gs/dji-firmware-tools): IMaH parser and tool documentation.
- [Earlier RSA-3072 signature-size discussion, issue 292](https://github.com/o-gs/dji-firmware-tools/issues/292): a different product, included as related format history, not evidence of N3 support.
- [REA](https://github.com/morluto/rea): local analysis tool used in this investigation.
- [DankDroneDownloader](https://github.com/cs2000/DankDroneDownloader): explored downloader; no firmware acquired through it.

Only selected public metadata and derived research notes are published. Firmware images, application binaries, extracted assemblies, raw logs, credentials, device serial numbers, and machine-specific configuration are not included.
