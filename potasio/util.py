import os
from os import path


def clean_pyfile(filename):
    return filename.split('.js')[0]


def get_dashboard_files():
    root_path = os.path.dirname(__file__)
    file_map = {}
    dashboard_dir = path.join(path.dirname(root_path), 'public/dashboards')
    for filename in os.listdir(dashboard_dir):
        file_map[clean_pyfile(filename)] = path.join(dashboard_dir, filename)
    return file_map


def dashboards():
    return get_dashboard_files()
    #return [name for name, path in get_dashboard_files()]
