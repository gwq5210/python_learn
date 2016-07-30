#!/usr/bin/env python
# coding=utf-8

from NetInfo import NetInfo;
from CpuInfo import CpuInfo, ProcessCpuInfo;
from Common import CpuNetInfo;
import sys;
import time;
from datetime import datetime;
import getopt;
try:
    import cPickle as pickle;
except:
    import pickle;

def PrintUsage():
    print "python %s [-o output_file] [-t run_seconds] [-i interval] [-p process_name] -h -d" % sys.argv[0];
    print "-o output_file. default not save.";
    print "-t run_seconds. default 60s.";
    print "-i interval. default 5s.";
    print "-p process_name. default no used.";
    print "-h print help information"
    print "-d debug";

try:
    opts, args = getopt.getopt(sys.argv[1:], "o:t:i:p:hd");
except getopt.GetoptError as err:
#   print help information and exit.
    print(err);
    PrintUsage();
    sys.exit(0);

output_file = "";
run_seconds = 60;
sleep_time = 5;
process_names = [];
debug = False;
for opt, arg in opts:
    if opt == "-o":
        output_file = arg;
    elif opt == "-t":
        run_seconds = int(arg);
    elif opt == "-i":
        sleep_time = int(arg);
    elif opt == "-p":
        process_names.append(arg);
    elif opt == "-h":
        PrintUsage();
        sys.exit();
    elif opt == "-d":
        debug = True;
    else:
        print "Unknow option " + opt;
        sys.exit();

seconds_left = run_seconds;
times = run_seconds / sleep_time;

eth = "wlp3s0";
#eth = "eth1";
dev_file = "/proc/net/dev";
cpu_file = "/proc/stat";

oldNetInfo = NetInfo(dev_file);
oldNetInfo.LoadNetInfo();
netInfo = NetInfo(dev_file);
netInfo.LoadNetInfo();
beginTime = datetime.now();
sampleBeginTime = datetime.now();
sampleEndTime = datetime.now();

oldCpuInfo = CpuInfo(cpu_file);
oldCpuInfo.LoadCpuInfo();
cpuInfo = CpuInfo(cpu_file);
cpuInfo.LoadCpuInfo();

totalIn = 0.0;
totalOut = 0.0;
totalCpu = 0.0;
totalProcessCpu = {};
processCpu = {};
for process_name in process_names:
    processCpu[process_name] = ProcessCpuInfo(process_name);
    processCpu[process_name].GetProcessCpuInfo();
    totalProcessCpu[process_name] = ProcessCpuInfo(process_name);
    totalProcessCpu[process_name].GetProcessCpuInfo();
    totalProcessCpu[process_name].Clear();

cnt = times;
while cnt > 0:
    print "times %d." % cnt;
    time.sleep(sleep_time);
    
    netInfo = NetInfo(dev_file);
    netInfo.LoadNetInfo();
    diffNetInfo = netInfo - oldNetInfo;
    totalIn += diffNetInfo.GetInMbps(eth);
    totalOut += diffNetInfo.GetOutMbps(eth);
    sampleEndTime = datetime.now();
    sampleSeconds = (sampleEndTime - sampleBeginTime).seconds;
    sampleBeginTime = datetime.now();
    oldNetInfo = netInfo;

    cpuInfo = CpuInfo(cpu_file);
    cpuInfo.LoadCpuInfo();
    diffCpuInfo = cpuInfo - oldCpuInfo;
    diffCpuInfo.CalcUsage();
    oldCpuInfo = cpuInfo;
    maxUsage, maxIdx = diffCpuInfo.GetMaxUsage();
    totalCpu += maxUsage;

    if debug:
        print "Sample Seconds %d." % sampleSeconds;
        print "In %.2f Mbps." % diffNetInfo.GetInMbps(eth, sampleSeconds);
        print "Out %.2f Mbps." % diffNetInfo.GetOutMbps(eth, sampleSeconds);
        print "Cpu %d %.2f%%." % (maxIdx, maxUsage);
    for process_name in process_names:
        processCpu[process_name] = ProcessCpuInfo(process_name);
        processCpu[process_name].GetProcessCpuInfo();
        totalProcessCpu[process_name] = totalProcessCpu[process_name] + processCpu[process_name];
        if debug:
            print processCpu[process_name].infoStr;
    cnt = cnt - 1;

endTime = datetime.now();
allTime = (endTime - beginTime).seconds;
avgIn = totalIn / allTime;
avgOut = totalOut / allTime;
avgCpu = totalCpu / times;

for process_name in process_names:
    totalProcessCpu[process_name].CalcUsage(times);

allInfo = CpuNetInfo();
allInfo.avgIn = avgIn;
allInfo.avgOut = avgOut;
allInfo.avgCpu = avgCpu;
allInfo.processCpu = totalProcessCpu;
if output_file == "":
    print "summary:"
    print str(allInfo);
    sys.exit();

if debug:
    print "before:"
    print str(allInfo);

with open(output_file, "w") as f:
    pickle.dump(allInfo, f);

if debug:
    info  = None;
    with open(output_file) as f:
        info = pickle.load(f);
    print "after:"
    print str(info);
