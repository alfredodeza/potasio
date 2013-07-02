from pecan import expose, request, response


class ErrorsController(object):

    @expose('errors.html')
    def validation(self):
        response.status = 400
        return {'message':request.pecan['validation_errors']}

    @expose('json')
    def forbidden(self):
        response.status = 403
        return {'message': 'Not allowed'}

    @expose('errors.html')
    def database(self):
        response.status = 500
        return {'message':'Internal Server Error'}

    @expose('errors.html')
    def notfound(self):
        response.status = 404
        return {'message':'Not Found'}

    @expose('errors.html')
    def unable(self):
        """
        Unable to continue because of current state.
        Usually meant for instances that need to
        be in a certain condition before modification occurs.
        """
        response.status = 400
        return {'message':'current state does not allow modification'}

    @expose('errors.html')
    def not_implemented(self):
        """
        Unable to continue because the server could not fulfill
        the request.
        Most of the time is due to a third party request.
        """
        response.status = 501
        return {'message':'server was not able to complete this request'}
