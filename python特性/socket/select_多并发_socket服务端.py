import select
import socket
import queue

server = socket.socket()
host_port = ('127.0.0.1',8888)
print(f'server on {host_port}')
server.bind(host_port)
server.listen()
# 不阻塞
server.setblocking(False)
# 返回客户端数据
msg_queue = {}
# 内核检测连接
inputs = [server]
# 客户端连接对象
outputs = []

while 1:
    print('waiting for next connect')
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    for r in readable:
        # 处理活跃的连接，每个r是一个socket连接对象
        if r is server:
            conn,address = server.accept()
            print('arrived a new connect',address)
            conn.setblocking(False)
            # 实现这个客户端发送数据server端能知道,需要让select在监测这个conn
            inputs.append(conn)
            msg_queue[conn] = queue.Queue()
        # r不是server代表是一个与客户端建立的文件描述符
        else:
            data = r.recv(1024)
            if data:
                print('received data from [%s]'%r.getpeername()[0],data)
                msg_queue[r].put(data)
                if r not in outputs:
                    outputs.append(r)
            # 收不到data代表客户端已经断开
            else:
                print('client is disconnect',r)
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                del msg_queue[r]
    # 处理要返回给客户端的连接列表
    for w in writeable:
        try:
            next_msg = msg_queue[w].get_nowait()
        except queue.Empty:
            print("client [%s]" % w.getpeername()[0], "queue is empty...")
            # 确保下次循环时writeable不返回已经处理完的连接
            outputs.remove(w)
        else:
            print('sending message to [%s]'%w.getpeername()[0],next_msg)
            # 放回客户端原数据
            w.send(next_msg)

    # 处理异常连接
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_queue[e]
