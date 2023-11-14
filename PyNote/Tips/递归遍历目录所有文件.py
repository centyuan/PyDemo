"""
打印目录下所有文件

"""
import os


def print_directory_contents(sPath):
    for child in os.listdir(sPath):
        child_path = os.path.join(sPath, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)
