

**面试题**

>Go面试复习指南: https://xmcy0011.github.io/interview-golang/
>
>Go常见面试题: https://zhuanlan.zhihu.com/p/471490292
>
>面试题: http://mian.topgoer.com/
>
>go语言中文文档: https://www.topgoer.com/
>
>go语言设计与实现: https://draveness.me/golang/docs/
>
>面向信仰编程: https://draveness.me/
>
>为什么这么设计: https://draveness.me/whys-the-design/
>
>

##### channel死锁场景

>1.没有缓冲区的时候,单协程内通道写早于读
>
>2.没有数据的时候进行读,(可以使用select来规避)
>
>3.chan1和chan2循环依赖
>
>4.有缓冲区,收发在同一协程,但是缓冲区已满
>
>5.有缓冲区,缓冲区没数据，继续从channel取数据

##### 读写channel哪个先关

>负责写chan的goroutine先关闭
>
>因为关闭chan后,写会panic，读不会(返回通道类型的零值)



