from typing import List
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.pagination import paginate
from config import responses
from .apis_request import req
from .models import *
from .schemas import *
import os,time
from .utils import libs
from .db import *
from functools import wraps
import json
import hashlib
from django.http import FileResponse
import os
from django.conf import settings


def require_sign(view_func):
    @wraps(view_func)
    def decorated_function(request, *args, **kwargs):
        # 替换key
        key = 'secretKey'
        sign = request.headers.get('Authorization')
       
        if request.method == 'GET':
            args_dict = request.GET.dict()
        elif request.method == 'POST':
            if request.content_type == 'application/json':
                try:
                    args_dict = json.loads(request.body)
                except json.JSONDecodeError:
                    args_dict = {}
            else:
                args_dict = request.POST.dict()
        
        arg_json = ''
        if args_dict:
            arg_json = json.dumps(args_dict, separators=(',', ':'))
        # print(sign)
        print(arg_json)
        md5 = hashlib.md5()
        md5.update((arg_json + key).encode())
        computed_sign = md5.hexdigest()
        
        if not sign:
            return responses.error('No sign provided')
        elif sign != computed_sign:
            print(f"receive sign '{sign}'")
            print(f"server sign '{computed_sign}'")
            return responses.error('Invalid sign')
        return view_func(request, *args, **kwargs)
    return decorated_function

router = Router(tags=['api_v1'])

@router.get("/hello")
def hello(request):
    return "Hello World!"


    