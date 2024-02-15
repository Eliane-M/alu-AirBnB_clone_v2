#!/usr/bin/python3
"""
This is module 1-pack_web_static.py
The following is a fabfile
"""

from fabric.api import local
from datetime import datetime

@task
def do_pack():
  """
    a Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
  """
  timestr = datetime.strftime("%Y%m%d%H%M%S")
  try:
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static/".
    format(timestr))
    return ("versions/web_static_{}.tgz".format(timestr))
  except:
    return None
