import websockets
import asyncio

websocket_users = set()


# 检测客户端权限，用户名密码正确退出循环
async def check_user_permit(websocket):
    print("new websocket_users:", websocket)
    websocket_users.add(websocket)
    print("websocket_users list:", websocket_users)
    while True:
        recv_str = await websocket.recv()
        cred_dict = recv_str.split(":")
        if cred_dict[0] == 'admin' and cred_dict[1] == '123456':
            response_str = "Congratulation, successfully connected to the server "
            await websocket.send(response_str)
            print('password is ok')
            return True
        else:
            response_str = "Sorry,please input the username or password"
            print('password is wrong')
            await websocket.send(response_str)


# 接受客户端信息并处理，这里只是简单把客户都发来的返回去
async def recv_user_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        print('接收消息:', websocket.pong, recv_text)
        response_text = f'服务器返回:{recv_text}'
        print('返回消息:', response_text)
        await websocket.send(response_text)


# 主函数
async def run(websocket, path):
    while True:
        try:
            await check_user_permit(websocket)
            await recv_user_msg(websocket)
        except websockets.ConnectionClosed:
            print("连接断开",path)
            print("旧的websocket_users:",websocket_users)
            websocket_users.remove(websocket)
            print("新的websocket_users:",websocket_users)
            break
        except websockets.InvalidState:
            print("无效状态")
            break
        except Exception as e:
            print("异常:",e)
websocket_obj = websockets.serve(run, "127.0.0.1", 8181)
if __name__ == '__main__':
    print("127.0.0.1:8181 websocket...")
    asyncio.get_event_loop().run_until_complete(websocket_obj)
    asyncio.get_event_loop().run_forever()