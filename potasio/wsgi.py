import os
from pecan.deploy import deploy
import pecan_mount

def config_file():
    _file = os.path.abspath(__file__)
    dirname = lambda x: os.path.dirname(x)
    parent_dir = dirname(dirname(_file))
    return os.path.join(parent_dir, 'config.py')

pecan_mount.tree.mount('/', config_file())
pecan_mount.tree.mount('/fu', config_file())
pecan_mount.tree.mount('/admin', config_file())
application = pecan_mount.tree
#application = deploy(config_file())
