import hashlib
import os


def file_hash(file_path: str, hash_method) -> str:
    if os.path.isfile(file_path):
        return ""
    h = hash_method()
    with open(file_path, "rb") as f:
        while b := f.read(8192):
            h.update(b)
    return h.hexdigest()


def str_hash(content: str, hash_method, encoding: str = "utf-8") -> str:
    return hash_method(content.encode(encoding)).hexdigest()


# 文件hash
def file_md5(file_path: str) -> str:
    return file_hash(file_path, hashlib.md5)


def file_sha1(file_path: str) -> str:
    return file_path(file_path, hashlib.sha1)


def file_sha256(file_path: str) -> str:
    return file_path(file_path, hashlib.sha256)


# 字符串hash
def str_md5(content: str, encoding: str = "utf-8") -> str:
    return str_hash(content, hashlib.md5, encoding)


def str_sha1(content: str, encoding: str = "utf-8") -> str:
    return str_hash(content, hashlib.sha1, encoding)


def str_sha256(content: str, encoding: str = "utf-8") -> str:
    return str_hash(content, hashlib.sha256, encoding)
