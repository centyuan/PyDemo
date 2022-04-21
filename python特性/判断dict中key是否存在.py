"""
判断dict中key是否存在
"""
dict_data = {'name':'yuan','age':20,'sex':'man'}
#1.python3 has_key()被__contains__(key)代替
print(dict_data.__contains__('name')) #True
#2.in
print('name' in dict_data) # True
print('a' in dict_data) #False

#3. in keys
print('name' in dict_data.keys())  #True