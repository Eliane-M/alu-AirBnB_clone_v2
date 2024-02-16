#!/usr/bin/python3
"""
This is a Fabric script to create and distribute an archive to web servers using the deploy function.
"""

from fabric.api import task, env, run, put
from fabric.state import output
from fabric.colors import green, red
from os.path import isfile

# Importing modules with modified names
import pack_web_static
import do_deploy_web_static

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
    archive_path = pack_web_static.do_pack()

    if not archive_path or not isfile(archive_path):
        print(red("Failed to create archive. Deployment aborted."))
        return False

    print(green("Archive created: {}".format(archive_path)))

    # Call the do_deploy function using the new path of the new archive
    deployment_result = do_deploy_web_static.do_deploy(archive_path)

    if deployment_result:
        print(green("Deployment successful!"))
        return True
    else:
        print(red("Deployment failed."))
        return False

if __name__ == "__main__":
    # Set your server IP addresses, username, and private key
    env.hosts = ['<IP web-01>', '<IP web-02>']
    env.user = '<your_username>'
    env.key_filename = '<path_to_your_private_key>'

    deploy()