from pecan.hooks import  RequestViewerHook

from potasio import util

# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'potasio.controllers.root.RootController',
    'modules': ['potasio'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/potasio/templates',
    'debug': True,
    'hooks': [
        RequestViewerHook({'blacklist': ['/favicon.ico', '/javascript', '/static']}),
    ],
    'errors': {
        '__force_dict__': True
    }
}

logging = {
    'loggers': {
        'root' : {'level': 'INFO', 'handlers': ['console']},
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        }
    }
}

dashboards = util.dashboards()

graphite_url = 'http://graphite.example.com'
