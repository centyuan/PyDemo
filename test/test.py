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

queryset=lottery.models.MemberFundLog.objects.all()
yatou=queryset.filter(member='815',in_or_out='1',cause='代理返点',create_time__gte='2019-08-02',create_time__lt='2019-08-03')
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


from django.db.models import Sum
from decimal import Decimal
import datetime
import lottery
start='2019-08-01'
end_='2019-08-02'
member='815'
data = []
data1={}
while start < end_:
    #end_ = start + datetime.timedelta(days=1)
    qs = lottery.models.MemberSpeciesV2Report.objects.filter(**{
        'create_time__gte': start,
        'create_time__lt': end_,
        'member': member
    })
    d = lottery.models.MemberSpeciesV2Report.get_statistics_data(qs)
    d['create_time'] = start

    data1 = lottery.models.MemberFundLog.objects.get_fundlog_statistics(
        2,
        filter_params={'member': member, 'create_time__gte': start, 'create_time__lt': end_})['充值']

    #     d['activity'] = lottery.models.ContractBill.objects.filter(
    #         status=2, type='wage', contract__party_b=member,
    #         end_time__gte=(start - datetime.timedelta(days=1)),
    #         end_time__lt=(end_ - datetime.timedelta(days=1))).aggregate(activity=Sum('amount'))['activity'] or Decimal(
    #         '0')
    data.append(d)
    print(d)
    start = end_


#代理佣金
import lottery
queryset=lottery.models.MemberFundLog.objects.all()
yatou1=queryset.filter(member='814',in_or_out='1',create_time__gte='2019-08-02',create_time__lt='2019-08-03')
yatou2=queryset.filter(member='814',in_or_out='0',create_time__gte='2019-08-02',create_time__lt='2019-08-03')
#冻结资金
dongjie=queryset.filter(member='814',cause='资金冻结',create_time__gte='2019-08-02',create_time__lt='2019-08-03')
jiedong=queryset.filter(member='814',cause='资金解冻',create_time__gte='2019-08-02',create_time__lt='2019-08-03')
money_in=0
money_out=0
# for item in yatou1:
#     money_in +=float(item.amount)
# for item in yatou2:
#     money_out +=float(item.amount)
dongjie_num=0
jiedong_num=0
for item in dongjie:
    money_in +=float(item.amount)
    dongjie_num +=1
for item in jiedong:
    money_out +=float(item.amount)
    jiedong_num +=1



#获取用户总的资金明细
import utils
import lottery
from restful.exceptions import SCError
#pk='814'
# pk='13116'
#pk='11111'
pk='804'
queryset = lottery.models.Member.objects.all()
try:
    obj = queryset.get(id=pk)
except:
    raise SCError(400, 'Invalid member', '无效的用户 ID')

start = '2019-08-15'
end = '2019-08-20'
filter_params = {'member_id': pk}
if start:
    start = utils.transform_string_to_datetime(start, time_format='%Y-%m-%d')
    end = utils.transform_string_to_datetime(end, time_format='%Y-%m-%d')
    filter_params.update({
        'create_time__gte': start,
        'create_time__lte': end
    })
data = lottery.models.MemberFundLog.objects.get_fundlog_statistics(
    enterprise=obj.enterprise,
    datetime=None,
    filter_params=filter_params
)



# 每日 2:00 点执行
@shared_task(queue='cron')
def lottery_calculate_contract_bill():
    """
    定时记算昨日的契约分红/工资的账单
    """
    for bill in lottery.models.ContractBill.objects.filter(
            status=0):
        lotterymanage.tasks.async_calculate_contract_amount.apply_async(
            args=(bill.id, )
        )

lottery_calculate_contract_bill

#计算分红
from decimal import Decimal
from lottery.models import Result
from django.utils.timezone import timedelta, now
from celery import shared_task
import lottery.models
import utils
from lotterymanage.species.scheduler import Scheduler
from lotterymanage.species.openresult import OpenResult
from lotterymanage.species.loop import loop
import enterprise.models
from django.db.models import Count, Sum
import random
import json
from lotterymanage.models import perform_create
from django.core.cache import cache
import lottery.api.serializers
from restful.exceptions import SCError
import lottery.api.channel
from tools.platform_data import PlatformReportData
from lotterymanage.models import MoocRequest
import account.models
import datetime
bill_id=28350
bill = lottery.models.ContractBill.objects.get(id=bill_id)
data = lottery.models.ContractBill.calculate_bill(bill)


