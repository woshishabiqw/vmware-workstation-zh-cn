# VMware Workstation Pro（Linux）简体中文语言包

> 非官方、社区维护的界面汉化。与 VMware / Broadcom 无任何关联。

VMware Workstation Pro 内置多语言消息字典：当系统区域为 `zh_CN` 时，程序会加载
`/usr/lib/vmware/messages/zh_CN/vmware.vmsg`。本项目提供该中文语言包，覆盖菜单、
对话框、向导、设置、快照、许可、网络编辑器、VIX 错误等界面文案（约 4430 条）。

## 适用版本
本语言包针对 **VMware Workstation Pro 26H1u1（内部版本 26.0.1，build 25688693，Linux 版）** 制作与验证。
- 语言包按该版本的界面字符串生成；**其他 VMware 版本**可能缺少或多出条目，需用 `build/build.sh` 在本机重新提取并补充翻译后再用。
- 升级/修复 VMware 后，建议重新安装与对应版本匹配的汉化包。

## 安装
从 [Releases](../../releases) 下载 `vmware-workstation-zh-cn_1.0.3_all.deb` 后：
```bash
sudo apt install ./vmware-workstation-zh-cn_1.0.3_all.deb
# 或
sudo dpkg -i vmware-workstation-zh-cn_1.0.3_all.deb
```
安装后**完全退出并重新打开 VMware** 生效（系统区域需为 `zh_CN`）。

卸载：
```bash
sudo apt remove vmware-workstation-zh-cn
```

## 从源码构建
依赖：`python3`、`dpkg-dev`，以及本机已安装的 VMware Workstation。
```bash
cd build
./build.sh
# 生成 dist/vmware-workstation-zh-cn_1.0.3_all.deb
```
`build/extract.py` 会在**你本机**从已安装的 VMware 二进制中提取界面原文字符串，
再与 `phrase*.tsv` / `keyphrase*.tsv` 词表合并生成语言包；仓库本身不包含官方原文数据。

## 目录
- `messages/zh_CN/vmware.vmsg` —— 生成好的中文语言包
- `build/` —— 词表、生成与打包脚本（`extract.py` 构建时本机提取原文）
- `install-system.sh` —— 不打包、直接安装到系统目录（需 sudo）
- `vmware-zh.sh` + `redir.c` —— 免 root 备用启动器（可选）

## 免责声明
- 本项目为个人学习/自用目的的界面本地化，**非 VMware/Broadcom 官方产品**，不受其支持。
- 语言包内容为对 VMware 界面字符串的翻译，可能涉及 VMware/Broadcom 的版权或服务条款；
  请在遵守当地法律及软件许可的前提下**自行承担使用风险**。若版权方要求，请立即停止使用并删除。
- 升级/修复/重装 VMware 可能清除该文件，重新安装本包即可。
- VMware、Broadcom、Windows 等产品名称/版本号按惯例保留原文。

## 许可
仓库内脚本与构建工具以 MIT 许可发布（见 `LICENSE`）；翻译文本仅用于互操作性/个人使用。
