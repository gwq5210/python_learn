#!/usr/bin/env python
# coding=utf-8

import os;
import sys;
import time;
from Utils import *;

stdout = "/dev/null"
stdin = "/dev/null"
stderr = None
pidfile = "./.daemon.pid"
if pidfile:
    print("pid file alread exist!")
sys.stdout.flush()
sys.stdin.flush()
try:
    pid = os.fork()
    if pid > 0:
        sys.exit() #父进程退出只剩下子进程
except OSError,e:
    sys.stderr.write("fork #1 failed:(%d)%s\n" % (e.errno,e.strerror))
    sys.exit()
#调用‘chdir("/")’确认我们的进程不保持任何目录于使用状态。不做这个会导致系统管理员不能卸装(umount)一个文件系统，因为它是我们的当前工作目录。 [类似的，我们可以改变当前目录至对于守护程序运行重要的文件所在目录]
#改变当前进程运行目录 
os.chdir("/")
#使当前线程 拥有文件读写权限
os.umask(0)
#使子线程 脱离父线程的进程组，会话组，是子进程成为新的的头领， 进程同时与会话脱离 ，
os.setsid()
try:
    pid = os.fork() #父进程的会话头领可以退出，以为着非会话头领进程永远不可能获得终端
    if pid > 0 :
        sys.exit()
except OSError,e:
    sys.stderr.write("fork #2 failed:(%d)%s\n"  % (e.errno,e.strerror))
#调用close关闭从父进程继承过来的标准输入输出
if not stderr:
    stderr = stdout
    si = file(stdin,'r')
    so = file(stdout,'a+')
    se = file(stderr,'a+',0)#ubuffered
    pid = str(os.getpid())
    print("daemon process id:%s" % pid)
    sys.stderr.write("\n%s\n" % pid)
    sys.stderr.flush()
    if pidfile:
        abspath = os.path.abspath(pidfile)
        print(abspath)
        print("write to pid file :true")
        open(pidfile,"a").write("%s\n" % pid)
   #改变文件符号
    #os.dup2(si.fileno(), sys.stdin.fileno())
    #os.dup2(so.fileno(),sys.stdout.fileno())  
    #os.dup2(se.fileno(),sys.stderr.fileno())  


def SetLSvrMcpCnt(mcp_cnt):
    ip = "10.175.70.10";
    cmd = "cd /usr/local/services/LSvr/bin/; sh ./both_mcp_cnt_set.sh %d" % mcp_cnt;
    ExeRemoteCmd(ip, cmd);

def GetStatFile():
    ip = "10.175.70.10";
    cmd = "cd /data/jackjluo/sh/; sh ./get_stat.sh";
    ExeRemoteCmd(ip, cmd);

def SetDetailItemNum(num):
    ip = "10.175.70.10";
    cmd = "cd /usr/local/services/LSvr/bin/; sh ./lsvr_modify_attr.sh 20 DetailItemNum %d" % num;
    ExeRemoteCmd(ip, cmd);

min_cnt = 4;
max_cnt = 24;
mcp_cnt = min_cnt;
min_thread = 10;
max_thread = 200;
thread_num = min_thread;
baseName = "test.xls";
fileName = "";
reqSet = set([1, 3, 4, 5, 9, 10, 11, 12]);
totalCnt = 0;
SetDetailItemNum(111);
while mcp_cnt <= 24:
    SetLSvrMcpCnt(mcp_cnt);

    thread_num = min_thread;
    while thread_num <= max_thread:
        fileName = "test_%d_%d.xls" % (mcp_cnt, thread_num);
        if not os.path.isfile(fileName):
            os.system("cp test.xls %s" % fileName);
        for req_type in reqSet:
            cmd = "python Run.py -c %d -s %d -r %d -f %s" % (mcp_cnt, thread_num, req_type, fileName);
            print cmd;
            #os.system(cmd);
            GetStatFile();
            totalCnt += 1;
        thread_num += min_thread;
    mcp_cnt += min_cnt;
print "total count: %d" % totalCnt;

mcp_cnt = min_cnt;
thread_num = min_thread;
req_type = 1;
SetDetailItemNum(10);
while mcp_cnt <= 24:
    SetLSvrMcpCnt(mcp_cnt);

    thread_num = min_thread;
    while thread_num <= max_thread:
        fileName = "test_%d_%d.xls" % (mcp_cnt, thread_num);
        if not os.path.isfile(fileName):
            os.system("cp test.xls %s" % fileName);
        cmd = "python Run.py -c %d -s %d -r %d -f %s" % (mcp_cnt, thread_num, req_type, fileName);
        print cmd;
        #os.system(cmd);
        GetStatFile();
        thread_num += min_thread;
        totalCnt += 1;
    mcp_cnt += min_cnt;
print "total count: %d" % totalCnt;
