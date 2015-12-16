#!/usr/bin/env python
# coding=utf-8

import os;
import time;
import getopt;
import sys;
from Utils import *;
from Common import *;

def PrintUsage():
    print "python %s [-c mcp_cnt] [-t run_seconds] [-s thread_num] [-r req_type] -n -h" % sys.argv[0];
    print "-c mcp_cnt. required.";
    print "-t run_seconds. default 120s.";
    print "-s thread_num. default 1.";
    print "-r req_type. default 1.";
    print "-h print help information."
    print "-n north presscall, default False.";
    print "req_type is:";
    print "1-send";
    print "2-rushcheck+opencheck+getdetailist+open";
    print "3-rushcheck";
    print "4-opencheck";
    print "5-open";
    print "6-update answer";
    print "7-get answer";
    print "8-change status";
    print "9-get detail header";
    print "10-get detail list";
    print "11-get send list";
    print "12-get receive list";
    print "13-delete send record";
    print "14-delete receive record";

def GatherInfo():
    # monitor info
    print "gather monitor info:"
    SaveWithIp(lsvr_ips);
    SaveWithIp(d_access_ips, pwd = red_password);
    SaveWithIp(sr_access_ips, pwd = red_password);
    SaveWithIp(d_cache_ips, pwd = red_password);
    SaveWithIp(sr_cache_ips, pwd = red_password);

    # presscall info
    print "gather presscall info:"
    SaveWithIp(presscall_ips_red, name = presscall_file, remote_name = presscall_file,
            pwd = red_password, local_dir = presscall_local_dir, remote_dir = presscall_remote_dir);
    SaveWithIp(presscall_ips, name = presscall_file, remote_name = presscall_file,
            local_dir = presscall_local_dir, remote_dir = presscall_remote_dir);

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:t:s:r:knh");
except getopt.GetoptError as err:
#   print help information and exit.
    print(err);
    PrintUsage();
    sys.exit(0);

mcp_cnt = 0;
run_seconds = 120;
thread_num = 1;
req_type = 1;
is_south = True;
for opt, arg in opts:
    if opt == "-c":
        mcp_cnt = int(arg);
    elif opt == "-t":
        run_seconds = int(arg);
    elif opt == "-s":
        thread_num = int(arg);
    elif opt == "-r":
        req_type = int(arg);
    elif opt == "-h":
        PrintUsage();
        sys.exit();
    elif opt == "-n":
        is_south = False;
    else:
        print "Unknow option " + opt;
        sys.exit();

if mcp_cnt == 0:
    print "-c option mcp_cnt is required.";
    PrintUsage();
    sys.exit();

print "start presscall...";
StartPresscall(mcp_cnt, req_type, thread_num, run_seconds, is_south);

#time.sleep(30);
StartMonitor();

GatherInfo();

LoadMonitorInfo();
LoadPresscallInfo();

WriteXls();
