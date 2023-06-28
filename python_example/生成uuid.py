"""
uuid全称:Universally Unique Identifier即通用唯一识别码,无序
由一组32位的16进制数字构成(8位-4位-4位-4位-12位)
由几部分组成(当前的日期和时间,时钟序列,全局的唯一IEEE机器识别号)
使用最普遍的是微软的GUID
"""


import uuid

print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'yuanlin'))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'yuanlin'))
# uuid命名空间
uuid.NAMESPACE_DNS表示标准域名
uuid.NAMESPACE_URL
uuid.NAMESPACE_OID
uuid.NAMESPACE_X500

# 1去掉-
str1 = "3cfc8d7a-f169-11e9-af5b-58a023321f81"
str_2 = "".join(str1.split('-'))
str_2 = "".join(str(uuid.uuid1()).split('-'))
print(str_2[:6])
print(len(''.join(str.split('-'))))
# 2 .hex
uuid_ = uuid.uuid1()
print(uuid_)
print(uuid_.hex)

"""
uuid1()：这个是根据当前的时间戳和MAC地址生成的，最后12个字符408d5c985711就是MAC地址，因为是MAC地址,具有唯一性。但是暴露了MAC地址。

uuid3()：里面的namespace和具体的字符串都是我们指定的，然后呢···应该是通过MD5生成的。

uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的，但这就像中奖似的，几率超小，因为是随机而且使用还方便，所以使用这个的还是比较多的。

uuid5()：这个和uuid3()貌似并没有什么不同，也是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1.

hash算法:MD5/SHA1/SHA256
MD5:128位散列值(16字节),快速,安全不足
SHA1:160位散列值(20字节)---40个十六进制数表示，一般,安全较高
SHA256: 256散列值(32字节)---64个十六进制表示, 较慢,安全高
"""
UUID只读属性:
print("UUID is ", UUID)
print("UUID Type is ",type(UUID))
print('UUID.bytes   :', UUID.bytes)
print('UUID.bytes_le :', UUID.bytes_le)
print('UUID.hex     :', UUID.hex)
print('UUID.int     :', UUID.int)
print('UUID.urn     :', UUID.urn)
print('UUID.variant :', UUID.variant)
print('UUID.version :', UUID.version)
print('UUID.fields  :', UUID.fields)
print("Prining each field seperately")
print('UUID.time_low            : ', UUID.time_low)
print('UUID.time_mid            : ', UUID.time_mid)
print('UUID.time_hi_version     : ', UUID.time_hi_version)
print('UUID.clock_seq_hi_variant: ', UUID.clock_seq_hi_variant)
print('UUID.clock_seq_low       : ', UUID.clock_seq_low)
print('UUID.node                : ', UUID.node)
print('UUID.time                : ', UUID.time)
print('UUID.clock_seq           : ', UUID.clock_seq)
print('UUID.SafeUUID           : ', UUID.is_safe)
