# 接受客户端信息并处理，这里只是简单把客户都发来的返回去
async def recv_user_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        print('接收消息:', websocket.pong, recv_text)
        response_text = f'服务器返回:{recv_text}'
        print('返回消息:', response_text)
        await websocket.send(response_text)

recv_user_msg()