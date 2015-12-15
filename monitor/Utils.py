#!/usr/bin/env python
# coding=utf-8

import os;

presscall_ips_red = [];
presscall_ips = [];
lsvr_ips = [];
d_access_ips = [];
sr_access_ips = [];
d_cache_ips = [];
sr_cache_ips = [];
password = "";
red_password = "";
kv_user = "";
kv_password = "";
local_dir = "";
remote_dir = "";

def CopyFile(ip, name = "", remote_name = "", user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir, is_copy_from = True):
    path = local_dir;
    remote_path = remote_dir;
    if name != "":
        path += "/" + name;

    if remote_name != "":
        remote_path += "/" + remote_name;

    cmd = "";
    if not is_copy_from:
        cmd = "sh remote_cp.sh -i " + ip + " -l " + user + " -P " + pwd + " -f " + path + " -t " + remote_path;
        cmd += " -a";
    else:
        cmd = "sh remote_cp.sh -i " + ip + " -l " + user + " -P " + pwd + " -f " + remote_path + " -t " + path;
    print cmd;
    #os.system(cmd);

def CopyFileByIps(ips, name = "", remote_name = "", user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir, is_copy_from = True):
    for ip in ips:
        CopyFile(ip, name, remote_name, user, pwd, local_dir, remote_dir, is_copy_from);

def CopyToIps(ips, name = "", remote_name = "", user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir):
    CopyFileByIps(ips, name, remote_name, user, pwd, local_dir, remote_dir, False);

def CopyFromIps(ips, name = "", remote_name = "", user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir):
    CopyFileByIps(ips, name, remote_name, user, pwd, local_dir, remote_dir);

def CopyTo(ip, name = "", remote_name = "", user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir):
    CopyFile(ip, name, remote_name, user, pwd, local_dir, remote_dir, False);

def CopyFrom(ip, name = "", remote_name = "", user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir):
    CopyFile(ip, name, remote_name, user, pwd, local_dir, remote_dir);

if __name__ == "__main__":
    print "CopyToIps:"
    CopyToIps(presscall_ips_red, "test.dat", "test.dat");
    print "";

    print "CopyFromIps:";
    CopyFromIps(presscall_ips_red, pwd = red_password);
    print "";

    print "CopyTo:";
    CopyTo(presscall_ips[0], remote_dir = "/");
    print "";

    print "CopyFrom:"
    CopyFrom(presscall_ips[0]);
    print "";
