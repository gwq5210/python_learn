#!/usr/bin/env python
# coding=utf-8

import os;
import time;
import getopt;
import sys;
from Utils import *;
from Common import *;
from XlsMod import XlsMod;

def PrintUsage():
    print "python %s [-c mcp_cnt] [-t run_seconds] [-s thread_num] [-r req_type] [ -f file_name ] -l -n -h -d" % sys.argv[0];
    print "-c mcp_cnt. required.";
    print "-t run_seconds. default 120s.";
    print "-s thread_num. default 1.";
    print "-r req_type. default 1.";
    print "-h print help information.";
    print "-n north presscall, default False.";
    print "-f save xls with file_name, default test.xls.";
    print "-l load data from local dir.";
    print "-d debug";
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
    print "gather monitor info:";
    SaveWithIp(lsvr_ips);
    SaveWithIp(d_access_ips, pwd = red_password);
    SaveWithIp(sr_access_ips, pwd = red_password);
    SaveWithIp(d_cache_ips, pwd = red_password);
    SaveWithIp(sr_cache_ips, pwd = red_password);

    # presscall info
    print "gather presscall info:";
    SaveWithIp(presscall_ips_red, name = presscall_file, remote_name = presscall_file,
            pwd = red_password, remote_dir = presscall_remote_dir);
    SaveWithIp(presscall_ips, name = presscall_file, remote_name = presscall_file,
            remote_dir = presscall_remote_dir);

def GetLSvrCpuStr(lsvrCpuInfo, lsvrMcpCnt):
    baseName = "LSvr_mcp";
    retStr = "";
    for idx in range(lsvrMcpCnt):
        name = "%s_%d" % (baseName, idx);
        retStr += "%s %.2f\n" % (name, lsvrCpuInfo[baseName].info[name]);
    return retStr.strip()

def GetLSvrMaxCpu(lsvrCpuInfo, lsvrMcpCnt):
    baseName = "LSvr_mcp";
    maxCpu = 0.0;
    for idx in range(lsvrMcpCnt):
        name = "%s_%d" % (baseName, idx);
        maxCpu = max(maxCpu, lsvrCpuInfo[baseName].info[name]);
    return maxCpu;

def GetLRsyncCpuStr(lrsyncCpuInfo, lrsyncMcpCnt):
    baseName = "lrsync_mcp";
    retStr = "";
    for idx in range(lrsyncMcpCnt):
        name = "%s_%d" % (baseName, idx);
        retStr += "%s %.2f\n" % (name, lrsyncCpuInfo[baseName].info[name]);
    return retStr.strip()

def LoadAllMonitorInfo(lsvrMcpCnt):
    ret = {};
    lsvr_info = LoadMonitorInfo(lsvr_ips);
    ret["LSVR_IN"] = lsvr_info[lsvr_ips[0]].avgIn;
    ret["LSVR_OUT"] = lsvr_info[lsvr_ips[0]].avgOut;
    ret["LSVR_CPU"] = GetLSvrCpuStr(lsvr_info[lsvr_ips[0]].processCpu, lsvrMcpCnt);
    ret["LRSYNC_CPU"] = GetLRsyncCpuStr(lsvr_info[lsvr_ips[0]].processCpu, lsvrMcpCnt / 4);
    ret["LSVR_MAX_CPU"] = GetLSvrMaxCpu(lsvr_info[lsvr_ips[0]].processCpu, lsvrMcpCnt);

    infoMap = LoadMonitorInfo(d_access_ips);
    dAccessInfo = AvgCpuNetInfo(infoMap);
    ret["D_ACCESS_CPU"] = dAccessInfo.avgCpu;
    ret["D_ACCESS_IN"] = dAccessInfo.avgIn;
    ret["D_ACCESS_OUT"] = dAccessInfo.avgOut;

    infoMap = LoadMonitorInfo(sr_access_ips);
    srAccessInfo = AvgCpuNetInfo(infoMap);
    ret["SR_ACCESS_CPU"] = srAccessInfo.avgCpu;
    ret["SR_ACCESS_IN"] = srAccessInfo.avgIn;
    ret["SR_ACCESS_OUT"] = srAccessInfo.avgOut;

    infoMap = LoadMonitorInfo(d_cache_ips);
    dCaCheInfo = AvgCpuNetInfo(infoMap);
    ret["D_CACHE_CPU"] = dCaCheInfo.avgCpu;
    ret["D_CACHE_IN"] = dCaCheInfo.avgIn;
    ret["D_CACHE_OUT"] = dCaCheInfo.avgOut;

    infoMap = LoadMonitorInfo(sr_cache_ips);
    srCacheInfo = AvgCpuNetInfo(infoMap);
    ret["SR_CACHE_CPU"] = srCacheInfo.avgCpu;
    ret["SR_CACHE_IN"] = srCacheInfo.avgIn;
    ret["SR_CACHE_OUT"] = srCacheInfo.avgOut;
    return ret;

