#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-22 下午3:11

#实现命令行参数传递
import argparse

parser = argparse.ArgumentParser()
parser.description='描述信息' #创建描述信息
parser.add_argument('first') #添加默认参数
parser.add_argument('second')
parser.add_argument("--optional", help="可选参数",type=int) #可选参数可以不输入，且不会报错
parser.add_argument('-o','--op')
args = parser.parse_args()
print(args.first,args.second)
if args.optional:
    print(args.optional,args.op)

#python argparse_test.py to be --optional 5 -o g