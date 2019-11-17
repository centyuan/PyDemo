import json
from urllib import parse
from paymentgateway.payments.payment import AlipayMobile, WxMobile
from decimal import Decimal
from django.utils.timezone import now
from restful.exceptions import SCError
import time
import random
import hashlib
import requests


class LeXinPayMixin(object):
    gatewayurl = "http://106.14.156.198:8081/home/HAHA"

    def get_sign(self, str_sign):
        # secret = '5DFEDF03-FD7B-A531-F57B-36A07026C175'
        # secret = self.setting['secret']
        if self.paytype == 'secret':
            secret = self.setting['secret']
        elif self.paytype == 'secret_wx':
            secret = self.setting['secret_wx']

        po_da = sorted(str_sign.items(), key=lambda x: x[0])
        sign_str = ''
        for item in po_da:
            if not item[1]:
                continue
            sign_str += item[0] + str(item[1])
        sign_str = secret + sign_str + secret
        sign = hashlib.md5(sign_str.encode('utf8')).hexdigest().upper()
        return sign

    def get_params(self):
        gatewayurl = "http://106.14.156.198:8081/home/HAHA"
        # group_id = '10000202'  # 机构id
        # group_id = self.setting['group_id'] # 机构id
        if self.paytype == 'secret':
            group_id = self.setting['group_id']
        elif self.paytype == 'secret_wx':
            group_id = self.setting['group_id_wx']

        post_data1 = {  # 业务参数对象
            "group_id": group_id,  # 机构号
            "order_no": self.order.ordernumber,  # 商户订单号
            "total_fee": str(round(self.order.amount)*100),  # 交易金额单位(分)  交易金额范围（1-3000）元
            "notify_url": self.order.upstream_notifyurl,  # 回调地址
            # "sign":'',
        }

        post_data1['sign'] = self.get_sign(post_data1)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(gatewayurl, data=post_data1, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result["code"] == 0:
                payurl = result["code_url"]
                return {
                    'payurl': payurl
                }
            else:
                raise SCError(400, 'error', "%s" % (result["message"]))
        else:
            raise SCError(400, 'error', '支付出错')
    def verify_sign(self):
            data = self.request.GET
            verify_data = {
                "upstream_notify_response": json.dumps(data),
                "upstream_notify_time": now(),
                "upstream_ordernumber": data["order_no"],
                "upstream_status": data["code"],
                "upstream_amount": data["total_fee"],
                "upstream_fee": 0
            }
            self.verify_data = verify_data

    def parse_notify(self):
        if self.verify_data['upstream_status'] == '0' and self.order.status == 0 \
                and str(round(self.order.amount, 2)) == str(round(Decimal(self.verify_data['upstream_amount']), 2)):
            return 'success'
        else:
            return 'fail'



class LeXinPayAlipayMobile(LeXinPayMixin, AlipayMobile):
    gatewayurl = "http://106.14.156.198:8081/home/HAHA"
    paytype = "secret"


class LexinPayWxMobile(LeXinPayMixin, WxMobile):
    gatewayurl = "http://106.14.156.198:8081/home/HAHA"
    paytype = "secret_wx"


class LexinPay():
    alipaymobile = LeXinPayAlipayMobile
    wxmobile = LexinPayWxMobile
