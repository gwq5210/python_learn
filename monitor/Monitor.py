#!/usr/bin/env python
# coding=utf-8

from NetInfo import NetInfo;
from CpuInfo import CpuInfo, GetProcessCpuInfo;
import sys;
import time;
import getopt;

def PrintUsage():
    print "python %s [-o output_file] [-t run_seconds] [-i interval] [-p process_name] -h" % sys.argv[0];
    print "-o output_file. default not save.";
    print "-t run_seconds. default 60s.";
    print "-i interval. default 5s.";
    print "-p process_name. default no used.";

try:
    opts, args = getopt.getopt(sys.argv[1:], "o:t:i:p:h");
except getopt.GetoptError as err:
#   print help information and exit.
    print(err);
    PrintUsage();
    sys.exit(0);

output_file = "";
run_seconds = 60;
sleep_time = 5;
process_name = "";
for opt, arg in opts:
    if opt == "-o":
        output_file = arg;
    elif opt == "-t":
        run_seconds = int(arg);
    elif opt == "-i":
        sleep_time = int(arg);
    elif opt == "-p":
        process_name = arg;
    elif opt == "-h":
        PrintUsage();
        sys.exit();
    else:
        print "Unknow option " + opt;
        sys.exit();

seconds_left = run_seconds;
times = run_seconds / sleep_time;

#eth = "wlp3s0";
eth = "eth1";
dev_file = "dev";
cpu_file = "stat";

oldNetInfo = NetInfo(dev_file);
oldNetInfo.LoadNetInfo();
netInfo = NetInfo(dev_file);
netInfo.LoadNetInfo();

oldCpuInfo = CpuInfo(cpu_file);
oldCpuInfo.LoadCpuInfo();
cpuInfo = CpuInfo(cpu_file);
cpuInfo.LoadCpuInfo();

totalIn = 0.0;
totalOut = 0.0;
totalCpu = 0.0;
totalLSvrCpu = ProcessCpuInfo();
totalLrsyncCpu = ProcessCpuInfo();
while seconds_left > 0:
    print "time left %d." % seconds_left;
    seconds_left = seconds_left - sleep_time;
    time.sleep(sleep_time);
    
    netInfo = NetInfo(dev_file);
    netInfo.LoadNetInfo();
    diffNetInfo = netInfo - oldNetInfo;
    totalIn += diffNetInfo.GetInMbps(eth);
    totalOut += diffNetInfo.GetOutMbps(eth);
    oldNetInfo = netInfo;
    print "In %.2f Mbps." % diffNetInfo.GetInMbps(eth);
    print "Out %.2f Mbps." % diffNetInfo.GetOutMbps(eth);

    cpuInfo = CpuInfo(cpu_file);
    cpuInfo.LoadCpuInfo();
    diffCpuInfo = cpuInfo - oldCpuInfo;
    diffCpuInfo.CalcUsage();
    oldCpuInfo = cpuInfo;
    maxUsage, maxIdx = diffCpuInfo.GetMaxUsage();
    totalCpu += maxUsage;
    print "Cpu %d %.2f%%." % (maxIdx, maxUsage);
    if process_name != "":
        processCpuInfoStr = GetProcessCpuInfo(process_name, True);
        with open(output_file, "w+") as f:
            f.write(processCpuInfoStr);

avgIn = totalIn / times;
avgOut = totalOut / times;
avgCpu = totalCpu / times;
print "summary:"
print "avgIn: %.2f Mbps" % avgIn;
print "avgOut: %.2f Mbps" % avgOut;
print "avgCpu: %.2f%%" % avgCpu;

if output_file == "":
    sys.exit();

with open(output_file, "w") as f:
    f.write("avgIn %.2f\n" % avgIn)
    f.write("avgOut %.2f\n" % avgOut);
    f.write("avgCpu %.2f\n" % avgCpu);

if process_name != "":
    processCpuInfoStr = GetProcessCpuInfo(process_name, True);
    with open(output_file, "w+") as f:
        f.write(processCpuInfoStr);
