#!/usr/bin/env python
# coding=utf-8

class CpuNetInfo:
    def __init__(self):
        self.avgIn = 0.0;
        self.avgOut = 0.0;
        self.avgCpu = 0.0;
        self.processCpu = {};

    def __str__(self):
        retStr = "";
        retStr += "avgIn %.2f\n" % avgIn;
        retStr += "avgOut %.2f\n" % avgOut;
        retStr += "avgCpu %.2f\n" % avgCpu;
        for process_name in self.processCpu:
            retStr += process_name + ":\n";
            retStr += str(self.processCpu[process_name]) + "\n";
        return retStr.strip();
