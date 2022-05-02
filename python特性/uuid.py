import uuid

l = "9042ebe1302a46839f6deec81de2a4ea"
m = "bda4ceec2917426cb9ee20b3bcb20653"
print(len(l),len(m))
print(len(str(uuid.uuid1())))
print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS, "test"))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS, "test"))
s = ''.join(str(uuid.uuid4()).split('-'))
print(s)