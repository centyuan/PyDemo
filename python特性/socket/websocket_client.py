import asyncio
import websockets
from websockets import  ConnectionClosed


# 发送消息
async def clientsend(websocket):
    while True:
        input_text = input("输入消息:")
        if input_text == 'exit':
            print("退出并断开连接")
            await websocket.close(reason='exit')
            return False
        await websocket.send(input_text)
        recv_text = await  websocket.recv()
        print(f"接受消息:{recv_text}")
# 定时任务
async def ping(websockt):
    while True:
        try:
            await websockt.send('ping')
            await asyncio.sleep(10)
        except:
            break
# 建立websocket连接
async def clientRun():
    while True:
        try:
            async with websockets.connect("ws://" + "127.0.0.1:8181") as websocket:
                while True:
                    try:
                        input_text = input("输入消息:")
                        if input_text == 'exit':
                            print("退出并断开连接")
                            await websocket.close(reason='exit')
                            return False
                        await websocket.send(input_text)
                        recv_text = await  websocket.recv()
                        print(f"接受消息:{recv_text}")
                    except ConnectionClosed as e:
                        # 保证 ws 连接一直处于接收状态（长连接）
                        print("接收报出异常",e.code) # 1000 正常关闭码和 1006 服务端内部错误异常关闭码两种
                        if e.code ==1006:
                            print('退出循环,延时2秒后，websockets.connect重新建立连接') # 两个while实现了重连机制
                            await asyncio.sleep(2)
                            break
        except ConnectionRefusedError as e:
            # 服务端拒绝连接时
            print("ConnectionRefusedError",e)
            global count
            # 重试十次
            if count == 10:
                return
            count += 1
            await asyncio.sleep(2)

if __name__ == '__main__':
    print("客户端开始")
    asyncio.get_event_loop().run_until_complete(clientRun())
