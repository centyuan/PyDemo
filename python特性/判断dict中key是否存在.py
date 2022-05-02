"""
判断dict中key是否存在
"""
dict_data = {'name':'yuan','age':20,'sex':'man'}
#1.python3 has_key()被__contains__(key)代替
print(dict_data.__contains__('name')) #True
#2.in
print('man' in dict_data) # True
print('a' in dict_data) #False

#3. in keys
print('name' in dict_data.keys())  #True

var = "sex"
if var in dict_data:
    print(dict_data.get(var))


def test_args(*info):
    print(info)
def test_kwargs(**info):
    print(info,info.keys(),info.values())
tuple_data = ("name","age","man")

test_args("name","age","man")
test_args(*tuple_data)
test_kwargs(**dict_data)
test_kwargs(a="a",b="123",c="234")

data = [("192","ru1"),("192","rul2"),("193","rul1"),("194","rul1")]
for i in data:
    if "193" == i[0]:
        print(i[1])
