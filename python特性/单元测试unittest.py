# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/27 9:46
import doctest
def multiply(v1,v2):
    """
    >>> multiply(10,8)
    80
    >>> multiply("zhangsan,",5)
    'zhangsan,zhangsan,zhangsan,zhangsan,zhangsan,'
    """
    return v1 * v2


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    """
    测试用例的位置必须放在整个模块文件的开头，或者紧接着对象声明语句的下一行。也就是可以被 __doc__ 这个属性引用到的地方
    """


# unittest