#提现测试

from hashlib import md5
from requests import post
from decimal import Decimal
from django.http import HttpResponse
from django.db import transaction
from django.core.cache import cache
from django.db.models import Sum, Count
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from lottery.api.payment.serializers import ( RechargeSerializer, WithdrawSerializer, PaymentChannelSerializer,
                                              WithdrawUpdateSerializer, TransferCreateSerializer, TransferSerializer,
                                              WithdrawQuickSerializer )
from lottery.models import ( Recharge, Withdraw, Member, PaymentChannel, MemberFund, Setting, ContractBill,
                             MemberSafequestion, Transfer, TreePaths )
from lottery.api.utils import get_ordernum
from lottery.api.views import LotteryAPIViewMixins
from restful.exceptions import SCError
from django_filters.rest_framework import DjangoFilterBackend
from lottery.api.payment.filters import WithdrawFilter, RechargeFilter
from lottery.authentications import LotteryMemberTokenAuthentication
from lottery.api.utils import get_today_datetime_range
from utils import const, serialize_currency
import json
from lottery.models import RechargeConsumptionRecord
from lottery.models import OtBettingLog
from lottery.models import MemberFundLog

#member = Member.objects.get(account=13574)
member = Member.objects.get(account=7872)

enterprise=2
fund, _ = MemberFund.objects.get_or_create(member=member, currency='CNY')

keys = ('withdraw_server_time', 'withdraw_free_times', 'withdraw_limit_times', 'withdraw_limit_amount',
        'withdraw_fee_desc_formula', 'min_withdraw', 'max_withdraw', 'withdraw_fee', 'withdraw_fee_max',
        'withdraw_must_safequestion')
settings = Setting.objects.get_settings(enterprise=enterprise, keys=keys)

withdrawinfo = Withdraw.objects.filter(member=member, create_time__range=get_today_datetime_range()) \
    .aggregate(today_withdraw_amount=Sum('amount'), today_withdraw_times=Count('*'))

withdraw_amount = member.calculate_withdraw_amount()

if withdraw_amount <= 0:
    withdraw_amount = 0

try:
    title_safequestion = MemberSafequestion.objects.filter(member=member)[:1][0].problem
except:
    title_safequestion = ''

# 提现是否需要安全问题
if int(settings.get("withdraw_must_safequestion")) == 1:
    try:
        safequestion = MemberSafequestion.objects.filter(member=member)[:1][0].problem
    except IndexError:
        raise SCError(400, '', '未设置安全问题')
else:
    safequestion = ""

data = {
    "balance": serialize_currency(fund.balance),  # 账户总余额
    "withdraw_amount": serialize_currency(withdraw_amount),  # 可提现金额
    'consumption_gap': member.calculate_withdraw_consumption(),  # 提现所需消费量
    "withdraw_server_time": settings['withdraw_server_time'],  # 提现服务时间
    "withdraw_free_times": settings['withdraw_free_times'],  # 每日免费次数
    "today_withdraw_amount": 0 if withdrawinfo.get('today_withdraw_amount') is None else withdrawinfo.get(
        'today_withdraw_amount'),  # 今日提现金额
    "today_withdraw_times": withdrawinfo.get('today_withdraw_times'),  # 今日提现次数
    "withdraw_limit_times": settings['withdraw_limit_times'],  # 每日限制次数
    "withdraw_limit_amount": settings['withdraw_limit_amount'],  # 每日限制金额
    "max_withdraw": settings['max_withdraw'],
    "min_withdraw": settings['min_withdraw'],
    "withdraw_fee_max": settings['withdraw_fee_max'],
    "withdraw_fee": settings['withdraw_fee'],
    "withdraw_fee_desc_formula": settings['withdraw_fee_desc_formula'],
    "safequestion": safequestion,
    "title_safequestion": title_safequestion

}

#计算消费量

consumption = Decimal('0')

objs = list(
    RechargeConsumptionRecord.objects.filter(
        member=member, status=0
    ).order_by('ass_log__create_time')
)

below_grade = []
recharge_rate = Setting.objects.get(
    enterprise=member.enterprise,
    key='consumpetion_standard').value