def LoadAllPresscallInfo():
    infoMap = LoadPresscallInfo(presscall_ips_red);
    infoMap = dict(infoMap, **LoadPresscallInfo(presscall_ips));
    return AvgPresscallInfo(infoMap);

def WriteXls(info, fileName, apiStr):
    writer = XlsMod(fileName);
    for key in info:
        if key != "LSVR_MAX_CPU":
            writer.SetCell(apiRowMap[apiStr], dataColMap[key], info[key], 1);
    for key in dataHeaderColMap:
        writer.SetCell(apiHeaderRowMap[apiStr], dataHeaderColMap[key], info[key], 1);
    writer.Save(fileName);

def InfoToStr(info):
    retStr = "";
    for key in info:
        retStr += "%s: %s\n" % (key, info[key]);
    return retStr.strip();


try:
    opts, args = getopt.getopt(sys.argv[1:], "c:t:s:r:knhf:ld");
except getopt.GetoptError as err:
#   print help information and exit.
    print(err);
    PrintUsage();
    sys.exit(0);

mcp_cnt = 0;
run_seconds = 120;
thread_num = 1;
req_type = 1;
apiStr = apiStrMap[1];
fileName = "test.xls";
is_south = True;
is_load = False;
debug = False;
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
    elif opt == "-f":
        fileName = arg;
    elif opt == "-l":
        is_load = True;
    elif opt == "-d":
        debug = True;
    else:
        print "Unknow option " + opt;
        sys.exit();

if mcp_cnt == 0:
    print "-c option mcp_cnt is required.";
    PrintUsage();
    sys.exit();

if not is_load:
    print "kill presscall...";
    KillPresscall();

    print "start presscall...";
    StartPresscall(mcp_cnt, req_type, thread_num, run_seconds, is_south);

    sleep_time = run_seconds / 4;
    print "sleep %d seconds..." % sleep_time;
    #time.sleep(sleep_time);

    print "start monitor. will run %d seconds." % (sleep_time * 2);
    StartMonitor(sleep_time * 2);
    #time.sleep(sleep_time * 2);

    sleep_time = sleep_time + 30;
    print "wait for presscall stop. sleep %d seconds..." % sleep_time;
    #time.sleep(sleep_time);

    GatherInfo();

print "load monitor info:";
info = LoadAllMonitorInfo(mcp_cnt);
print "load presscall info:";
info = dict(info, **LoadAllPresscallInfo());
print InfoToStr(info);

if debug:
    confirm = raw_input("is save with %s(yes/no): " % fileName);
    if confirm != "yes":
        print "no save and exit";
        sys.exit();

print "write xls %s." % fileName;
WriteXls(info, fileName, apiStr);

downFileCmd = "sz -be %s" % fileName;
print downFileCmd;
os.system(downFileCmd);
