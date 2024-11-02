import json
import hashlib
from datetime import datetime, timezone, timedelta
from api.models import *
import ipaddress
import random
from django.apps import apps

def getParam(request, key, default=None):
    if request.method == 'GET':
        return request.GET.get(key, default)
    elif request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                json_data = json.loads(request.body.decode('utf-8'))
                return json_data.get(key, default)
            except json.JSONDecodeError:
                return default
        else:
            return request.POST.get(key, default)
    return default

def md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode())
    return md5.hexdigest()

def timeTransfer(time):
    timestamp_in_seconds = time / 1000
    date = datetime.fromtimestamp(timestamp_in_seconds, tz=timezone.utc)
    return date.strftime('%Y-%m-%d %H:%M:%S')

    