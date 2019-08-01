#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-25 下午11:07

OPERATIONLOGS_MAP = {
    "success_withdrawal": {
        "remark": "%s 到账 %s 提现订单: %s, 金额: %s",
        "operationname": "确认提现"
    },
    "confirm_withdrawal": {
        "remark": "%s 确认 %s 提现订单: %s, 金额: %s",
        "operationname": "确认提现"
    },
}
print(OPERATIONLOGS_MAP['success_withdrawal']['remark'])

import lottery
queryset=lottery.models.MemberFundLog.objects.all()
yatou=queryset.filter(member='815',in_or_out='1',cause='代理返点',create_time__gte='2019-07-25',create_time__lt='2019-07-26')
money=0
for item in yatou:
    money +=float(item.amount)

from django.db.models import Sum
import lottery
queryset_1=lottery.models.MemberFundLog.objects.all()
yatou1=queryset_1.filter(member='815',cause='代理返点',create_time__gte='2019-07-26',create_time__lt='2019-07-27')
# money=0
# for item in yatou1:
#     money +=float(item.amount)
money1=yatou1.aggregate(Sum('amount'))

from django.db.models import Sum
report=lottery.models.MemberSpeciesV2Report.objects.all()
V2=report.filter(member='815',create_time__gte='2019-07-26',create_time__lt='2019-07-27')
proxy_rebate=0
consumption_rebate=0
rebate=0
sum_rebate=V2.aggregate(rebate=Sum('rebate'),)
for item in V2:
    proxy_rebate +=float(item.proxy_rebate)
    consumption_rebate += float(item.consumption_rebate)
    rebate +=float(item.rebate)