for i in range(len(objs)):
    start_time = objs[i].ass_log.create_time

    try:
        end_time = objs[i + 1].ass_log.create_time

    except IndexError:
        end_time = None
    print('start_time',start_time)
    print('end_time', end_time)
    filter_params = {
        'create_time__gte': start_time,
        'member': member,
    }
    if end_time:
        filter_params['create_time__lt'] = end_time

    # ots的消费
    print(filter_params)
    otsconsumption = OtBettingLog.objects.filter(**filter_params).aggregate(consumption=Sum("betamount"))[
                         "consumption"] or Decimal("0")
    data = MemberFundLog.objects.get_fundlog_statistics(
        member.enterprise, filter_params=filter_params)
    rate = objs[i].rate
    print("otsconsumption",otsconsumption)
    print("data",data)
    print("rate",rate)
    consumption += (rate * objs[i].ass_log.amount - data['消费'] - data['红包赔付'] - otsconsumption - data['普通转出'] * Decimal(
        recharge_rate))
    print("consumption",consumption)
    if consumption < Decimal('0'):
        consumption = Decimal('0')
        obj = objs[i]
        obj.status = 1
        obj.save()
        for r in below_grade:
            r.status = 1
            r.save()
        below_grade = []
    else:
        below_grade.append(objs[i])



#return consumption


#调线
# from rest_framework import serializers
# from im.models import RedEnvelopeDividendDetail
# import utils
# from lottery.api.utils import add_each_other
# from restful.exceptions import SCError

'''
jian168:766
aze8888:781
a666666:5688
 wo928616:5803
  taoge888:5804
  wo080808:6405
   1115184284:6444

一:计算wo928616所有下级,
二:删除aze8888:781 a666666:5688与wo928616所有下级的treepaths
三:再修改jian168和wo928616及其所有下级的treepaths的distance和path

dev01:609
  dev02:610
     dev03:611
 	   dev10:5785
	     ydev10:13358
            ydev11:13359
            ydev12:13360
	   dev05:612
		dev07:663
		dev08:664
'''

# 同一条线,调线(下级往上下)
import lottery

# new_ancestor=766
# descendant=5803
new_ancestor = 610
descendant = 13358

one_ancestor = lottery.models.TreePaths.get_ancestor(descendant, return_id=True)
two_ancestor = lottery.models.TreePaths.get_ancestor(new_ancestor, return_id=True)
jiao = list(set(one_ancestor) & set(two_ancestor))
if jiao:
    issame_line = True
else:
    issame_line = False

#import lottery

# issame_line = True
# up_or_down = True
new_ancestor = 766
descendant = 5803
# if issame_line and up_or_down:
# 获取要修改的用户及其所有下级包括它本身
all_descendant = lottery.models.TreePaths.get_descendant(
    descendant, include_self=True, return_id=True)
# 获取要修改用户的所有上级
all_ancestor = lottery.models.TreePaths.get_ancestor(descendant, return_id=True)
# 获取所修改用户的新上级的所有上级
new_allancestor = lottery.models.TreePaths.get_ancestor(new_ancestor, include_self=True, return_id=True)
# 做差,如果在一条线的话,去掉相同的,留下去掉
left_all_ancestor = list(set(all_ancestor) - set(new_allancestor))
distance = len(left_all_ancestor)
# 修改新上级的所有上级和所有下级的treepaths记录
result = lottery.models.TreePaths.objects.filter(ancestor__in=new_allancestor, descendant__in=all_descendant)
for item in result:
    item.distance = item.distance - 2
    # for value in left_all_ancestor:
    #     item.path.remove(str(value))
    item.save()
# 去掉原来上级和新上级之间的treepaths记录
lottery.models.TreePaths.objects.filter(
    descendant__in=all_descendant,
    ancestor__in=left_all_ancestor).delete()

# 生成契约账单
# 异步生成契约分红 / 工资账单
import lottery
contract_id ='147'
contract = lottery.models.Contract.objects.get(id=contract_id)

# last check
if not contract.can_generate_bill:
    print(False)

contract.generate_bill()

#
for descendant in descendants:
    consumption = lottery.models.MemberFundLog.objects.get_fundlog_statistics(
        enterprise=descendant.enterprise,
        filter_params={'member': descendant, 'create_time__lt': end_time, 'create_time__gte': start_time}
    )

    total_consume=consumption["消费"]+consumption["红包赔付"]
    if total_consume > Decimal("300"):
        effective_player_count = effective_player_count + 1
        
