# Help wanted: N3 ↔ O3 feasibility, ZV30 module analysis, and USB recovery

我想让 N3 直接无线连接 O3，软件功能参考 Goggles 3 + O3，并保留 O4 支持。目前只有研究材料，没有可用固件，希望有相关经验的开发者帮助判断是否可行。

I am researching direct Goggles N3 ↔ O3 Air Unit compatibility, using Goggles 3 + O3 as the software reference and retaining O4 support. I have N3 and can borrow O3. No disassembly is available. This is an early research request, not a working firmware announcement.

Current evidence:

- Candidate encrypted IMaH module: ZV30 / 2805, 295,949,920 bytes, PRAK / UFIE, 384-byte signature.
- Payload SHA-256 matches its header; signature authenticity is unverified and no plaintext has been obtained.
- Full N3 package manifest and G3 reference firmware are missing. RF hardware compatibility is unknown.
- No N3–O3 pairing or video test has succeeded or been attempted in this research. USB recovery after modified-firmware boot failure is unverified, so no modified firmware will be flashed.

Specific help needed:

1. Public documentation or tools supporting this IMaH variant and correct signature validation.
2. Legitimate, reproducible ways to identify/download complete N3 and G3 update module sets without starting a device update.
3. Source-backed hardware/stack comparisons that can establish or rule out a software path to O3 support.
4. Evidence for a non-disassembly USB recovery path, including its failure limits.

Please share sources, exact versions, reproducible observations, and uncertainty. Suggestions that rule out a path are welcome. Please do not post credentials, private signing keys, device identifiers, or proprietary firmware dumps.

Research notes were assisted by AI/REA and need independent review. This request does not claim a verified porting or recovery method.
