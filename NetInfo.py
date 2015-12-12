#!/usr/bin/env python
# coding=utf-8

class NetInfo:
    def __init__(self, filename = "/proc/net/dev"):
        self.filename = filename;
        self.info = {};
        self.LoadNetInfo();

    def LoadNetInfo(self):
        with open(self.filename) as f:
            for line in f:
                devInfo = {};
                if line.find(":") < 0:
                    continue;
                name = line.split(":")[0].strip();
                datas = line.split(":")[1].split();
                devInfo["in_bytes"] = int(datas[0]);
                devInfo["in_packets"] = int(datas[1]);
                devInfo["in_errors"] = int(datas[2]);
                devInfo["in_drops"] = int(datas[3]);
                devInfo["in_fifo"] = int(datas[4]);
                devInfo["in_frame"] = int(datas[5]);
                devInfo["in_compressed"] = int(datas[6]);
                devInfo["in_multicast"] = int(datas[7]);
                devInfo["out_bytes"] = int(datas[8]);
                devInfo["out_packets"] = int(datas[9]);
                devInfo["out_errors"] = int(datas[10]);
                devInfo["out_drops"] = int(datas[11]);
                devInfo["out_fifo"] = int(datas[12]);
                devInfo["out_frame"] = int(datas[13]);
                devInfo["out_compressed"] = int(datas[14]);
                devInfo["out_multicast"] = int(datas[15]);
                self.info[name] = devInfo;

    def GetDevInfo(self, name):
        return self.info[name];

    def __sub__(self, otherInfo):
        retInfo = {};
        for name in self.info:
            devInfo = {};
            for key in self.info[name]:
                devInfo[key] = self.info[name][key] - otherInfo.info[name][key];
            retInfo[name] = devInfo;
        return retInfo;

if __name__ == "__main__":
    netInfo = NetInfo("dev");
    otherInfo = NetInfo("dev");
    eth1_info = netInfo.GetDevInfo("eth1");
    print eth1_info;
    otherInfo.info["eth1"]["in_bytes"] = 1;
    diffInfo = netInfo - otherInfo;
    print diffInfo["eth1"];
