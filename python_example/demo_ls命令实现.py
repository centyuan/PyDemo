#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-6 下午8:21

import os
import argparse

parser = argparse.ArgumentParser(prog='ls',description='显示文件夹下的文件')

#指定参数
parser.add_argument('-a','--all',const=True,nargs='?',help='是否显示隐藏的文件')
parser.add_argument('-d','--directory',help='指定显示的目录，默认为当前目录')
parser.add_argument('-r','--recursion',const=True,nargs='?',help='是否递归显示')

#解析参数
args = parser.parse_args()
directory = args.directory


if directory:
    if not os.path.exists(directory):
        #如果指定目录不存在，抛出异常
       raise ValueError("directory does't exist")
    if not os.path.isdir(directory):
        #如果directory 不是一个目录
       raise ValueError("directory is not a directory")

else: #directory 为None
    directory = '.'

class LsCommand():

    def __init__(self, show_all=False, directory='.', recursion=False):
        '''

        :param show_all: 是否显示隐藏文件夹
        :param directory: 指定的文件目录
        :param recursion: 是否递归显示目录下的文件
        '''
        self.show_all = show_all
        self.directory = directory
        self.recursion = os.path.abspath(directory)

    def handle_dir(self, directory, grade=1,placeholder='--'):
        '''
        处理目录
        :param directory: 文件目录
        :param grade: 目录层级
        :param placeholder: 子目录文件前面的占位符
        :return:
        '''
        pass

    def show_file_or_dir(self, file, prefix=''):
        # 如果不显示隐藏文件

        # 打印前缀和文件名
        pass

    def run(self):
        '''
        运行ls命令
        :return:
        '''

        print(os.listdir(self.directory)) #得到dir目录下所有文件，文件夹

        # 遍历self.directory目录先所有文件，文件夹

        pass

ls = LsCommand(bool(args.all), directory, bool(args.recursion))
ls.run()