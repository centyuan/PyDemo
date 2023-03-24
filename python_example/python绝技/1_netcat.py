import argparse
import socket
import subprocess
import shlex
# shlex模块为基于Uninx shell语法的语言提供了一个简单的lexer
import sys
import textwrap
import threading

# https://zhuanlan.zhihu.com/p/523435178
# 执行命令
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)  # stderr错误句柄
    return output.decode()  # 结果解码


class Netcat():
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置了SO_REUSEADDR的标记为true,操作系统就会在服务器socket被关闭或者服务器进程终止后马上释放该服务器的端口。这样做，可以使调试程序更简单
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)  # 接受小于4096的数据
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('>')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('用户 terminated')
            self.socket.close()
            sys.exit()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)  # 5为最大连接数
        while True:
            client_socket, _ = self.socket.accept()  # 返回connect对象,addr
            client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            client_thread.start()

    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        # 上传文件
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                print(data.decode)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'保存文件{self.args.upload}'
            client_socket.send(message.encode())
        # 执行命令
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'yuan:#>')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'服务被杀 {e}')
                    self.socket.close()
                    sys.exit()


if __name__ == '__main__':
    # 创建解释器
    parser = argparse.ArgumentParser(description='simple netcat 工具',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""Example:
                                     netcat.py -t 192.168.0.108 -p 5555 -l -c # command shell
                                     netcat.py -t 192.168.0.108 -p 5555 -l -u=mytest.txt # upload file
                                     netcat.py -t 192.168.0.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
                                     echo 'ABC' | ./netcat.py -t 192.168.0.108 -p 135 # echo text to server port 135
                                     netcat.py -t 192.168.0.108 -p 5555 # connect to server
                                     """)
                                     )
    # 添加需要的参数 --command(command:参数名称)
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.0.108', help='specified ip')
    parser.add_argument('-u', '--upload', help='upload file')
    # 参数解析
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc = Netcat(args, buffer.encode())
    nc.run()