if effective_player_count >=1 and effective_player_count < 2:
   distance = 1
elif effective_player_count >=2 and effective_player_count < 4:
   distance = 2
elif effective_player_count >= 4 and effective_player_count < 8:
   distance = 3
elif effective_player_count >= 8 and effective_player_count < 12:
   distance = 4
elif effective_player_count >= 12:
   distance = 5
else:
   distance = 0
f = {
      "member": member,
      "create_time__lt": end_time,
      "create_time__gte": start_time
  }


if distance > 0:
    f["level__lte"] = distance
    bills = im.models.RedEnvelopeDividendDetail.objects.filter(**f).iterator()
    for bill in bills:
        beneficiary = bill.member
        if not beneficiary.virtual:
            beneficiary.fund_cny.add_balance(bill.amount, '127.0.0.1',
                                             const.MEMBER_FUND_CAUSE_MAP["platform_tax_commission"],
                                             remark=bill.remark,
                                             extra=json.dumps({
                                                 "username": bill.accept_member.nickname,
                                                 "account_id": bill.accept_member.account.pk,
                                                 "distance": bill.level
                                             }),
                                             speciescode=bill.speciescode,
                                             periodnumber=bill.periodnumber,
                                             group_name=bill.group_name
                                             )
            bill.status = 1
            bill.save(update_fields=["status"])




today = utils.today_morning()
yesterday = utils.yesterday_morning()
member_ids = im.models.RedEnvelopeDividendDetail.objects.filter(
    create_time__lt=today,
    create_time__gte=yesterday
).exclude(status=1).distinct('member').values_list('member', flat=True)
for member_id in member_ids:
    _send_hb_commission(member_id, yesterday, today)



bill = lottery.models.ContractBill.objects.get(id=bill_id)
data = lottery.models.ContractBill.calculate_bill(bill)
data.pop('target', None)
today = utils.today_morning()
# 若超过结算时间，则更换状态为待确认
# if bill.end_time <= today:
#    data['status'] = 1

lottery.models.ContractBill.objects.filter(id=bill_id).update(**data)
# 对于金额为 0 和契约工资全部自动发放
if data.get('status') == 1 and bill.is_freeze == 0:
   bill.refresh_from_db()
   if bill.type == 'wage' or bill.amount == Decimal('0'):
       bill.send_welfare()

   elif bill.type == 'dividend' and bill.contract.party_b.is_partner():
       bill.send_welfare()




# 检查工资转账金额
import lottery
from decimal import Decimal
import re
import json
from django.utils.translation import ugettext_lazy as _
from django.db.models import Sum
from rest_framework import serializers
from restful.exceptions import SCError
from lottery.models import RebateLevel, Member, RedRebateLevel, ChessRebateLevel, VideoRebateLevel
import lottery.models
from utils.const import MEMBER_FUND_CAUSE_MAP
from utils import format_nickname, serialize_currency, transform_string_to_datetime
import im.models
import account.models
import logging


# activity_amount = lottery.models.ContractBill.objects.filter(
#     status=2, contract__party_b=self.ancestor, end_time__gte=start_time
# ).aggregate(activity=Sum('amount'))['activity'] or Decimal('0')
#BAY6688
#yatou1994
ancestor = lottery.models.Member.objects.get(account__username="pan1998")
start_time = transform_string_to_datetime("2019-07-01 00:00:00")
new_start = transform_string_to_datetime("2019-07-01 02:10:00")
cause = lottery.models.MemberFundLog.objects.get_fundlog_statistics(
    ancestor.enterprise,
    filter_params={'member': ancestor,
                   'create_time__gte':start_time
                   }
)
rebate = cause["返点"]
commission = cause["税收佣金"]
agency_commission = cause["代理佣金"]
#activity_amount = cause["活动"] + cause["工资转出"] - cause["工资转入"] + cause["活动撤回"]

data = lottery.models.MemberFundLog.objects.get_fundlog_statistics(
                ancestor.enterprise,
                filter_params={'member': ancestor,
                               'create_time__gt':new_start
                               }
            )
