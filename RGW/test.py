import sys, os, base64, datetime, hashlib, hmac, urllib
import requests # pip install requests
def admin_api(*args):
    access_key = "nguyenhung-accesskey"
    secret_key = b'nguyenhung-secretkey'
    if access_key is None or secret_key is None:
        print('No access key is available.')
        sys.exit()
    
    unixtime = datetime.datetime.utcfromtimestamp(0)
    current_time = datetime.datetime.utcnow()
    five_sec_next = current_time + datetime.timedelta(seconds=30)
    date_second = str(round((five_sec_next - unixtime).total_seconds()))
    print(date_second)
    HTTP_Verb = args[0]
    Content_MD5 = ''
    Content_Length = ''
    CanonicalizedAmzHeaders = ''

    CanonicalizedResource = args[1]

    StringToSign = HTTP_Verb + '\n' + Content_MD5 + '\n' + Content_Length + '\n' + date_second + '\n' + CanonicalizedAmzHeaders  + CanonicalizedResource

    # Sign the string_to_sign using the signing_key
    signature = base64.b64encode(hmac.new(secret_key, (StringToSign).encode('utf-8'), hashlib.sha1).digest())
    signature_encode = urllib.parse.quote(signature)

    url = f"http://ceph-gateway:7480{CanonicalizedResource}?AWSAccessKeyId={access_key}&Expires={date_second}&Signature={signature_encode}"
    print(url)

    headers = {  'Expires':date_second }
    r = requests.get(url, headers=headers)
    print("----- RESPONSE -------")
    print(r.text)
    print(r.status_code)
    print(r.headers)
 
admin_api("GET" ,"/hunghung", "")
                                 
                                 