__author__ = 'wangyi'

import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.response import Response

def sys_exc_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        pass

    return response

def handle_exc(ref, status_code, details=None):
    cause = {'Cause': "<'%s'> Does Not Exist!" % ref, 'details':details}
    rep = Response(data=cause, status=status_code)
    return rep

class REST_APIException(APIException):

    status_code = status
    default_details = ""

    def __init__(self, detail=None):
        if detail is None:
            self.detail = self.default_details
        else:
            self.detail = {'msg':detail, 'default':self.default_details}

class REST_API_DBException(REST_APIException):pass
class Lost_Conn(REST_API_DBException):pass
class Field_Voilation(REST_API_DBException):pass

class REST_API_Auth_Exception(REST_APIException):pass

class REST_API_INPUT_Excepiton(REST_APIException):pass
class Cols_Not_Found(REST_API_INPUT_Excepiton):

    status_code = status.SYS_5001_COLS_NOT_FOUND
    default_details = "Cols Not Matched"

class BAD_SIGN(REST_API_INPUT_Excepiton):

    status_code = status.SYS_5002_BAD_SIGN
    default_details = "Sign Is Bad!"

class Func_Exception(REST_APIException):

    status_code = status.SYS_2001_FUNC_METHOD_DOES_NOT_MATCH_THE_PARAMETERS
    default_details = "Parameters provided does not fit into the function"

class MultiReq_Exception(REST_API_Auth_Exception):

    status_code = status.SYS_3001_MULTI_REQUEST_FORBIDDEN
    default_details = "Multiple requests should not be made"

class SignatureFailed_Exception(REST_APIException):

    status_code = status.SYS_3002_SIGNATURE_NOT_PASS
    default_details = "Signature not passed"




