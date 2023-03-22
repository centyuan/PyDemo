import hashlib, hmac, json, os, sys, time
from datetime import datetime
import base64
ak = 'AKID02scCmLtJnDdyHbpvpW4stuoVxGMI1ob'
sk = 'e8TRErLKOTYO3lkWFqLhsutlSyJkBX2R'


def get_authorization(ak, sk):
    # 密钥参数
    secret_id = ak
    secret_key = sk

    service = "ocr"
    host = "ocr.tencentcloudapi.com"
    endpoint = "https://" + host
    region = "ap-beijing"
    action = "GeneralBasicOCR"
    version = "2018-11-19"
    algorithm = "TC3-HMAC-SHA256"
    timestamp = int(time.time())
    # timestamp = 1668763410
    date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
    print('時間',timestamp,date)

    # ************* 步骤 1：拼接规范请求串 *************
    http_request_method = "POST"
    canonical_uri = "/"
    canonical_querystring = ""
    ct = "application/json; charset=utf-8"
    canonical_headers = "content-type:%s\nhost:%s\n" % (ct, host)
    signed_headers = "content-type;host"
    canonical_request = (http_request_method + "\n" +
                         canonical_uri + "\n" +
                         canonical_querystring + "\n" +
                         canonical_headers + "\n" +
                         signed_headers + "\n")

    # ************* 步骤 2：拼接待签名字符串 *************
    credential_scope = date + "/" + service + "/" + "tc3_request"
    hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
    string_to_sign = (algorithm + "\n" +
                      str(timestamp) + "\n" +
                      credential_scope + "\n" +
                      hashed_canonical_request)

    # ************* 步骤 3：计算签名 *************
    # 计算签名摘要函数
    def sign(key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
    secret_service = sign(secret_date, service)
    secret_signing = sign(secret_service, "tc3_request")
    signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()

    # ************* 步骤 4：拼接 Authorization *************
    authorization = (algorithm + " " +
                     "Credential=" + secret_id + "/" + credential_scope + ", " +
                     "SignedHeaders=" + signed_headers + ", " +
                     "Signature=" + signature)
    print(authorization)
    return authorization


if __name__ == '__main__':
    auth = get_authorization(ak, sk)
    import requests

    headers = {
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Authorization': auth,
        'Host': 'ocr.tencentcloudapi.com',
        'X-TC-Version': '2018-11-19',
        'X-TC-Timestamp': '1668762758',
        'X-TC-Language': 'zh-CN',
        'X-TC-RequestClient': 'APIExplorer',
        'X-TC-Action': 'GeneralAccurateOCR',
        'X-TC-Region': 'ap-beijing',
    }
    img_path = r'../resource/5R86.png'
    with open(img_path, 'rb') as f:
        image_base64 = str(base64.b64encode(f.read()), 'utf-8')
        json_data = {
            'ImageBase64': image_base64}
        response = requests.post('https://ocr.tencentcloudapi.com/', headers=headers, json=json_data)
        print(response.json())
