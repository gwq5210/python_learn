#!/usr/bin/env python
# coding=utf-8

from NetInfo import NetInfo;
from CpuInfo import CpuInfo, GetProcessCpuInfo;
import sys;
import time;

run_seconds = 10;
sleep_time = 5;
seconds_left = run_seconds;
times = run_seconds / sleep_time;

oldNetInfo = NetInfo("dev");
oldNetInfo.LoadNetInfo();
netInfo = NetInfo("dev");
netInfo.LoadNetInfo();

oldCpuInfo = CpuInfo("stat");
oldCpuInfo.LoadCpuInfo();
cpuInfo = CpuInfo("stat");
cpuInfo.LoadCpuInfo();

totalIn = 0.0;
totalOut = 0.0;
while seconds_left > 0:
    seconds_left = seconds_left - sleep_time;
    time.sleep(sleep_time);
    
    netInfo = NetInfo("dev");
    netInfo.LoadNetInfo();
    diffNetInfo = netInfo - oldNetInfo;
    totalIn += diffNetInfo.GetInMbps();
    totalOut += diffNetInfo.GetOutMbps();
    oldNetInfo = netInfo;
    print "In %.2f Mbps." % diffNetInfo.GetInMbps();
    print "Out %.2f Mbps." % diffNetInfo.GetOutMbps();

    cpuInfo = CpuInfo("stat");
    cpuInfo.LoadCpuInfo();
    diffCpuInfo = cpuInfo - oldCpuInfo;
    diffCpuInfo.CalcUsage();
    oldCpuInfo = cpuInfo;
    maxUsage, maxIdx = diffCpuInfo.GetMaxUsage();
    print "Cpu %d %.2f%%." % (maxIdx, maxUsage);

avgIn = totalIn / times;
avgOut = totalOut / times;
print "avgIn: %.2f Mbps" % avgIn;
print "avgOut: %.2f Mbps" % avgOut;
