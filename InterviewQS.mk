### Python
list和tuple区别?

is和==区别?

装饰器是什么?

实例方法,静态方法,类方法区别？

Python是引用传递还是值传递？
参数的传递是赋值传递,或叫对象的引用传递
所有都是对象，新变量和原变量指向相同对象
1、如果对象是可变的，当其改变时，所有指向这个对象的变量都会改变。
2、如果对象不可变，简单的赋值只能改变其中一个变量的值，其余变量则不受影响。

深拷贝和浅拷贝,赋值区别？

可变和不可变对象?
int、float、bool、string、tuple
list、dict、set

ORM有哪些？

返回一个整数的二进制?
bin(3)

检查一个字符串是否仅仅包含数字？
isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象
str = u"this2009";  
print(str.isnumeric())

检查一个字符串是否仅仅包含字母？
str.isalpha()

检查字符串是否只包含数字和字母?
str.isalnum()

remove、del和pop有什么区别?
remove 删除第一个匹配的值。
del按索引删除元素。
pop 按索引删除一个元素并返回该元素。