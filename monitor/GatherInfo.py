#!/usr/bin/env python
# coding=utf-8

import os;
from Utils import *;

infoFileName = "test.dat"

def SaveWithIp(ips, name = infoFileName, remote_name = infoFileName, user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir):
    for ip in ips:
        CopyFrom(ip, name + "." + ip, remote_name, user, pwd, local_dir, remote_dir);


SaveWithIp(presscall_ips_red, pwd = red_password);
SaveWithIp(presscall_ips);
SaveWithIp(lsvr_ips);
SaveWithIp(d_access_ips, pwd = red_password);
SaveWithIp(sr_access_ips, pwd = red_password);
SaveWithIp(d_cache_ips, pwd = red_password);
SaveWithIp(sr_cache_ips, pwd = red_password);
