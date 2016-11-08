import hmac
import hashlib
import base64

msg_tmpl = "{HTTP_METHOD} {URL}/?{DATE}"

def secret_coder(secret, method, url, date):
    print(type(secret))
    msg = msg_tmpl.format(HTTP_METHOD=method, URL=url, DATE=date)
    print(msg)
    digest_obj = hmac.new(secret, msg=msg, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest_obj).decode()

if __name__ == "__main__":
    import sys
    print(secret_coder(*sys.argv[1:]))
