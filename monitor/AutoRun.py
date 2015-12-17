#!/usr/bin/env python
# coding=utf-8

import os;
from Utils import *;

def SetLSvrMcpCnt(mcp_cnt):
    ip = "10.175.70.10";
    cmd = "cd /usr/local/services/LSvr/bin/; sh ./both_mcp_cnt_set.sh %d" % mcp_cnt;
    ExeRemoteCmd(ip, cmd);

def GetStatFile():
    ip = "10.175.70.10";
    cmd = "cd /data/jackjluo/sh/; sh ./get_stat.sh";
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
        thread_num += min_thread;
        totalCnt += 1;
    mcp_cnt += min_cnt;
print "total count: %d" % totalCnt;
