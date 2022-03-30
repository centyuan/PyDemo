#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-4 上午10:21
"""

命令行火车票查看器
Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h  --help 显示帮助信息
    -g    高铁
    -d    动车
    -t    特快
    -k    快速
    -z    直达
Example:
    tickets 海口 广州 2019-06-06
    tickets -dg 海口 广州 2019-06-06

"""
from docopt import docopt
from station import stations
from prettytable import PrettyTable
import requests
import json

class TrainCollection:
    header = '车次 车站 时间 历时 一等 二等 高级软卧 软卧 硬卧 硬座 无座'.split()
    def __init__(self,available_trains,available_place,options):
        self.available_trains=available_trains
        self.available_place=available_place
        self.options=options
    #@property装饰器(decorator:给函数动态加上功能)把一个方法变成属性调用

    @property
    def trains(self):

        for raw_train in self.available_trains:
            raw_train_list = raw_train.split('|')
            train_no = raw_train_list[3]
            initial = train_no[0].lower()
            duration = raw_train_list[10]
            if not self.options or initial in self.options:
                train = [
                    train_no,  # train number
                    '\n'.join([self.available_place[raw_train_list[6]],  # 始发站
                               self.available_place[raw_train_list[7]]]),  # 终点站
                    '\n'.join([raw_train_list[8],  # 发车时间
                               raw_train_list[9]]),  # 到站时间
                    duration,  # 时长
                    raw_train_list[-6] if raw_train_list[-6] else '--',  # 一等
                    raw_train_list[-7] if raw_train_list[-7] else '--',  # 二等
                    raw_train_list[-15] if raw_train_list[-15] else '--',  # 高级软卧
                    raw_train_list[-8] if raw_train_list[-8] else '--',  # 软卧
                    raw_train_list[-14] if raw_train_list[-14] else '--',  # 硬卧
                    raw_train_list[-11] if raw_train_list[-11] else '--',  # 硬座
                    raw_train_list[-9] if raw_train_list[-9] else '--',  # 无座
                ]
                yield train

    def pretty_print(self):
        #将命令行的查询结果以彩色表格形式打印
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

def cli():
    """command-line interface centyuan"""
    #print(help(cli))可以获取函数注释内容，且注释内容为三双引号 三单引号均可 ,但 # 的不行
    #print(cli.__doc__)
    #print(__doc__)  # 输出文件开头注释内容
    arguments=docopt(__doc__)
    print(arguments)
    print(arguments['<from>'])
    from_station=stations.get(arguments['<from>'])
    to_station=stations.get(arguments['<to>'])
    date=arguments['<date>']
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
        date, from_station, to_station
    )
    html=requests.get(url,verify=False)
    # print(json.loads(str(html.text)))
    # print(type(html))
    # print(dir(html))
    #print(html.json())#.json()将json数据转化为python字典
    available_trains=html.json()['data']['result']
    available_places=html.json()['data']['map']
    print(available_trains)
    #available_trains
    #available_places {'GZQ': '广州', 'VUQ': '海口'}
    options=''.join([key for key,value in arguments.items() if value is True])
    TrainCollection(available_trains,available_places,options).pretty_print()



if __name__=="__main__":
    cli()


