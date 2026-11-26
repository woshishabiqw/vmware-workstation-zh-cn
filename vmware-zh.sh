#!/bin/sh
# 以中文消息字典启动 VMware Workstation（无需 root）
DIR="$(cd "$(dirname "$0")" && pwd)"
export VMSGDIR="$DIR/messages"
export LD_PRELOAD="$DIR/redir.so${LD_PRELOAD:+:$LD_PRELOAD}"
exec /usr/bin/vmware "$@"
