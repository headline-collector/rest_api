__author__ = 'wangyi'

import re

FIELDS_LIMIT_RE = re.compile(r"(\+|-)?\((?P<fields>[\w]+(?:,[\w]+)*)\)")

def field_parse(fields_string):
    """
    +(field_1, field_2, ...)
    -(field_1, field_2, ...)
     (field_1, field_2, ...)
    """
    mtch = FIELDS_LIMIT_RE.match(fields_string)
    if not mtch:
        raise Exception("Not Matched!")
    arr = mtch.groups()
    if arr[0] in (u'+', u'-'):
        sign = arr[0]
    else:
        sign = u'+'
    return sign, arr[1].split(',')