wage = data["活动"] + data["工资转出"] - data["工资转入"]
dividend = data["分红"]
activity_amount = wage + dividend
old_activity = cause["活动"] + cause["工资转出"] - cause["工资转入"] +cause["分红"]
total_transfer_amount = lottery.models.Transfer.objects.filter(
    member=ancestor, type=1, create_time__gte=start_time
).exclude(
    status=2
).aggregate(activity=Sum('amount'))['activity'] or Decimal('0')

total_receive_amount = lottery.models.Transfer.objects.filter(
    recipient=ancestor, type=1, create_time__gte=start_time
).exclude(
    status=2
).aggregate(activity=Sum('amount'))['activity'] or Decimal('0')

test_transfer_amount = lottery.models.Transfer.objects.filter(
    member=ancestor, create_time__gte=start_time
).aggregate(activity=Sum('amount'))['activity'] or Decimal('0')
if validated_data['amount'] + total_transfer_amount > activity_amount + rebate + commission + total_receive_amount:
    raise SCError(
        400,
        'Invalid activity transfer amount.',
        '工资转账金额超过最大可转账金额数目')

import lottery
from django.utils.timezone import now,datetime,timedelta
from django.db import transaction

with transaction.atomic():
    time = datetime.strptime("2019-07-04 00:00:00", "%Y-%m-%d %H:%M:%S")
    next_start = datetime.strptime("2018-08-25 00:00:00","%Y-%m-%d %H:%M:%S")

    all_contract = lottery.models.Contract.objects.filter(interval=1,next_start_time=time)
    lottery.models.Contract.objects.filter(interval=1, next_start_time=time).update(next_start_time=next_start)

import lottery
from django.utils.timezone import now,datetime,timedelta
from django.db import transaction
with transaction.atomic():
    #修改contract
    # 删除时间错误的ContractBill,开始时间(2019-08-01 00:00:00+08到2019-08-31 23:59:59.999999+08)
start = datetime.strptime("2019-08-01 00:00:00", "%Y-%m-%d %H:%M:%S")
#end = time = datetime.strptime("2019-08-31 23:59:59.999999", "%Y-%m-%d %H:%M:%S")
qs = lottery.models.ContractBill.objects.filter(type="share", start_time=start)
    qs.delete()

next_start = datetime.strptime("2019-09-01 00:00:00", "%Y-%m-%d %H:%M:%S")
new_start = datetime.strptime("2018-09-16 00:00:00","%Y-%m-%d %H:%M:%S")
qs = lottery.models.Contract.objects.filter(type="share",next_start_time=next_start)
lottery.models.Contract.objects.filter(type="share",next_start_time=next_start).update(next_start_time=new_start)
#修改contractbill start_time为2019-07-03 00:00:00的时间
with transaction.atomic():
    #获取今天的contractbill,并修改时间
    today_time = datetime.strptime("2019-07-03 00:00:00", "%Y-%m-%d %H:%M:%S")
    all_contractbill = lottery.models.ContractBill.objects.filter(start_time=today_time)
    start = datetime.strptime("2019-08-24 00:00:00", "%Y-%m-%d %H:%M:%S")
    end =datetime.strptime("2019-08-25 00:00:00", "%Y-%m-%d %H:%M:%S")-timedelta(microseconds=1)
all_contractbill.update(start_time=start,end_time=end)


#筛选
from django.db.models import Sum
import  lottery
one = datetime.strptime("2019-07-01 00:00:00", "%Y-%m-%d %H:%M:%S")
two = datetime.strptime("2019-07-02 00:00:00", "%Y-%m-%d %H:%M:%S")
one_amount = lottery.models.ContractBill.objects.filter(start_time=one).aggregate(amount=Sum('amount'))
total_amount = lottery.models.ContractBill.objects.filter(start_time=two).aggregate(amount=Sum('amount'))
one_contract = lottery.models.ContractBill.objects.filter(start_time=one,amount__gt=1).select_related("contract")
two_contract = lottery.models.ContractBill.objects.filter(start_time=two,amount__gt=1).select_related("contract")


#计算contractbill

#2019-07-02 00:00:00+08	2019-07-02 23:59:59.999999+08  48922
#2019-08-23 00:00:00+08	2019-08-23 23:59:59.999999+08
import  lottery
from decimal import Decimal
from django.utils.timezone import now,datetime,timedelta

