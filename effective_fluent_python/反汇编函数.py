"""
反汇编函数:
    查看pytho语句的汇编指令

"""
from dis import dis

print(dis("{1}"))
print(dis("set([1])"))

"""
  1           0 LOAD_CONST               0 (1)
              2 BUILD_SET                1
              4 RETURN_VALUE
None
  1           0 LOAD_NAME                0 (set)
              2 LOAD_CONST               0 (1)
              4 BUILD_LIST               1
              6 CALL_FUNCTION            1
              8 RETURN_VALUE


"""