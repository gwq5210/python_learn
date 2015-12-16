#!/usr/bin/env python
# coding=utf-8

import os;
from Common import *;
try:
    import cPickle as pickle;
except:
    import pickle;

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

def ExeRemoteCmd(ip, cmd_path, user = "root", pwd = password, port = 36000):
    cmd = "sh remote_cmd.sh -i %s -p %d  -l %s -P %s -c \"%s\"" % (ip, port, user, pwd, cmd_path);
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

def SaveWithIp(ips, name = infoFileName, remote_name = infoFileName, user = "root", pwd = password, local_dir = local_dir, remote_dir = remote_dir):
    for ip in ips:
        CopyFrom(ip, name + "." + ip, remote_name, user, pwd, local_dir, remote_dir);

def LoadMonitorInfo(ips, name = infoFileName, fileDir = local_dir):
    ret = {};
    for ip in ips:
        fileName = fileDir + "/" + name + "." + ip;
        print "open file %s." % fileName;
        #with open(fileName) as f:
        #    info = pickle.load(f);
        #    ret[ip] = info;
    return ret;

def LoadPresscallInfo(ips, name = presscall_file, fileDir = local_dir):
    ret = {};
    for ip in ips:
        fileName = fileDir + "/" + name + "." + ip;
        print "open file %s." % fileName;
        #with open(fileName) as f:
        #with open(fileName) as f:
        #    pass
    return ret;

def KillPresscall():
    for ip in presscall_ips:
        ExeRemoteCmd(ip, cmd_path = "sh /root/presscall_test/bin/kill_presscall.sh");
    for ip in presscall_ips_red:
        ExeRemoteCmd(ip, cmd_path = "sh /root/presscall_test/bin/kill_presscall.sh", pwd = red_password);

def StartPresscall(mcp_cnt, reqType, thread_num, run_seconds = 0, is_south = True):
    cmd = "cd %s; sh ./cnt_press_back.sh %d %d %d %d" % (presscall_remote_dir, mcp_cnt, reqType, thread_num, run_seconds);
    red_cmd = "cd %s; sh ./cnt_press_back.sh %d %d %d %d" % (presscall_remote_dir, mcp_cnt, reqType, thread_num / 2, run_seconds);
    if not is_south:
        cmd += " 1 &";
    else:
        cmd += " &";
    for ip in presscall_ips:
        ExeRemoteCmd(ip, cmd_path = cmd);
    for ip in presscall_ips_red:
        ExeRemoteCmd(ip, cmd_path = red_cmd, pwd = red_password);

def StartMonitor():
    cmd = "cd %s; python Monitor.py -o %s" % (remote_dir, infoFileName)
    for ip in lsvr_ips:
        ExeRemoteCmd(ip, cmd_path = cmd + " -p LSvr_mcp -p lrsync_mcp");
    for ip in d_access_ips:
        ExeRemoteCmd(ip, cmd_path = cmd, pwd = red_password);
    for ip in sr_access_ips:
        ExeRemoteCmd(ip, cmd_path = cmd, pwd = red_password);
    for ip in d_cache_ips:
        ExeRemoteCmd(ip, cmd_path = cmd, pwd = red_password);
    for ip in sr_cache_ips:
        ExeRemoteCmd(ip, cmd_path = cmd, pwd = red_password);

if __name__ == "__main__":
    print "CopyToIps:"
    CopyToIps(presscall_ips_red, "test.dat", "test.dat");

    print "CopyFromIps:";
    CopyFromIps(presscall_ips_red, pwd = red_password);

    print "CopyTo:";
    CopyTo(presscall_ips[0], remote_dir = "/");

    print "CopyFrom:"
    CopyFrom(presscall_ips[0]);

    print "StartPresscall:";
    StartPresscall(24, 1, 200, 120);
    StartPresscall(24, 1, 200, 120, is_south = False);

    print "KillPresscall:";
    KillPresscall();

    print "StartMonitor:";
    StartMonitor();
