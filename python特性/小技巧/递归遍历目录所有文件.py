"""
打印目录下所有文件

"""
import os


def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sPath)
        else:
            print(sChildPath)
