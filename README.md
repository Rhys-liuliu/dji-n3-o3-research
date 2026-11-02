# DJI Goggles N3 ↔ O3 compatibility research

**Research only. No working compatibility firmware, no flashable release, and no demonstrated N3–O3 RF connection.**

## 我想实现什么

我希望 DJI Goggles N3 可以直接无线连接 O3 图传，软件功能尽量与 Goggles 3 连接 O3 时相同。显示效果和性能按 N3 的硬件适配，同时保留 O4 支持。USB 视频输出或通过电脑转播不能代替这个目标。

我现在有 N3，可以借来 O3 做验证。不能拆机。可以接受修改固件，但必须先证明 USB 恢复方案可靠；目前没有证明，因此现阶段只做分析。

## 当前进展

- 已搭建本地 REA + Ghidra 分析环境，并分析 DJI Assistant 2 的部分下载逻辑。
- 找到一个疑似 N3 原厂固件模块：IM*H、ZV30、2805，295,949,920 字节。已核对其载荷 SHA-256 与头部记录一致。
- **尚未验证数字签名，尚未得到解密后的代码，也未确认它是完整的 N3 更新包。** 哈希一致不能证明来源真实性。
- 未取得 Goggles 3 参考固件；未进行 N3–O3 对频、视频或 O4 回归测试。
- 未通过本研究向眼镜写入修改固件。USB 恢复能力未验证。

## 最需要的帮助

1. 如何正确验证和解析这个 ZV30 / 2805 模块？是否有公开的格式说明或适用工具版本？
2. 如何合法获取 N3 与 Goggles 3 的完整模块清单和原厂固件，以便比较 O3 支持代码？
3. 有没有 N3 与 Goggles 3 射频芯片、基带和视频解码能力的可靠对比？需要先判断障碍是否可能通过软件解决。
4. 有没有可复现、无需拆机的 N3 USB 恢复资料？正常升级成功不能证明修改固件启动失败后仍可恢复。

请在 Issues 中提供来源、适用机型和版本、实际操作结果与限制。没有可行路径的证据也有帮助，不预设一定能移植。

## English

I want Goggles N3 to link **directly over RF** to an O3 Air Unit, with the software functions available on Goggles 3 + O3, adapted to N3 hardware, while preserving O4 support. USB video output is not a substitute.

I own N3 and can borrow O3 for testing. No disassembly is available. Modified firmware must not be flashed until recovery over USB has been demonstrated; this has not been established.

The immediate blocker is validating and understanding a candidate ZV30 / 2805 IMaH module. There is no decrypted N3 code, G3 reference image, working patch, or demonstrated compatibility yet. Help with format/tool support, legitimate firmware provenance, hardware comparisons, and recovery evidence is welcome.

## Research materials

- [Evidence and limitations](docs/RESEARCH.md)
- [Requirements and acceptance checks](docs/REQUIREMENTS.md)
- [Public metadata](evidence/n3-module.json)
- [Local verification tool](tools/inspect_imah.py) — reads a caller-supplied file; never writes firmware.
- [Help request](HELP_REQUEST.md)

Research was assisted by AI using [REA](https://github.com/morluto/rea). Interpretations are preliminary and need independent review. This is an independent project, not an official DJI or REA release. Original documentation and the inspection script are licensed under MIT; no license is granted for DJI firmware or third-party software.
