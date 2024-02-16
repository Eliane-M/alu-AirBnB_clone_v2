#!/usr/bin/python3
# generates an archive out of web-static folder

from fabric import task as fabric_task
from fabric.operations import local
from datetime import datetime


def do_pack(c):
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if successfully generated, None otherwise.
    """
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error occurred while creating archive:", e)
        return None
