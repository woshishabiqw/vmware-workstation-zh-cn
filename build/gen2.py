# -*- coding: utf-8 -*-
import json,re,glob
# existing translations
ns={}; exec(open('/tmp/gen.py',encoding='utf-8').read(), ns); ZH=dict(ns['ZH'])
import glob as _g
for _fn in _g.glob('/tmp/keyphrase*.tsv'):
    for _line in open(_fn,encoding='utf-8'):
        _line=_line.rstrip('\n')
        if not _line or '||' not in _line: continue
        _k,_v=_line.split('||',1)
        _v=_v.replace('\\n','\n').replace('\\t','\t')
        ZH[_k]=_v

E=json.load(open('/tmp/vm_all2.json'))
PHRASE={}
for fn in sorted(glob.glob('/tmp/phrase*.tsv')):
  for line in open(fn,encoding='utf-8'):
    line=line.rstrip('\n')
    if not line or '||' not in line: continue
    en,zh=line.split('||',1)
    en=en.replace('\\n','\n').replace('\\t','\t'); zh=zh.replace('\\n','\n').replace('\\t','\t')
    PHRASE[en]=zh
EXTRA={
 "msg.ui.dlgFirstTime.title":"欢迎使用 VMware Workstation",
 "msg.vmui.linux.localCnxTab.header":"正在连接到 Workstation Server",
 "msg.vmui.linux.localCnxTab.tasks":"任务",
 "msg.tray.openWorkstation":"打开 Workstation",
 "msg.tray.exitWorkstation":"退出 Workstation",
}
def tokens(s): return re.findall(r'%(?:%|[-+ #0]*\d*(?:\.\d+)?[diouxXeEfgGaAcsp])', s)
# apply phrase globally by exact English value
notfound=set(PHRASE)-set(E.values())
for k,v in E.items():
    if v in PHRASE and k not in ZH:
        ZH[k]=PHRASE[v]
for k,v in EXTRA.items():
    if k in E: ZH[k]=v
# also translate any keys in target groups whose value still untranslated but in PHRASE (covered)
# validate
errs=[]
for k,v in ZH.items():
    if k not in E: errs.append(("MISSING_KEY",k)); continue
    if tokens(E[k])!=tokens(v): errs.append(("TOKEN",k,E[k],v,tokens(E[k]),tokens(v)))
    if '"' in v: errs.append(("DQUOTE",k,v))
lines=['.encoding = "UTF-8"']
for k,v in ZH.items():
    val=v.replace('\\','\\\\').replace('\n',' ').replace('\t',' ')
    lines.append('%s = "%s"'%(k,val))
open('/tmp/vmware_zh.vmsg','w',encoding='utf-8').write('\n'.join(lines)+'\n')
print("ZH entries:",len(ZH))
print("phrase entries:",len(PHRASE),"not found in catalog:",len(notfound))
for x in sorted(notfound): print("  NOTFOUND:",repr(x))
if errs:
    print("ERRORS:",len(errs))
    for e in errs[:30]: print(e)
else:
    print("no errors")
