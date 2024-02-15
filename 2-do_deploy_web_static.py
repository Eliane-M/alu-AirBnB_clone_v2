#!/usr/bin/python3
"""
This is 2-do_deploy_web_static.py module and houses the 'do_deploy' function.
"""
import os.path
from fabric.api import env
from fabric.operations import run, put, sudo
env.hosts = ['54.152.171.203', '18.208.222.249']


def do_deploy(archive_path):
    """
        a Fabric script that generates a .tgz archive from the contents of the
        web_static folder of your AirBnB Clone repo, using the function do_pack.
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_comp, new_folder))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False
