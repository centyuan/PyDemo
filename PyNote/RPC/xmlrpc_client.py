from xmlrpc.client import ServerProxy


# 初始化服务器
server = ServerProxy('http://127.0.0.1:8000')
print(server.add(1, 2))
# print(server.add1(1, 2))
print(server.pow(1, 2))
print(server.multiply(1, 2))
# print(server.mul(1,2))
# 列出所有函数
print(server.system.listMethods())