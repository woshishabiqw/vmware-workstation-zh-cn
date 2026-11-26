# -*- coding: utf-8 -*-
import json,re
E=json.load(open('/tmp/vm_all2.json'))
cur=set()
for line in open('/tmp/vmware_zh.vmsg',encoding='utf-8'):
    if ' = "' in line: cur.add(line.split(' = "',1)[0])
UI=lambda k:k.startswith(('msg.cui.','msg.ui.','msg.vmui.','msg.lui.','msg.player.','msg.netcfg.','msg.tray.','msg.vmsettings.','button.'))
word=re.compile(r'[A-Za-z]{2,}')
ospat=re.compile(r'^(Windows|MS-DOS|OS/2|eComStation|Ubuntu|Debian|CentOS|Red Hat|Fedora|SUSE|openSUSE|FreeBSD|Mac OS X|OS X|macOS|Solaris|Sun Solaris|Oracle|Rocky|AlmaLinux|Amazon Linux|Linux(?! Mint| kernel)|Pardus|ProLinux|Novell|SCO|VMware ESXi|VMware ESX|VMware Photon|VMware CRX|Hyper-V|Other)')
os_vals=set(v for k,v in E.items() if k.startswith('button.') and len(v)<=42 and ospat.match(v))
rem=set()
for k,v in E.items():
    if k in cur: continue
    if not UI(k): continue
    if not word.search(v): continue
    if v in os_vals: continue
    rem.add(v)
rem=sorted(rem)
open('/tmp/todo_unique.txt','w',encoding='utf-8').write('\n'.join(rem)+'\n')
print("os_vals excluded:",len(os_vals))
print("remaining translatable unique UI strings:",len(rem))
# breakdown by namespace of first key
from collections import Counter
c=Counter()
for v in rem: c[v[:1]]+=1
