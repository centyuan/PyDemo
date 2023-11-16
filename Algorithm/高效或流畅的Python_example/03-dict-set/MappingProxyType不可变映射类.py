
"""
1.types 模块中引入了一个封装类名叫MappingProxyType。
2.如果给这个类一个映射，它会返回一个只读的映射视图。但是个只读视图，
3.虽然只读但它是动态的。这意味着如果对原映射做出了改动，我们通过这个视图可以观察到，
4.但是无法通过这个视图对原映射做出修改。

"""
from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy) #{1: 'A'} # d_proxy 是个只读视图,不能做修改,但是原映射(即d)修改了，d_proxy也会改变
