#!/usr/bin/env python
# coding=utf-8

testApiSet = set(["SEND_HB", "OPEN_HB", "GET_SEND", "GET_RECV"])
apiRowMap = {"SEND_HB": 19, "RUSH_CHECK": 20, "OPEN_CHECK": 21, "OPEN_HB_100": 22, "OPEN_HB": 23,
        "CHANGE_STATUS": 24, "GET_DHEADER": 25, "GET_DLIST": 26, "GET_SEND": 27, "GET_RECV": 28,
        "DEL_SEND": 29, "DEL_RECV": 30};
dataColMap = {"THREAD_NUM": 1, "TPS": 2, "AVG_TIME": 3, "MAX_TIME": 4, "LEVEL3": 5, "LEVEL2": 6,
        "LEVEL1": 7, "LSVR_CPU": 8, "LRSYNC_CPU": 9, "LSVR_IN": 10, "LSVR_OUT": 11, "SR_ACCESS_CPU": 12,
        "SR_ACCESS_IN": 13, "SR_ACCESS_OUT": 14, "D_ACCESS_CPU": 15, "D_ACCESS_IN": 16, "D_ACCESS_OUT": 17,
        "SR_CACHE_CPU": 18, "SR_CACHE_IN": 19, "SR_CACHE_OUT": 20, "D_CACHE_CPU": 21, "D_CACHE_IN": 22,
        "D_CACHE_OUT": 23};

presscall_ips_red = ["127.0.0.1"];
presscall_ips = ["127.0.0.1"];
lsvr_ips = ["127.0.0.1"];
d_access_ips = ["127.0.0.1"];
sr_access_ips = ["127.0.0.1"];
d_cache_ips = ["127.0.0.1"];
sr_cache_ips = ["127.0.0.1"];
password = "password";
red_password = "red_password";
kv_user = "kv_user";
kv_password = "kv_password";
local_dir = "local_dir";
remote_dir = "remote_dir";
infoFileName = "infoFileName";
presscall_local_dir = "presscall_local_dir";
presscall_remote_dir = "presscall_remote_dir";
presscall_file = "presscall_file";

class CpuNetInfo:
    def __init__(self):
        self.avgIn = 0.0;
        self.avgOut = 0.0;
        self.avgCpu = 0.0;
        self.processCpu = {};

    def __str__(self):
        retStr = "";
        retStr += "avgIn %.2f\n" % self.avgIn;
        retStr += "avgOut %.2f\n" % self.avgOut;
        retStr += "avgCpu %.2f\n" % self.avgCpu;
        for process_name in self.processCpu:
            retStr += process_name + ":\n";
            retStr += str(self.processCpu[process_name]) + "\n";
        return retStr.strip();
