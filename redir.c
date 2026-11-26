#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdarg.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdio.h>
static const char* PFX="/usr/lib/vmware/messages/";
static const char* remap(const char* p, char* buf, size_t n){
  const char* base=getenv("VMSGDIR");
  if(base && p && strncmp(p,PFX,strlen(PFX))==0){
    snprintf(buf,n,"%s/%s",base,p+strlen(PFX));
    return buf;
  }
  return p;
}
#define ARGS(flags) mode_t m=0; if((flags)&O_CREAT){va_list a;va_start(a,flags);m=va_arg(a,int);va_end(a);}
int openat(int dirfd,const char* path,int flags,...){static int(*r)(int,const char*,int,...);if(!r)r=dlsym(RTLD_NEXT,"openat");ARGS(flags);char b[4096];return r(dirfd,remap(path,b,sizeof b),flags,m);}
int openat64(int dirfd,const char* path,int flags,...){static int(*r)(int,const char*,int,...);if(!r)r=dlsym(RTLD_NEXT,"openat64");ARGS(flags);char b[4096];return r(dirfd,remap(path,b,sizeof b),flags,m);}
int open(const char* path,int flags,...){static int(*r)(const char*,int,...);if(!r)r=dlsym(RTLD_NEXT,"open");ARGS(flags);char b[4096];return r(remap(path,b,sizeof b),flags,m);}
int open64(const char* path,int flags,...){static int(*r)(const char*,int,...);if(!r)r=dlsym(RTLD_NEXT,"open64");ARGS(flags);char b[4096];return r(remap(path,b,sizeof b),flags,m);}
int __open_2(const char* path,int flags){static int(*r)(const char*,int);if(!r)r=dlsym(RTLD_NEXT,"__open_2");char b[4096];return r(remap(path,b,sizeof b),flags);}
int __open64_2(const char* path,int flags){static int(*r)(const char*,int);if(!r)r=dlsym(RTLD_NEXT,"__open64_2");char b[4096];return r(remap(path,b,sizeof b),flags);}
#include <stdio.h>
FILE* fopen(const char* path,const char* mode){static FILE*(*r)(const char*,const char*);if(!r)r=dlsym(RTLD_NEXT,"fopen");char b[4096];return r(remap(path,b,sizeof b),mode);}
FILE* fopen64(const char* path,const char* mode){static FILE*(*r)(const char*,const char*);if(!r)r=dlsym(RTLD_NEXT,"fopen64");char b[4096];return r(remap(path,b,sizeof b),mode);}
