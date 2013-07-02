import os
from pecan import conf, expose, redirect


class DashboardController(object):

    def __init__(self, name):
        self.name = name
        self.dir  = "%s/%s" % (conf.app.static_root, self.name)

    def exists(self):
       return os.path.exists(conf.dashboards.get(self.name, ''))

    @expose('dashboards.html')
    def index(self):
        if not self.exists():
            redirect('/errors/notfound')
        return {
            'name': self.name,
            'graphite_url': conf.graphite_url
        }
