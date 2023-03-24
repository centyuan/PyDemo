x = 1234
er = bin(1234)  # 0b10011010010
oc = oct(1234)  # 0o2322
he = hex(1234)  # 0x4d2
# 1.输出类型都为str
print(er, type(er), oc, type(oc), he, type(he))
# 0b10011010010 <class 'str'> 0o2322 <class 'str'> 0x4d2 <class 'str'>
# 2.去掉0b 0o 0x
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
# 3.转为十进制
print('二进制', int(er, 2), sep=':')
print('八进制', int(oc, 8), sep=':')
print('十六进制', int(he, 16), sep=':')

# 4.字节转字符串
bytes_obj = 'hello 世界'.encode()
print(type(bytes_obj), bytes_obj)
# 对于非 ASCII 字符，print 输出的是它的字符编码值（十六进制形式）
# b'hello \xe4\xb8\x96\xe7\x95\x8c
# b表示字节bytes(开头b,bytes(),encode())

a = '\xe4\xb8\x96\xe7\x95\x8c'  # utf-8编码
# 将启转换成汉字输出
# 方式1 将str转换成bytes,再decode
new_a = a.encode('raw_unicode_escape')  # b'\xe4\xb8\x96\xe7\x95\x8c'
print(type(new_a), new_a.decode())

# 方式2 加b转为bytes,再str(s,'utf8')
new_a = b'\xe4\xb8\x96\xe7\x95\x8c'
n = str(new_a, 'utf8')
print(type(n), n)

# 5.字节转整数
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
nu = int.from_bytes(data, 'little')
nu_ = int.from_bytes(data, 'big')
print(nu, nu_)
# 整数转为字节字符串
x = 9452284252074728448
da = x.to_bytes(16,'big')
da_ = x.to_bytes(16,'little')

