#!/usr/bin/python3
"""
This is a Fabric script to create and distribute
an archive to web servers using the deploy function.
"""

from fabric.api import task, env, run, put
from fabric.state import output
from fabric.colors import green, red
from os.path import isfile
import pack_web_static
import do_deploy_web_static

"""
    output
"""
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
    archive_path = pack_web_static.do_pack()

    if not archive_path or not isfile(archive_path):
        print(red("Failed to create archive. Deployment aborted."))
        return False

    print(green("Archive created: {}".format(archive_path)))
    deployment_result = do_deploy_web_static.do_deploy(archive_path)

    if deployment_result:
        print(green("Deployment successful!"))
        return True
    else:
        print(red("Deployment failed."))
        return False

if __name__ == "__main__":
    env.hosts = ['54.152.171.203', '18.208.222.249']
    env.user = 'ubuntu'
    env.key_filename = '/root/.ssh/school'

    deploy()
