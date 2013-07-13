import os
from pecan.deploy import deploy

def config_file():
    _file = os.path.abspath(__file__)
    dirname = lambda x: os.path.dirname(x)
    parent_dir = dirname(dirname(_file))
    return os.path.join(parent_dir, 'prod_config.py')

application = deploy(config_file())
