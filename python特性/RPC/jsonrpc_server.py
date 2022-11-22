from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

server = SimpleJSONRPCServer(('127.0.0.1',8000))
server.register_function(lambda x,y:x+y,'add')
server.serve_forever()
