#!/usr/bin/python3
"""
This is a Fabric script to distribute
an archive to web servers using the function do_deploy.
"""

from fabric.api import env, run, put, local, task
from os.path import exists
from datetime import datetime

env.hosts = ['54.152.171.203', '18.208.222.249']
env.user = 'ubuntu'

@task
def do_deploy(archive_path):
    """
    Distribute an archive to web servers and perform deployment steps.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if all operations are successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:

        put(archive_path, '/tmp/')
        archive_filename = archive_path.split("/")[-1]
        release_folder = "/data/web_static/releases/{}".format(archive_filename.split(".")[0])
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}".format(release_folder, release_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False