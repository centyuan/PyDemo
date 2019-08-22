#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-8 下午3:42



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
from lottery.models import ContractBill
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
from lottery.models import TreePaths
from lottery.models import MemberSpeciesV2Report
bill_id=28350
bill = lottery.models.ContractBill.objects.get(id=bill_id)
#data = lottery.models.ContractBill.calculate_bill(bill)
amount_ = Decimal('12008.188')
if bill.contract.interval == 15 and ContractBill.objects.filter(contract__party_b=bill.contract.party_b, type='dividend').count() % 2 == 0:
    # 周期分红第二期分红结算需要注意上一期有没有盈利
    # last_bill = ContractBill.objects.filter(
    #      end_time__lt=bill.start_time
    #  ).order_by('-start_time').first()

    last_bill=ContractBill.objects.filter(contract__party_b=bill.contract.party_b,type='dividend').order_by('-end_time')[1]
    if last_bill:
        team_b_ = TreePaths.get_descendant(
            ancestor=bill.contract.party_b.id, include_self=True
        ).filter(virtual=False)
        qs_ = MemberSpeciesV2Report.objects.filter(
            member__in=team_b_,
            create_time__gte=last_bill.start_time,
            create_time__lte=last_bill.end_time,
        )
        dat_ = MemberSpeciesV2Report.get_statistics_data(qs_)
        print('---5---')
        if dat_['profit'] > Decimal('0'):
            amount_ += dat_['profit']
            print(dat_['profit'])
            print('---6---')
