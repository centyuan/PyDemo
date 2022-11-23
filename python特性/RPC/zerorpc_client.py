import zerorpc

# zerorpc还提供了心跳检测，默认断线超时30秒，断线后会抛出LostRemote
c = zerorpc.Client()
c.connect('tcp://127.0.0.1:8000')
print(c.hello('RPC'))
