# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/24 22:21

# many-to-many   创建一个经典的多对多关系:一本书可以有多个作者，一个作者可以有多本书
from django.db import models
from time import timezone

# 一：
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    """
    会生成三张表，一个是book（书籍）表包含id,title两个字段，一个是author（作者表）包含id，name，email三个字段，
    这是我们刚刚在models.py文件中创建两个模型，但是有一点需要注意的是在book表里面没有我们创建的authors表，
    而是多了一个book_authors表，在这张表里面又多了两个字段book_id,author_id，
    其实这个第三张表就是用来存放书籍和作者之间映射关系的中间表
    """
# 1:查询
b = Book.objects.get(id=1)
b.authors.all() # 一本书的所有作者
a = Author.objects.get(id=1)
a.book_set.all() #一个作者的所有书
# 2:给多对多的字段添加值
b.authors.add(a)
# #:删除
b.authors.remove(a)

# 二：
"""
可以看出这个blog_book_authors是根据多对多关系自动生成的关系表,
但是如果我们想要搜集关于这个作者发布某一本书籍的时间额外增加一个字段，
或者说与现有的系统集成，这个关系表已经存在了，那对于这样的情形，
Django允许指定一个用于管理多对多关系的中间模型，然后就可以把这些额外的字段添加到这个中间模型中，
具体的方法就是在ManyToMany字段中指定through参数指定作为中介的中间模型，修改上述models.py:

"""

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, through='BookAuthor')  # 增加through参数

class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    pushed_at = models.DateTimeField(default=timezone.now)  # 添加额外字段

    class Meta:
        db_table = "book_author_relationship"  # 使用自定义名称

# 1：如何添加和删除
# 添加作者
author_1 = Author.objects.create(name='gene', email='gene@qq.com')
author_2 = Author.objects.create(name='paul', email='paul@qq.com')

book_1 = Book.objects.create(title='effective book')
# 给多对多添加值也就是添加多对多关系
# m1 = BookAuthor.objects,create(author=paul,book=book1)
# m1.save()
m1 = BookAuthor.objects.create(author=author_1, book=book_1)
# 当我们使用多对多的中间模型之后，
# add(),remove(),create()这些方法都会被禁用，所以在创建这种类型的关系的时候唯一的方法就是通过创建中间模型的实例


