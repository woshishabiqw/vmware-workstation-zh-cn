#!/usr/bin/env python3
"""从本机已安装的 VMware Workstation 二进制中提取界面消息标记，生成 /tmp/vm_all2.json。
仅在本机运行时读取本地文件，不随仓库分发任何官方原文。"""
import glob, json
marker = b"@&!*@*@("
files = [
    "/usr/lib/vmware/lib/libvmwareui.so/libvmwareui.so",
    "/usr/lib/vmware/lib/libvmware.so/libvmware.so",
    "/usr/lib/vmware/lib/libvmwarebase.so/libvmwarebase.so",
]
files += sorted(glob.glob("/usr/lib/vmware/lib/*/*.so"))
files += sorted(glob.glob("/usr/lib/vmware/bin/*"))
E = {}
for f in sorted(set(files)):
    try:
        d = open(f, "rb").read()
    except Exception:
        continue
    i = 0
    while True:
        j = d.find(marker, i)
        if j < 0:
            break
        k = d.find(b"\x00", j)
        if k < 0:
            k = len(d)
        b = d[j:k][len(marker):]
        i = k
        p = b.find(b")")
        if p < 0:
            continue
        E.setdefault(b[:p].decode("utf-8", "replace"), b[p+1:].decode("utf-8", "replace"))
json.dump(E, open("/tmp/vm_all2.json", "w"), ensure_ascii=False)
print("extracted", len(E), "messages -> /tmp/vm_all2.json")
