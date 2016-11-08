__author__ = 'wangyi'
from django.dispatch import Signal

user_signing = Signal(providing_args=['request', 'user'])
user_false_singed = Signal(providing_args=['credentials'])
user_signed = Signal(providing_args=['request', 'user'])