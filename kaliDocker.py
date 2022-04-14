#!/usr/bin/python3

import os
import argparse


argparser = argparse.ArgumentParser()

argparser.add_argument("-n", "--name", help="name container", required=True)
argparser.add_argument("-htb", "--hackthebox",
                       help="hackthebox volume", required=True)


def prepare():

    args = argparser.parse_args()

    name = args.name
    htb = args.hackthebox

    code = os.path.exists(htb)
    assert code, f'directory {htb} does not exists'
    cmd = ""
    cmd += f'docker run -it --name {name} '
    cmd += "--cap-add=NET_ADMIN --device /dev/net/tun "
    cmd += "--sysctl net.ipv6.conf.all.disable_ipv6=0 "
    cmd += f'-v /tmp/.X11-unix:/tmp/.X11-unix '
    cmd += f'-v {htb}:/root/HTB '
    cmd += f'kalilinux/kali-rolling:latest /bin/bash'

    return cmd


if __name__ == "__main__":
    os.system(prepare())
