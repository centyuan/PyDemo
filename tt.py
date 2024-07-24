import hashlib

# 原始密码
original_password = "qwe123456"
original_password1 = "2677"

# MD5 哈希
md5_hash = hashlib.md5(original_password.encode()).hexdigest()
md5_hash1 = hashlib.md5(original_password1.encode()).hexdigest()

# SHA-1 哈希
sha1_hash = hashlib.sha1(original_password.encode()).hexdigest()
sha1_hash1 = hashlib.sha1(original_password1.encode()).hexdigest()

print(md5_hash, sha1_hash)
print(md5_hash1, sha1_hash1)
