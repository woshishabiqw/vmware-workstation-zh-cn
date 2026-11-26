#!/bin/bash
# 从 build/ 源文件重建语言包与 deb 包（构建时自动从本机 VMware 提取原文）
set -e
SB="$(cd "$(dirname "$0")" && pwd)"
python3 "$SB/extract.py"
cp "$SB"/phrase*.tsv "$SB"/keyphrase*.tsv "$SB"/gen.py "$SB"/gen2.py /tmp/
python3 /tmp/gen2.py
ROOT=/tmp/vmzh_pkgroot
rm -rf "$ROOT"; mkdir -p "$ROOT/DEBIAN" "$ROOT/usr/lib/vmware/messages/zh_CN"
cp /tmp/vmware_zh.vmsg "$ROOT/usr/lib/vmware/messages/zh_CN/vmware.vmsg"
cat > "$ROOT/DEBIAN/control" <<'CTL'
Package: vmware-workstation-zh-cn
Version: 1.0.2
Section: misc
Priority: optional
Architecture: all
Maintainer: daikali407 <daikali407@localhost>
Description: VMware Workstation Pro 26.0.1 (26H1) 简体中文语言包
 适用于 VMware Workstation Pro 26.0.1（26H1，build 25688693，Linux）。
 安装 /usr/lib/vmware/messages/zh_CN/vmware.vmsg 中文语言包。
Homepage: https://github.com/woshishabiqw/vmware-workstation-zh-cn
CTL
( cd "$ROOT" && find usr -type f -exec md5sum {} \; > DEBIAN/md5sums )
OUT="$SB/../dist"; mkdir -p "$OUT"
dpkg-deb --build --root-owner-group "$ROOT" "$OUT/vmware-workstation-zh-cn_1.0.2_all.deb"
echo "已生成: $OUT/vmware-workstation-zh-cn_1.0.2_all.deb"
