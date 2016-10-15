__author__ = 'wangyi'

import hmac
import hashlib
import base64
from uuid import uuid4
import random

from django.utils import timezone
from api.utils.datetime import to_seconds_from_datetime


def app_key_gen(dev_name):
    random.seed()
    _now = timezone.now()
    # to prevent from being guessed by others
    return dev_name.upper() + _now.strftime('%d%M%Y%H%M') + str(random.randrange(to_seconds_from_datetime(_now)))

def app_secret_coder(api_secret, msg):
    digest_obj = hmac.new(api_secret, msg=msg, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest_obj).decode()

def app_secret_gen(str):
    coder = hashlib.sha256()
    salt = uuid4().hex
    coder.update(str+timezone.now().strftime('%H%M%S')+salt)
    return coder.hexdigest()

def check_sign_sim(sign_req, sign_serv):
    # check algorithm
    # decide cmp algorithm and whether to update
    return sign_req == sign_serv
