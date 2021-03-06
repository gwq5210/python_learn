#!/usr/bin/env python
# coding=utf-8

class NetInfo:
    def __init__(self, filename = "/proc/net/dev"):
        self.filename = filename;
        self.info = {};

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

    def GetInMbps(self, dev_name = "eth0", sleep_time = 1):
        return self.info[dev_name]["in_bytes"] * 8.0 / 1000000 / sleep_time;

    def GetOutMbps(self, dev_name = "eth0", sleep_time = 1):
        return self.info[dev_name]["out_bytes"] * 8.0 / 1000000 / sleep_time;

    def __sub__(self, otherInfo):
        retInfo = {};
        for name in self.info:
            devInfo = {};
            for key in self.info[name]:
                devInfo[key] = self.info[name][key] - otherInfo.info[name][key];
            retInfo[name] = devInfo;
        ret = NetInfo();
        ret.info = retInfo;
        return ret;

if __name__ == "__main__":
    eth = "eth1";
    netInfo = NetInfo("dev");
    netInfo.LoadNetInfo();
    otherInfo = NetInfo("dev");
    otherInfo.LoadNetInfo();
    eth_info = netInfo.GetDevInfo(eth);
    print eth_info;
    otherInfo.info[eth]["in_bytes"] = 1;
    diffInfo = netInfo - otherInfo;
    print diffInfo.info[eth]["in_bytes"];
    print "In %.2f." % diffInfo.GetInMbps(eth);
    print "Out %.2f." % diffInfo.GetOutMbps(eth);
