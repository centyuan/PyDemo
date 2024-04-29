---
title: dict创建/合并/自定义排序
categories: 
   - Python从入门到放弃
tags: 
   - Python
---
#### 1.**创建方式**

```python
# 1.
a = dict(one=1,two=2,three=3)
# 2.
a = dict({"one":1,"two":2,"three":3})
# 3.zip
a = dict(zip(["one","two","three"],[1,2,3]))
# 4.列表元组
a = dict([("one",1),("two",2),("three",3)])
# 5.字典推导
a = {k:v for k,v in zip(["one","two","three"],[1,2,3]}
```

#### 2.**合并方式**

```python
d1 = {"usr":"root","pwd":"123456"}
d2 = {"ip":"127.0.0.1","port":"8080"}

# 1.dict.update
d3 = {}
d3.update(d1)
d3.update(d2)

# 2.python3.5后
d3 = {**d1,**d2}

# 3.dict(d1,**d2)
d3 = dict(d1,**d2)

# 4.字典的常规处理
for k,v in d1.items():
    d3[k] = v

for k,v in d2.items():
    d3[k]=v
```

#### 3.排序

```python
dict_date = {6:9,10:5,3:11,8:2,7:6}
# 1.按key升序
d = sorted(dict_data,key=lambda x:x[0])

# 2. 按value降序,reverse=True
d = sorted(dict_data,key=lambda x:x[1],reverse=True)

# 3.operator.itemgetter
rank = [
    {'score': 12, 'time': '2022-08-04'},
    {'score': 23, 'time': '2022-08-01'},
    {'score': 23, 'time': '2022-07-24'},
    {'score': 10, 'time': '2022-07-16'},
    {'score': 12, 'time': '2022-07-16'},

]
from operator import itemgetter
# 按照score排序,
d = sorted(dict_data,key=itemgetter("score")
# 先按照score排序,score相同,在按time排序
d = sorted(dict_data,key=itemgetter("score","time")
# itemgetter排序列表元组,先按下标为1的排序,相同在按2排序
score = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
d = sorted(score ,key=itemgetter(1,2)
     
# 4.cmp_to_key 自定义排序
from functools import cmp_to_key

def custom_sorted(x,y):
    if x["score"]>y["score"]:
        return 1     # 返回1交换位置
    elif x["score"]<y["score"]:
        return -1    # 返回-1不交换位置
    else:
        if x["time"]>y["time"]:
            return 1
        else:
            return -1

to_rank = sorted(rank,key=cmp_to_key(custom_sorted))

```

#### 4.最大值

```python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}
# 1.根据value获取最大值:输出最大值的key
max_ = max(prices,key=lambda k:prices[k])
print(max_)
>>AAPL
# 2.获取最大值key,value
print(max(zip(prices.values(),prices.keys())))
>>(612.78,'AAPL')
```
