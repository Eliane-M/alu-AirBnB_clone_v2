#!/usr/bin/python3
"""
generates an archive out of web-static folder
using do_pack before sending
"""

from fabric.api import task
from fabric.api import local
from datetime import datetime


@task
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
