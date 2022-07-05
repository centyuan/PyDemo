# 1.os.system
import os
result = os.system('ls -al')
# result 执行成功返回0，否则返回执行错误

# 2. os.popen
result = os.popen('cat /etc/passwd')
result.readlines()
# 返回执行结果

# 3.commands
# import commands
# status = commands.getstatus('cat /etc/passwd')
# output = commands.getoutput('cat /etc/passwd')
# status,output = commands.getstatusoutput('cat /etc/passwd')

# 4.subprocess
import subprocess
res = subprocess.Popen('cat /etc/passwd',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
for line in res.stdout.readlines():
    print(line)
res.stdout.close()


