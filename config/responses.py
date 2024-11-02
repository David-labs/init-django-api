from typing import Optional

from django.http import HttpResponse
from ninja.errors import HttpError


def _gen_resp(message, resp_data: Optional[dict], status_code):
    if resp_data:
        data = {'code':status_code,'detail': message, **resp_data}
    else:
        data = {'code':status_code,'detail': message}

    if status_code >= 500:
        HttpResponse(data, status=status_code, content_type='application/json')

    return data


def ok(message: str, data: Optional[dict] = None):
    return _gen_resp(message, data, 200)


def forbidden(message: str, data: Optional[dict] = None):
    return _gen_resp(message, data, 403)


def bad_request(message: str, data: Optional[dict] = None):
    return _gen_resp(message, data)

def fail_request(message: str,code=400):
    return _gen_resp(message, None, code)

def not_found(message: str, data: Optional[dict] = None):
    return _gen_resp(message, data, 404)


def unauthorized(message: str, data: Optional[dict] = None):
    return _gen_resp(message, data, 401)


def error(message: str, data: Optional[dict] = None):
    return _gen_resp(message, data, 500)
