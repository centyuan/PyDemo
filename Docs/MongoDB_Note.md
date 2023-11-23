---
title: MongoDB Note
categories:
   - 数据库
tags:
   - MongoDB
---

#### 概述

>MongoDB是一个基于分布式文件存储的数据库，由C++语言编写，旨在为WEB应用提供可扩展的高性能数据存储解决方案。
>
>是一个介于**关系数据库**和**非关系数据库**之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。
>
>MongoDB的最小存储单位就是文档document对象。文档document对象对应于关系型数据库的行。数据在MongoDB中以BSON（Binary-JSON）文档的格式存储在磁盘上
>
>BSON中，除了基本JSON类型： string，integer，boolean，double，null，array和object，mongo还使用了特殊的数据类型。这些类型包括 date， object id， binary data， regular expression和code
>
>
>**应用场景**
>
>```
>1.High Performance:对数据高并发读写
>2.Huge Storage: 对海量数据的高效率存储和访问的需求
>3.High Scalability && High Availability：对数据库的高可扩展性和高可用性的需求
>```
>
>这些应用场景中，数据操作方面的共同特点是：
>
>数据量大/读写都很频繁/价值较低的数据，对事务性要求不高



#### 集群

>支持三种集群方式:
>
>1.主从备份(Master-salve)
>2.副本集(Replia Set)模式
>3.分片(Sharding)
>
>推荐使用副本集/分片