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

if __name__ == "__main__":
    print GetProcessCpuInfo("test", True);
    print GetProcessCpuInfo("test");
    print "\x1b[0;10m0.0";
    print "0.0";
    print "\033[1;31;1m0.0";
