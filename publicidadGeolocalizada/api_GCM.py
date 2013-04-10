
"""
api_GCM.py: Se encarga de las notificaciones push
para el dispositivo android

@author Eric Huerta
@date 05/04/2013
"""

from models import *
from conversionTipos import *
from django.contrib.auth.models import User
from django.db import connection
from utilidades import *
connection._rollback()
#import pdb

import urllib
import urllib2


def send_gcm_message(api_key, reg_id, data, collapse_key=None):

    values = {
        "registration_id": reg_id,
        "collapse_key": collapse_key,
    }

    for k, v in data.items():
        values["data.%s" % k] = v.encode('utf-8')

    data = urllib.urlencode(values)

    headers = {
        'UserAgent': "GCM-Server",
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'key=' + api_key,
        'Content-Length': str(len(data))
    }

    request = urllib2.Request("https://android.googleapis.com/gcm/send", data, headers)
    response = urllib2.urlopen(request)
    result = response.read()

    return result

