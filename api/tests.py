# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import SimpleTestCase, TestCase
from utils.auth_utils import app_key_gen, app_secret_coder, app_secret_gen, check_sign_sim
import logging
from utils.log import LoggerAdaptor
_logger = logging.getLogger("api.tests")
import json

developer_name = 'Yiak'
password = '123456yiak'
msgs_without_header = "Get http://www.example.com?Date=2016-3-1 00:00:00"

class SignatureTest(SimpleTestCase):

    logger = LoggerAdaptor("TestSignature", _logger)

    def test_app_key_secret_gen(self):
        APP_KEY =  app_key_gen()
        APP_SECRET = app_secret_gen()
        self.logger.info("[INFO] test_app_key_secret: %s: %s" % (APP_KEY, APP_SECRET))


class AppModelTest(SimpleTestCase):

    # logger = LoggerAdaptor("TestApp", _logger)

    def test_create_app(self):
        from api.models import App
        import names
        my_app = App.objects.create('test_app01', '123456', 'test01@gmail.com')

if __name__ == "__main__":
    from urllib import urlencode
    test_str = urlencode("http://127.0.0.1:8000/api/0.1.3/articles/2016%E8%AF%A5%E4%B9%B0%E6%88%BF%E8%BF%98%E6%98%AF%E8%AF%A5%E5%8D%96%E6%88%BF%EF%BC%9F/")
    print(test_str)