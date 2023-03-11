"""
os.system()
os.popen()
commands模块
subprocess模块
"""
import os

# 1.os.system()：创建一个子进程()

result = os.system("ping www.baidu.com")
print(result)

# 2.os.popen(command,mode):通过管道(返回一个文件对象)
file = os.popen("ipconfig")
print(file.read())

# 3.commands
# import commands
# status = commands.getstatus("cat /etc/passwd")
# status,output = commands.getstatusoutput("cat /etc/passwd")

# 4.subprocess.Popen()
import subprocess

result = subprocess.Popen("cat /etc/passwd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# 标准输出
for line in result.stdout.readlines():
    print(line)
result.stdout.close()
