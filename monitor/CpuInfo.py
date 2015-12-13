#!/usr/bin/env python
# coding=utf-8

import os;
import sys;

def GetProcessCpuInfo(name, ret_str = False):
    top_args = os.popen("ps aux | grep " + name + " | grep -v grep | awk '{print $2}' | sed 's/^/-p/g' | xargs").read();
    top_args = top_args.strip();
    info = os.popen("top -n 1 " + top_args + " | grep " + name + " | sed 's/ //1' | awk '{print $2, $1}' | sort").read();
    info = info.strip();
    ret = {};
    retStr = "";
    for line in info.split("\n"):
        datas = line.split();
        datas[1] = datas[1][datas[1].rfind('m') + 1:]; # 处理特殊字符串
        retStr += datas[0] + " " + datas[1] + "\n";
        ret[datas[0]] = float(datas[1]);
    if ret_str:
        return retStr.strip();
    else:
        return ret;


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
    cpuInfo = CpuInfo("stat");
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

    #print GetProcessCpuInfo("LSvr_mcp", True);
    #print GetProcessCpuInfo("LSvr_mcp");
    #print "\x1b[0;10m0.0";
    #print "0.0";
    #print "\033[1;31;1m0.0";
