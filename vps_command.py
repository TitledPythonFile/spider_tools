#!usr/bin/python
# encoding:utf-8
# author:masako
# date:2018/05/23

"""
dial vps change ip commands
"""

import subprocess


def call_cmd(cmd):
    try:
        r = subprocess.call(cmd)
    except Exception as e:
        print e
        return False

    if r == 0:
        return True
    return False


def net_stop():
    cmd = 'pppoe-stop'
    return call_cmd(cmd)


def net_start():
    cmd = 'pppoe-start'
    return call_cmd(cmd)


def stop_net_server():
    cmd = '/bin/systemctl stop NetworkManager.service'
    return call_cmd(cmd)


def has_net():
    cmd = ['curl', 'www.baidu.com']
    return call_cmd(cmd)


def dial():
    try_count = 0
    stop_net_server()
    while try_count < 3:
        net_stop()
        net_start()
        if has_net():
            return True
        try_count += 1

    return False
