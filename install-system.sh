#!/bin/sh
# 系统级安装：把中文消息字典放入 VMware 安装目录（需要 sudo/root）
# 安装后，直接运行原来的 VMware 图标即可加载中文（系统区域为 zh_CN 时）。
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
sudo mkdir -p /usr/lib/vmware/messages/zh_CN
sudo cp "$DIR/messages/zh_CN/vmware.vmsg" /usr/lib/vmware/messages/zh_CN/vmware.vmsg
echo "已安装到 /usr/lib/vmware/messages/zh_CN/vmware.vmsg"
echo "请完全退出并重新打开 VMware Workstation。"
