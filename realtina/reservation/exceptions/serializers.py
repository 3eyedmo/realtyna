from rest_framework.exceptions import APIException


class InvalidSaveOperationException(APIException):
    """
    This Exception is raised when model instance cant be saved.
    """
    status_code = 400
    
