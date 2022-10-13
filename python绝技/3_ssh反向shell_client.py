import subprocess
import shlex

import paramiko


def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()  # 1.创建一个ssh对象
    # 解决问题:如果之前没有，连接过的ip，会出现选择yes或者no的操作，
    # 自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024).decode())
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd = command.decode()
                if cmd == 'exit':
                    client.close()
                    break
                # 执行命令
                # shlex 使用类似shell的语法分割字符串
                cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)
                # 返回
                ssh_session.send(cmd_output or 'okay')
            except Exception as e:
                ssh_session.send(str(e))
                client.close()


if __name__ == '__main__':
    import getpass

    # user = getpass.getuser()
    # # 提示用户输入密码而不回显
    # password = getpass.getpass()
    user = input("user:")
    password = input("password:")
    ip = input("Enter server ip:")
    port = input("Enter port:")
    ssh_command(ip, port, user, password, "clientConnected")
