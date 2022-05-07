import hashlib

da = "望太微兮穆穆"
# 1.
print(hashlib.md5(da.encode('utf8')).hexdigest())
print(hashlib.sha1(da.encode('utf8')).hexdigest())
print(hashlib.sha224(da.encode('utf8')).hexdigest())
print(hashlib.sha256(da.encode('utf8')).hexdigest())
print(hashlib.sha384(da.encode('utf8')).hexdigest())
print(hashlib.sha512(da.encode('utf8')).hexdigest())
print(hashlib.md5(da.encode()))

# 2.
m = hashlib.md5()
m.update(da.encode('utf-8'))
print(m.hexdigest())