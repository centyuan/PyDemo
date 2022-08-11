import paramiko

# https://developer.51cto.com/article/604700.html
# 1.paramiko 远程密码连接
client = paramiko.SSHClient()  # 创建一个ssh对象
# 如果之前没有，连接过的ip，会出现选择yes或者no的操作，
##自动选择yes
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
