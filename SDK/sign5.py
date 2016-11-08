__author__ = "Lei Wang"

import urllib, httplib
import hmac, hashlib, base64
from collections import OrderedDict
from datetime import datetime
try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse

test_headers = "(request-target) date"
Authorization = 'Signature key="{key}",algorithm="{algorithm}",headers="{headers}",signature="{signature}"'
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

def app_secret_coder(api_secret, msg, algorithm="hmac-sha256"):
    algo, hash_scheme = algorithm.split("-")
    if algo == "hmac" and hash_scheme == "sha256":
        digest_obj = hmac.new(api_secret, msg=msg, digestmod=hashlib.sha256).digest()
    else:
        raise Exception("(%s, %s) Not Be Supported Yet!" % (algo, hash_scheme))
    return base64.b64encode(digest_obj).decode()

def compose_signature(method, path, signed_headers):
    """
    Signing HTTP Messages draft-cavage-http-signature-signatures-05 Chapter 2.3(Construct a Signature)
    :return: `signature string`
    """
    signature_string = "(request-target): {method} {path}\n{ret}"

    def encode_signed_headers(signed_headers):
        # Signing HTTP Messages draft-cavage-http-signature-signatures-05 Rule 2.3.2

        args_processor = lambda (key, val): \
            ': '.join((key.lower(), ', '.join(val) )) if isinstance(val, (list, tuple)) and len(val) > 1 else \
            ': '.join((key.lower(), val[0] if isinstance(val, (list, tuple)) else val))
        map_ob = map(args_processor, signed_headers.items())
        return '\n'.join(map_ob)

    ret = encode_signed_headers(signed_headers)
    return signature_string.format(method=method, path=path, ret=ret)


def client(url, keyId, secret, algorithm, headers=None):
    parsed = urlparse(url)
    signature_string = compose_signature('get', parsed.path,
                                         OrderedDict({
                                            'Date': 'Tue, 08 Nov 2016 15:58:03 GMT'#datetime.utcnow().strftime(GMT_FORMAT)
                                         }))
    print("Signature string:")
    print(signature_string)
    signature = app_secret_coder(secret, signature_string)

    # x-www-form-urlencoded
    headers = {"Content-Type":"application/json",
               "Connection":"Keep-Alive",
               "Authorization":Authorization.format(key=keyId,
                                                    algorithm=algorithm,
                                                    headers=headers or test_headers,
                                                    signature=signature)}

    print(parsed.netloc)
    conn = httplib.HTTPConnection(parsed.netloc)
    print("request headeres:", headers)
    conn.request(method="POST",url=url ,headers=headers)
    response = conn.getresponse()
    print("request finished!")
    print("%s: %s" %(response.reason, response.status))
    print(response.msg)


def test(*args):
    print("begin test... *******\n")
    url = "http://127.0.0.1:8000/api/0.1.4/user/"#raw_input()
    keyId = "SNFPDVAAKXUBHHEI"#raw_input()
    secret = "aca8b32823db20ec542f004e273c12771028b0f4716a957f04c2bcc9cb5c98bd"#raw_input()
    algorithm = "hmac-sha256"
    client(url, keyId, secret, algorithm)
    print("****** end of test")

if __name__ == "__main__":
    import sys
    test(*sys.argv[1:])