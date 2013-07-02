# Server Specific Configurations
server = {
    'port' : '8080',
    'host' : '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root'            : 'potasio.controllers.root.RootController',
    'modules'         : ['potasio'],
    'static_root'     : '%(confdir)s/../../public', 
    'template_path'   : '%(confdir)s/../templates',
    'debug'           : True,
    'errors'          : {
        '404'            : '/error/404',
        '__force_dict__' : True
    }
}


dashboards = {'example': '/'}
# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
# 
# All configurations are accessible at::
# pecan.conf
