#!/usr/bin/env python
# coding=utf-8

import os;
import sys;

class ProcessCpuInfo:
    def __init__(self, name = ""):
        self.name = name;
        self.info = {};
        self.infoStr = "";
        self.usageKey = "usage";

    def GetProcessCpuInfo(self):
        cmd = "top -b -n 1 | grep " + self.name + " | sed 's/^[ ]*//g' | awk '{print $12, $9}' | sort";
        self.infoStr = os.popen(cmd).read();
        self.infoStr = self.infoStr.strip();
        if (self.infoStr == ""):
            return;
        ret = {};
        for line in self.infoStr.split("\n"):
            datas = line.split();
            ret[datas[0]] = float(datas[1]);
        self.info = ret;

    def Clear(self):
        for name in self.info:
            self.info[name] = 0.0;
        self.infoStr = "";

    def CalcUsage(self, times):
        for name in self.info:
            self.info[name] = self.info[name] / times;
        self.infoStr = str(self).strip();

    def __sub__(self, otherInfo):
        retInfo = {};
        for name in self.info:
            retInfo[name] = self.info[name] - otherInfo.info[name];
        ret = ProcessCpuInfo();
        ret.info = retInfo;
        ret.infoStr = str(ret).strip();
        return ret;

    def __add__(self, otherInfo):
        retInfo = {};
        for name in self.info:
            retInfo[name] = self.info[name] + otherInfo.info[name];
        ret = ProcessCpuInfo();
        ret.info = retInfo;
        ret.infoStr = str(ret).strip();
        return ret;

    def __str__(self):
        retStr = "";
        for name in self.info:
            retStr += name + " " + str(self.info[name]) + "\n";
        return retStr.strip();



class CpuInfo:
    def __init__(self, filename = "/proc/stat"):
        self.info = {};
        self.filename = filename;
        self.usageKey = "usage";

    def GetCoreNum(self):
        return len(self.info) - 1;

    def LoadCpuInfo(self):
        with open(self.filename) as f:
            for line in f:
                coreInfo = {};
                datas = line.split();
                name = datas[0];
                if name.find("cpu") < 0:
                    continue;
                coreInfo["user"] = int(datas[1]);
                coreInfo["nice"] = int(datas[2]);
                coreInfo["system"] = int(datas[3]);
                coreInfo["idle"] = int(datas[4]);
                coreInfo["iowait"] = int(datas[5]);
                coreInfo["irq"] = int(datas[6]);
                coreInfo["softirq"] = int(datas[7]);
                self.info[name] = coreInfo;

    def GetCoreInfo(self, idx):
        key = "cpu%d" % idx;
        return self.info[key];

    def GetCoreUsage(self, idx):
        return self.GetCoreInfo(idx)[self.usageKey];

    def GetAveUsage(self, idx):
        return self.GetAveInfo()[self.usageKey];

    def GetMaxUsage(self):
        idx = -1;
        maxUsage = 0.0;
        coreNum = self.GetCoreNum();
        for num in range(coreNum):
            key = "cpu%d" % num;
            coreInfo = self.info[key];
            if coreInfo[self.usageKey] > maxUsage:
                maxUsage = coreInfo[self.usageKey];
                idx = num;
        return maxUsage, idx

    def GetAvgInfo(self):
        key = "cpu";
        return self.info[key];

    def CalcUsage(self):
        for key in self.info:
            coreInfo = self.info[key];
            total = 0;
            for coreKey in coreInfo:
                total += coreInfo[coreKey];
            used = total - coreInfo["iowait"] - coreInfo["idle"];
            if total == 0:
                coreInfo[self.usageKey] = 0;
            else:
                coreInfo[self.usageKey] = used * 100.0 / total;

    def __sub__(self, otherInfo):
        retInfo = {};
        for name in self.info:
            coreInfo = {};
            for key in self.info[name]:
                coreInfo[key] = self.info[name][key] - otherInfo.info[name][key];
            retInfo[name] = coreInfo;
        ret = CpuInfo();
        ret.info = retInfo;
        ret.CalcUsage();
        return ret;

if __name__ == "__main__":
    #cpuInfo = CpuInfo("stat");
    cpuInfo = CpuInfo();
    cpuInfo.LoadCpuInfo();
    cpuInfo.CalcUsage();
    print "CoreNum %d." % cpuInfo.GetCoreNum();
    print "Core %d Info:\n%s" % (1, cpuInfo.GetCoreInfo(1));
    print "Ave Info:"
    print cpuInfo.GetAvgInfo();

    maxUsage, maxIdx = cpuInfo.GetMaxUsage();
    coreNum = cpuInfo.GetCoreNum();
    print "maxUsage: %.2f" % maxUsage;
    print "maxIdx: %d" % maxIdx;
    print "CoreNum: %d" % coreNum;

    cpuInfo = cpuInfo - cpuInfo;
    maxUsage, maxIdx = cpuInfo.GetMaxUsage();
    print "maxUsage: %.2f" % maxUsage;
    print "maxIdx: %d" % maxIdx;

    pCpuInfo = ProcessCpuInfo("LSvr_mcp");
    pCpuInfo.GetProcessCpuInfo();
    print pCpuInfo.infoStr;
    pCpuInfo.CalcUsage(1);
    print pCpuInfo.infoStr;
    pCpuInfo = pCpuInfo + pCpuInfo;
    print pCpuInfo.infoStr;
    pCpuInfo = pCpuInfo - pCpuInfo;
    print pCpuInfo.infoStr;
