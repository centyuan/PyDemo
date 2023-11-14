import jsonrpclib

server = jsonrpclib.Server('http://127.0.0.1:8000')
print(server.add(1,2))
