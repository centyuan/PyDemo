import hashlib, hmac, json, os, sys, time
from datetime import datetime

# 密钥
secret_id = 'AKID02scCmLtJnDdyHbpvpW4stuoVxGMI1ob'
secret_key = 'e8TRErLKOTYO3lkWFqLhsutlSyJkBX2R'

service = 'OcrGather'
host = ''
# Action: GeneralBasicOCR
# Version: 2018-11-19

# 腾讯sdk:pip install tencentcloud-sdk-python-OcrGather

# pyocr