bill = lottery.models.ContractBill.objects.get(id='47941') #
contract = bill.contract
#start_time1=datetime.strptime("2019-08-23 00:00:00", "%Y-%m-%d %H:%M:%S")
#end_time1 =datetime.strptime("2019-08-24 00:00:00", "%Y-%m-%d %H:%M:%S")-timedelta(microseconds=1)

start_time2=datetime.strptime("2019-08-22 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time2=datetime.strptime("2019-08-23 00:00:00", "%Y-%m-%d %H:%M:%S")-timedelta(microseconds=1)

team_b = lottery.models.TreePaths.get_descendant(
    ancestor=contract.party_b.id, include_self=True).filter(virtual=False)
qs = lottery.models.MemberSpeciesV2Report.objects.filter(
    enterprise=contract.party_b.enterprise,
    member__in=team_b,
    create_time__gte=start_time2, create_time__lt=end_time2
)
sum_data =lottery.models.MemberSpeciesV2Report.get_statistics_data(qs)
data = {
    'profit': sum_data['profit'],
    'consume': sum_data['consume'],
}
data['active_num'] = bill.calculate_active_num(team_b)
data['team'] = bill.calculate_team()
rule, rebate = bill.get_bill_rule(data, cmp_team=False)
data['rebate'] = rule['rebate']
data['amount'] = bill.calculate_amount(data, rebate)
data['target'] = {
    'status': 0 if not rebate else 1,
    'rule': rule,
}



#计算账单工资
import lottery
from decimal import Decimal

bill = lottery.models.ContractBill.objects.get(id='50046')
contract = bill.contract
team_b = lottery.models.TreePaths.get_descendant(
    ancestor=contract.party_b.id, include_self=True).filter(virtual=False)
qs = lottery.models.MemberSpeciesV2Report.objects.filter(
    enterprise=contract.party_b.enterprise,
    member__in=team_b,
    create_time__gte=bill.start_time, create_time__lt=bill.end_time
)
sum_data = lottery.models.MemberSpeciesV2Report.get_statistics_data(qs)
data = {
    'profit': sum_data['profit'],
    'consume': sum_data['consume'],
}
data['active_num'] = bill.calculate_active_num(team_b)
data['team'] = bill.calculate_team()
rule, rebate = bill.get_bill_rule(data, cmp_team=False)
data['rebate'] = rule['rebate']
data['amount'] = bill.calculate_amount(data, rebate)
data['target'] = {
    'status': 0 if not rebate else 1,
    'rule': rule,
}
return data


#计算工资

#start_time1=datetime.strptime("2019-08-23 00:00:00", "%Y-%m-%d %H:%M:%S")
#end_time1 =datetime.strptime("2019-08-24 00:00:00", "%Y-%m-%d %H:%M:%S")-timedelta(microseconds=1)

start_time2=datetime.strptime("2019-08-24 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time2=datetime.strptime("2019-08-25 00:00:00", "%Y-%m-%d %H:%M:%S")-timedelta(microseconds=1)


if self.type == 'wage':
    # 工资的计算使用点位差来计算
amount = Decimal('0')
for descendant in lottery.models.TreePaths.get_descendant(
        contract.party_b.id, distance=1):
    team_b = lottery.models.TreePaths.get_descendant(
        descendant.id, include_self=True)

    qs = lottery.models.MemberSpeciesV2Report.objects.filter(
        member__in=team_b,
        create_time__gte=bill.start_time,
        create_time__lt=bill.end_time
    )
    data = lottery.models.MemberSpeciesV2Report.get_statistics_data(qs)
    consume = data['consume']
    consume = Decimal(consume)
    print("consume<--->", consume)
    if consume < Decimal(0):
        consume = Decimal(0)

    rebate_gap = rebate
    print("rebate_gap<--->", rebate_gap)
    descendant_contract = lottery.models.Contract.objects.filter(
        party_a=contract.party_b,
        party_b=descendant, status=1, type='wage').first()
    print("contract.party_b<--->descendant", contract.party_b, descendant)
    print("descendant_contract<--->", descendant_contract)
    if descendant_contract:
        bill = lottery.models.ContractBill.objects.filter(
            contract=descendant_contract, type='wage').last()
        if bill:
            data['active_num'] = bill.calculate_active_num(team_b)
            _, wage_rebate = bill.get_bill_rule(
                data)
        else:
            wage_rebate = Decimal('0')
        print("wage_rebate<--->",wage_rebate)
        rebate_gap = Decimal(str(rebate)) - Decimal(wage_rebate)
        print("rebate_gap<--->", rebate_gap)
    print("befor amount<--->",amount)
    amount += consume * Decimal(rebate_gap) * Decimal('0.01')
    print("after amount<--->", amount)

if amount == Decimal('0'):
    print(data['consume'])
    amount = data['consume'] * Decimal(str(rebate)) * Decimal('0.01')
    print(amount)

#生成十五天周期性分红
#contract的next_start_time 2019-08-31 00:00:00+08

import  lottery
from decimal import Decimal
from django.utils.timezone import now,datetime,timedelta
from django.db import transaction


with transaction.atomic():
    next_start = datetime.strptime("2019-08-31 00:00:00", "%Y-%m-%d %H:%M:%S")
    #next_start = datetime.strptime("2018-08-28 00:00:00", "%Y-%m-%d %H:%M:%S")
    start_time = next_start - timedelta(days=15)
    end_time = next_start - timedelta(microseconds=1)
    #qs = lottery.models.Contract.objects.filter(type='dividend',interval='15', next_start_time=next_start)
    for contract in lottery.models.Contract.objects.filter(type="dividend",interval='15',next_start_time=next_start):
        contract = lottery.models.Contract.objects.get(id=contract.id)
        data = {
            'contract': contract,
            'rule': contract.bill_rules(),
            'rebate': contract.basic_rule.rebate,
            'type': contract.type,
            'start_time': start_time,
            'end_time': end_time,
        }
        created = lottery.models.ContractBill.objects.create(**data)

#生成提现订单
# def perform_create(self, serializer):

# member = self.request.user.lottery_member_account
# agent_withdrawal_disable = TreePaths.get_ancestor(
#     member, include_self=True
# ).filter(agent_withdrawal_disable=1).exists()


# if agent_withdrawal_disable:
#     raise SCError(400, 'Authentication faild', '代理线路已被禁用提现')

import lottery
from lottery.api.utils import get_ordernum
from decimal import Decimal
from django.utils.timezone import now,datetime,timedelta
from django.db import transaction
from django.db.models import Sum
with transaction.atomic():
amount = '1000'
member = lottery.models.Member.objects.get(id='14153')

#serializer = WithdrawSerializer()
abc = lottery.models.MemberBank.objects.get(member=member)

ordernum = get_ordernum('WD')
create_time= now()
account = abc.account
account_name = abc.account_name
account_bank =abc.account_bank

    lottery.models.Withdraw.objects.get_or_create(name="WZT", age=23)(member=member, ordernum=ordernum, enterprise=member.enterprise, create_time=create_time,account=account,account_name=account_name,account_bank=account_bank
                    )
    # 提现订单创建成功后，扣减账户余额
membercny = member.fund_cny
membercny.less_balance(
    amount=amount,
    ip='127.0.0.1',
    cause=const.MEMBER_FUND_CAUSE_MAP["withdraw"],
    ass_withdraw=serializer.instance,
    type="common"
)

#提现，消费之ag
from django.db.models import Sum
from decimal import  Decimal
from utils import transform_string_to_datetime
import lottery
from django.utils.timezone import datetime,timedelta

member = lottery.models.Member.objects.get(id='14210')

objs = list(
    lottery.models.RechargeConsumptionRecord.objects.filter(
        member=member, status=0
    ).order_by('ass_log__create_time')
)
i=0
start_time = objs[i].ass_log.create_time
try:
    end_time = objs[i + 1].ass_log.create_time
except IndexError:
    end_time = None

filter_params = {
    'create_time__gte': start_time,
    'member': member,
}
f = {
    'create_time__gte': start_time - timedelta(hours=12),
    'member': member,
}
if end_time:
    filter_params['create_time__lt'] = end_time
    f['create_time__lt'] = end_time - timedelta(hours=12)
print(f, filter_params)
# ots的消费
otsconsumption1 = lottery.models.OtBettingLog.objects.filter(**filter_params).aggregate(consumption=Sum("betamount"))[
                      "consumption"] or Decimal("0")
otsconsumption = lottery.models.OtBettingLog.objects.filter(**f).aggregate(consumption=Sum("betamount"))["consumption"] or Decimal("0")
print(otsconsumption, otsconsumption1)