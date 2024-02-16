#!/usr/bin/python3
"""
This is a Fabric script to create and distribute an archive to web servers using the deploy function.
"""

from fabric.api import task
from fabric.state import output
from fabric.colors import green, red
from os.path import isfile
from fabric.operations import local

from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

output['running'] = False
output['warnings'] = False
output['stdout'] = False
output['stderr'] = False

@task
def deploy():
    """
    Create and distribute an archive to web servers using do_pack and do_deploy.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Call the do_pack function and store the path of the created archive
    archive_path = do_pack()

    if not archive_path or not isfile(archive_path):
        print(red("Failed to create archive. Deployment aborted."))
        return False

    print(green("Archive created: {}".format(archive_path)))

    # Call the do_deploy function using the new path of the new archive
    deployment_result = do_deploy(archive_path)

    if deployment_result:
        print(green("Deployment successful!"))
        return True
    else:
        print(red("Deployment failed."))
        return False

if __name__ == "__main__":
    deploy()