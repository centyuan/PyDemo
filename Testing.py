# s = "Talk is cheap show me the code"
# print(s.upper())
# print("原始", s)
# print(s.split(" "))
# print("原始", s)
# print(s.isspace())


class A:
    _bar = "aa"
    def __init__(self):
        self.val = 1
        self._bar = "单下划线"
        self.__boo = "双下划线"

    def p(self):
        print(self.val, self._bar, self.__boo)

    def _pp(self):
        print(self.val, self._bar, self.__boo)

    def __ppp(self):
        print(self.val, self._bar, self.__boo)


class B(A):
    def __init__(self):
        self.val = 1


print(A._bar)
a = A()
print(a.val)
a._bar = "aaa"
print(a._bar)
print(a._pp())
# print(a.__boo)
b = B()
print(b.val)
print(b._bar)
# print(b._pp())
print(b.__dir__())