#!/usr/bin/env python
# coding=utf-8

from NetInfo import NetInfo;
from CpuInfo import CpuInfo;

netInfo = NetInfo("dev");
cpuInfo = CpuInfo("stat");
maxUsage, maxIdx = cpuInfo.GetMaxUsage();
print maxUsage;
print maxIdx;
