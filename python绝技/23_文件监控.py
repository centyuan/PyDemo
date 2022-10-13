import os
import tempfile
import threading
import win32con
import win32file

FILE_CREATED = 1
FILE_DELETED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

FILE_LIST_DIRECTORY = 0x0001
PATH = ["C:\Windows\Temp",tempfile.gettempdir()]

def monitor(path_to_watch):
    h_directory = win32file.CreateFile(
        path_to_watch,FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ|
        win32con.FILE_SHARE_WRITE|
        win32con.FILE_SHARE_DELETE,
        None,win32con.OPEN_EXISTING,win32con.FILE_FLAG_BACKUP_SEMANTICS,None)
    while True:
        try:
            results = win32file.ReadDirectoryChangesW(
                h_directory,1024,True,
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SECURITY |
                win32con.FILE_NOTIFY_CHANGE_SIZE,
                None,None)
            for action,file_name in results:
                full_filename = os.path.join(path_to_watch,file_name)
                if action == FILE_CREATED:
                    print(f"[+] create {full_filename}")
                elif action == FILE_DELETED:
                    print(f"[-] delete {full_filename}")
                elif action == FILE_MODIFIED:
                    print(f"[*] modify {full_filename}")
                    try:
                        print("[vvv] dumping contents ...")
                        with open(full_filename) as f:
                            contents = f.read()
                            print(contents)
                        print("[^^^] dump complete")
                    except Exception as e:
                        print("[!!!] dump failed. {e}")
                elif action == FILE_RENAMED_FROM:
                    print(f"[>] renamed to {full_filename}")
                elif action == FILE_RENAMED_TO:
                    print(f"[<] renamed to {full_filename}")
                else:
                    print(f"[?] unknown action on {full_filename}")
        except Exception:
            pass

if __name__ == "__main__":
    for path in PATH:
        monitor_thread = threading.Thread(target=monitor,args=(path,))
        monitor_thread.start()