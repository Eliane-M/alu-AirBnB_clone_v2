#!/usr/bin/python3
"""
a Fabric script to distribute
an archive to web servers using the function do_deploy.
using 1-pack_web_static.py
"""

from fabric.api import env, run, put, local
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['54.160.49.83', '3.90.189.37']


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if successfully generated, None otherwise.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate timestamp for the archive name
        timestr = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the .tgz archive
        archive_path = "versions/web_static_{}.tgz".format(timestr)
        local("tar -cvzf {} web_static/".format(archive_path))

        return archive_path
    except Exception as e:
        print(e)
        return None


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
    except:
	return False

def deploy():
    """
    creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
