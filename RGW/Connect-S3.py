
import sys, os, base64, datetime, hashlib, hmac
import requests # pip install requests

# ************* REQUEST VALUES *************
def admin_api(*args):
    method = args[0]
    service = 's3'
    host = '192.168.50.129:7480'
    region = 'us-east-1'
    endpoint = 'http://192.168.50.129:7480/'

    access_key = "48E154A303A22F7B6COH"
    secret_key = b'1gNSoIPuYb6oyX0ZCzHbvBlF24L3pGucM1YwtXUH'
    if access_key is None or secret_key is None:
        print('No access key is available.')
        sys.exit()

    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope
    date = t.strftime('%a, %d %B %Y %H:%M:%S +0000')


    print(date)
    HTTP_Verb = args[0]
    Content_MD5 = ''
    Content_Length = ''
    # CanonicalizedAmzHeaders = 'host:' + host 
    CanonicalizedAmzHeaders = ''

    CanonicalizedResource = '/admin/user'

    StringToSign = HTTP_Verb + '\n' + Content_MD5 + '\n' + Content_Length + '\n' + date + '\n' + CanonicalizedAmzHeaders  + CanonicalizedResource 

    # Sign the string_to_sign using the signing_key
    signature = base64.b64encode(hmac.new(secret_key, (StringToSign).encode('utf-8'), hashlib.sha1).digest())

    authorization_header = f"AWS {access_key}:"+signature.decode('utf-8')+""

    print(authorization_header)
    headers = {  'Date':date,'Authorization':authorization_header}
    url = "http://192.168.50.129:7480/admin/user?format=json"
    # url = "http://192.168.50.129:7480/admin/user"

    # print(url)
    # payload = { 'uid': 'hung9999', 'display-name':'hung123'}
    # r = requests.put(url,  params=payload , headers=headers)
    # print("----- RESPONSE -------")
    # print(r.text)
   
    payload = { 'uid': 'hung9999', 'display-name':'hung123'}
    r = requests.put(url,  params=payload , headers=headers)
    print("----- RESPONSE -------")
    print(r.text)

# admin_api("GET" ,"?uid=admin")
# admin_api("PUT" ,"")


