import launch

# TODO: add pip dependency if need extra module only on extension

# if not launch.is_installed("aitextgen"):
#     launch.run_pip("install aitextgen==0.6.0", "requirements for Downloader")

import apt
cache = apt.Cache()
cache.open()
if cache is None:
    launch.run('apt-get -y install -qq aria2'.split(' '), 'Install requirements for Downloader')