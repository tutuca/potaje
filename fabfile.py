#!/usr/bin/env python
#-- coding: utf-8 --

"""Deployment script.
This script is coded so it can make the deployments automagically in the
designed servers, it also works as a documentation of where are the programs
installed.
USE: fab <hosts>:<username> <action>
EX: fab staging:admin release
"""
import os
import datetime
from fabric.api import env, run, local, require, put, cd, lcd, prefix
from fabric.contrib.files import exists

BASEDIR = os.path.dirname(__file__)
env.static_dir = os.path.join(BASEDIR, 'static')
env.project_name = 'potaje'
env.bundle_built = False
env.tar = "%s-%s.tar.gz" % (
    env.project_name,
    datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
)
env.bundle = "%s-static.tar.gz" % (
    env.project_name,
)

def staging(username, host):
    """Staging environment."""
    env.hosts = host
    env.user = username
    env.base_dir = BASEDIR
    env.static_root = os.path.join(env.base_dir, 'static_%s' % env.project_name)
    env.deploy_dir = os.path.join(env.base_dir, 'build', env.project_name)
    env.virtual_env = os.path.join(env.base_dir, 'venvs', env.project_name
    env.server_command = os.path.join(
        env.base_dir,
        'webapps',
        env.project_name,
        'apache2/bin/restart'
    )

def production(username, host, base_dir):
    """Production environment."""
    env.hosts = host
    env.user = username
    env.base_dir = base_dir
    env.static_root = os.path.join(env.base_dir, 'static_%s' % env.project_name)
    env.deploy_dir = os.path.join(env.base_dir, 'webapps', env.project_name)
    env.virtual_env = os.path.join(env.base_dir, 'venvs', env.project_name
    env.server_command = os.path.join(
        env.base_dir,
        'webapps',
        env.project_name,
        'apache2/bin/restart'
    )

def release(rev='HEAD'):
    """Create a tarball, uploads it and decompresses it in the rigth path."""
    require("host", provided_by=[production, staging])
    require("deploy_dir", provided_by=[production, staging])
    require("virtual_env", provided_by=[production, staging])
    tar = env.tar
    local("git archive %s -o %s" % (rev, tar))
    put(tar, tar)
    run("tar xfz %s -C %s" % (tar, env.deploy_dir))
    # run("chown -R apache %s " % env.deploy_dir)
    run("rm %s" % tar)
    local("rm %s" % tar)

def build_static_bundle():
    """
    Create a tarball, for uploading.
    """
    # XXX: This expects the virtualenv to be activated already.
    # XXX: overcome that limitation using `prefix()` and context managers.

    require("project_name", provided_by=[production, staging])
    require("static_dir")
    local("npm start")
    local("manage collectstatic --noinput")

    with lcd(env.static_dir):
        local("tar cf %s *" % env.bundle)
        local("mv %s ../" % env.bundle)

def upload_static(force=False):
    """
    Uploads `env.bundle` and decompresses it in the right path
    This will attempt to create and delete local gzips.
    Cleanup is not always what it should...
    """
    require("project_name", provided_by=[production, staging])
    require("static_root", provided_by=[production, staging])
    if not exists(env.bundle) or force:
        build_static_bundle()
    put(env.bundle, env.bundle)
    run("tar xf ~/%s -C %s " % (env.bundle, env.static_root))
    local("rm %s" % env.bundle)

def apache_restart():
    """Restart the program in the servers."""
    require("server_command", provided_by=[production, staging])
    run(env.server_command)
