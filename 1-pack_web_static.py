#!/usr/bin/python3
"""
deploy archive
"""

from fabric.api import *
from datetime import datetime


def do_pack():
  timestr = datetime.strftime("%Y%m%d%H%M%S")
  try:
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static/".
    format(timestr))
    return ("versions/web_static_{}.tgz".format(timestr))
  except:
    return None
