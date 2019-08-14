
import sys, os, base64, datetime, hashlib, hmac
import requests # pip install requests
def admin_api(*args):
    access_key = "nguyenhung-accesskey"
    secret_key = b'nguyenhung-secretkey'
    if access_key is None or secret_key is None:
        print('No access key is available.')
        sys.exit()

    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope
    date = t.strftime('%a, %d %B %Y %H:%M:%S +0000')


    HTTP_Verb = args[0]
    Content_MD5 = ''
    Content_Length = ''
    CanonicalizedAmzHeaders = ''

    CanonicalizedResource = args[1]

    StringToSign = HTTP_Verb + '\n' + Content_MD5 + '\n' + Content_Length + '\n' + date + '\n' + CanonicalizedAmzHeaders  + CanonicalizedResource

    # Sign the string_to_sign using the signing_key
    signature = base64.b64encode(hmac.new(secret_key, (StringToSign).encode('utf-8'), hashlib.sha1).digest())

    authorization_header = f"AWS {access_key}:"+signature.decode('utf-8')+""

    print(authorization_header)
    headers = {  'Date':date,'Authorization':authorization_header}
    url = f"http://ceph-gateway:7480{CanonicalizedResource}{args[2]}"
    print(url)


    r = requests.get(url , verify='/etc/ssl/certs/radosgw-selfsigned.pem' , headers=headers)
    print("----- RESPONSE -------")
    print(r.text)
    print(r.status_code)

admin_api("GET" ,"/hunghung", "")