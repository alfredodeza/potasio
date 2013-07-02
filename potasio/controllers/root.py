from pecan import expose, conf

from potasio.controllers.dashboards import DashboardController


class RootController(object):

    @expose(template='index.html')
    def index(self):
        dashboards = conf.dashboards.to_dict()
        return dict(
            dashboards=dashboards.keys()
        )

    @expose()
    def _lookup(self, name, *remainder):
        return DashboardController(name), remainder
