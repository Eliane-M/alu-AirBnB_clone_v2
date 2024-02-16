#!/usr/bin/python3
"""
a Fabric script to distribute
an archive to web servers using the function do_deploy.
using 1-pack_web_static.py
"""

from fabric.api import env, run, put, local
from os.path import exists, isdir
from datetime import datetime
import os
from fabric.api import *
env.hosts = ['54.160.49.83', '3.90.189.37']



env.hosts = ['54.152.171.203', '18.208.222.249']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
