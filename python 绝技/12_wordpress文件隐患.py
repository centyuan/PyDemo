import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERED = [".jpg",".gif",".png",".css"]
TARGET = "http://124.223.4.212/"
THREADS = 10

answer = queue.Queue()
web_paths = queue.Queue()

def gather_paths():
    for root,_,files in os.walk("."):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root,fname)
            if path.startswith("."):
                path = path[1:]
            print(path)
            web_paths.put(path)

@contextlib.contextmanager
def chdir(path):
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f"{TARGET}{path}"
        time.sleep(2)
        r = requests.get(url)
        if r.status_code == 200:
            answer.put(url)
            sys.stdout.write("+")
        else:
            sys.stdout.write("x")
        sys.stdout.flush()

def run():
    mythreads = list()
    for i in range(THREADS):
        print(f"Spawning thread {i}")
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()

    for thread in mythreads:
        thread.join()

if __name__ == "__main__":
    with chdir("/Users/ailx10/py3hack/chapter5/wordpress"):
        gather_paths()
    input("Press return to continue.")
    run()
    with open("myanswer.txt","w") as f:
        while not answer.empty():
            f.write(f"{answer.get()}\n")
        print("done.")

# https://www.zhihu.com/column/linuxbiji