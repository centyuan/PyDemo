import zerorpc

c = zerorpc.Client()
c.connect('tcp://0.0.0.0:8000')
print(c.hello('RPC'))