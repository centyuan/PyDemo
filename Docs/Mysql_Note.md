---
1ititle: mysql常用操作命令和性能优化
categories: 
   - 数据库
tags: 
   - mysql
---
mysql常用操作命令

mysql:单进程多线程模型,一个SQL语句无法利用多个cpu core
>mysql8加强安全性,头次登录,会生成一个临时随机密码,使用密码进行root用户登录,且root不支持远程登录
>查看临时密码:  grep 'temporary password' /var/log/mysqld.log

### 一:基本命令

**0.查看当前连接数**

```sql
show global status like 'Thread$';
show variables like "%timeout%";
show variables like "log_%";
```

**1.查看当前连接状态**

```sql
show processlist; # 或者show full processlist 或 select * from information_schema.processlist
# 查看正在运行的线程以及命令
```

**2.数据库连接**

```sql
mysql -h 主机名 -u root -ppassword
```

**3.添加用户**

```sql
insert into user (host,user,password,select_priv,insert_priv,update_priv) values ('localhost','guest',password('guest123'),'Y','Y','Y');
```

**4.创建用户**

```sql
create user 'username'@'host' identified by 'password';
create user 'username'@'%' identified by 'password';
```

```sql
#新创建用户无法登陆问题?
use mysql；
delete from user where user='';
flush privileges;

# 对db_name下所有表都有查询(SELECT)权限
grant select on db_name.* to 'username'@'%';

# 对所有表有全部权限
grant all on *.* to 'username'@'%';
```

**5.删除用户**

```sql
drop user 'username'@'host';
```

**6.修改用户密码**

```sql
set password for 'username'@'host' = password('123password');
update user set password=password("你的新密码") where user="root";
```

**7.创建数据库病设置字符集和排序规则**

```sql
create database data_name;
create database data_name character set utf8 collate utf8_general_ci;
```

**8.删除数据库**

```sql
drop database data_name;
```

### 二:操作命令

**1.删除表**

```sql
SELECT concat('DROP TABLE IF EXISTS ', table_name, ';')FROM information_schema.tablesWHERE table_schema = 'mydb';
# 或者
drop table table_name;
```

**2.显示表属性**

```sql
desc user_table;
show columns from user_table;
```

**3.显示数据表的索引信息**

```sql
show index from user_table;
```

**4.显示数据库所有以run开头的表信息**

```sql
show table status like'run%';
```

**5.创建表,engine=指定存储引擎,每张表都可以指定存储引擎**

```sql
# CREATE TABLE IF NOT EXISTS `table_test`(
CREATE TABLE  `table_test`(
   `t_id` INT UNSIGNED AUTO_INCREMENT,
   `t_title` VARCHAR(100) NOT NULL,
   `t_author` VARCHAR(40) NOT NULL,
   `sub_date` DATE,
   PRIMARY KEY(`t_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

**6.插入数据**

```sql
insert into table_name(field1,field2,field3,field4) values(value1,value2,value3,value4);
```

**7.更改字段类型**

```sql
alter table system_info modify column ip varchar(100) ;
```

**8.更改字段为非空**

```sql
alter table system_info alter column ip set not null;
```

**9.添加字段**

```sql
alter table system_info add email varchar(30);
```

**10.删除字段**

```sql
alter table system_info drop column email;
```

**11.字段改名**

```sql
alter table system_info rename email to new_email;
```

**12.清空表或删除记录**

```sql
/* 清空表记录三种方式 */
# 1. delete
delete from table_name; 或 delete from table_name where id=1;
# 删除select记录报错:mysql不允许对同一个表同时进行查询和更新
# 解决方案:对查询结果生产一个派生表,对派生表查询
delete from table_user  where id in (select id from (select id  from table_user where sex is null) as tmp);

# 2.truncate
truncate table_name 

# 3.use information_schema 清空所有表记录
select table_name,table_schema from information_schema.tables where table_schema='alphacapture_bigai'
select table_name,table_schema from information_schema.tables where table_schema like '%alphacapture_bigai%'
select concat('truncate table',table_schema,'.',table_name,';') from information_schema.tables where table_schema in ('数据库1','数据库2')
```

**13.插入记录**

```sql
insert into table_name(field1,field2,field3) values(value1,value2,value3);
```

**1.更新记录**

```sql
update table_name set field2="张三" where id =3;``
```

**15.修改表名**

```sql
alter table table_name rename to new_table_name;
```

**16.模糊查询,%表示任意字符**

```sql
select *  from Student where name like "%三%"
```

**17.多条件查询and,or**

```sql
select * from Sudent where age between 18 and 50;
select * from Student where age >18 and age <60 and address='上海'
```

**18.去重**

```sql
select distinct address from Student;
```

**19.排序:asc升序,desc倒序**

```sql
select * from Student order by age desc;
```

**20.查询上做计算**

```sql
select age*3 name from Student;
```

**21.最大max,最小min,平均avg,求和sum,个数count**

```sql
select count(id) from Student;
```

**22.分组查询 group by 将某一列相同数据视为一组**

```sql
#使用了group by,select后只能跟分组列和聚合函数
#查询人数大于3的地区的最大年龄
select address,max(age) from Student group by address having count(*)>3;
```

**23.分页**

```sql
select * from Student limit 3,5; # 从第三条记录,查询五条
select * from Student limit (n-1)*m,m; # 第n也查询m条记录
```

**24.join连表查询 on 条件**

```sql
select Sites.id,Sites.name,Log.count,Log.date from Sites inner join Log on Sites.id=Log.site_id;
```

**24.查看表占用磁盘空间大小,M单位**

```sql
# 查看单个表
select concat(round(sum(DATA_LENGTH/1024/1024),2),'M') as table_size  from information_schema.tables where table_schema='csjdemo' AND table_name='demo2';
SELECT (`DATA_LENGTH`+ `INDEX_LENGTH`)/1024/1024  as `table_data_size`  from `TABLES` WHERE TABLE_NAME ='tableName' and TABLE_SCHEMA='dbName';
#查看数据库
SELECT (sum(`DATA_LENGTH`) +sum(`INDEX_LENGTH`))/1024/1024   as `db_data_size`  from `TABLES` where `TABLE_SCHEMA`='dbName';
```

**25.创建主键primary三种方式**

```sql
create table table_name(
    uid INT PRIMARY KEY,
    uname VARCHAR(10),
)
create table table_name(
    uid INT,
    uname VARCHAR(10),
    PRIMARY KEY(uid),  # 或者PRIMARY KEY(uid,uname)联合主键
)
alter table table_name add PRIAMRY KEY(udi);  # 添加主键约束
alter table table_name drop PRIMARY KEY;      # 删除主键约束 
```

**26.创建唯一索引三种方式**

```sql
create table table_name(
    uid INT,
    uname VARCHAR(10),
    UNIQUE []
)
alter table table_name unique index(filed_name,filed_name)
create UNIQUE INDEX indexName on table_name(filed_name,filed_name)
```

### 数据(复制|导入|导出)操作

**1.复制n条记录并创建**

```sql
INSERT into reyo (num,overtime) SELECT num,overtime from reyo where id IN(1,3,5,6,7,9);
INSERT into reyo (`num`,`overtime`) SELECT `num`,`overtime` from reyo where id IN(1,3,5,6,7,9);
```

2.导出整个数据库

```sql
mysqldump -u root -ppassword dbname>dbname.sql

mysqldump -u root -p --all-databases >all-data-$(date+%F).sql  # 备份所有数据库
mysqldump -u root -p --databases auth mysql >auth-mysql.sql    # 备份auth和mysql数据库
mysqldump -u root -p dbname table_name >table_name.sql        # 备份数据库
mysqldump -u root -p -d dbname table_name > table_name.sql    # 仅备份表结构
mysqldump -u root -p -t dbname table_name > table_name.sql    # 仅备份数据

mysqldump -usoc-user -pSocuser@0511 -t -T /var/lib/mysql-files/ temp loophole_cnvd --where="id<200"  --fields-terminated-by=',' --fields-enclosed-by='\"' > loophole_cnvd.csv
-t: 不写表的创建信息
--fields-terminated-by:输出文件中的字段以给定的字符串结尾
--fields-enclosed-by:输出文件中的字段用给定的字符括起来。

https://zhuanlan.zhihu.com/p/396005871
```

**3.导出表 show variables like '%secure%'查看安全目录**

```sql
mysqldump -u root -p dbname users>dbname_users.sql
SELECT * FROM runoob_tbl  INTO OUTFILE '/var/lib/mysql-files/Dbug_manangement.txt';
SELECT * FROM users  INTO OUTFILE '/var/lib/mysql-files/users.sql';
```

**4.导入备份的整个数据库**

```sql
mysql -u root -p < Detector.sql     # 需要再sql文件创建或指定数据库
mysql>source /home/abc/abc.sql      # 进入数据库下use Detector
```

**5.插入数据到某个表**

```sql
load data local infile "/var/lib/mysql-files/CaseUrl.sql" into table CaseUrl;
load data local infile "/var/lib/mysql-files/CaseUrl.sql" into table CaseUrl
(id,name, url, status_code, result, processresult, proposal,@create_time,test_time,case_id) FIELDS TERMINATED BY ', '
set create_time=DATE_FORMAT(@create_time,"%Y-%m-%d %H:%i:%s")
```

### Mysql性能优化

> [高性能优化总结](https://javaguide.cn/database/mysql/mysql-high-performance-optimization-specification-recommendations.html#%E5%AF%B9%E4%BA%8E%E9%A2%91%E7%B9%81%E7%9A%84%E6%9F%A5%E8%AF%A2%E4%BC%98%E5%85%88%E8%80%83%E8%99%91%E4%BD%BF%E7%94%A8%E8%A6%86%E7%9B%96%E7%B4%A2%E5%BC%95)
>
> [超详细的MySQL高性能优化实践总结](https://cloud.tencent.com/developer/article/1921568)
>
> [mysql配置参数调优](https://blog.csdn.net/LJFPHP/article/details/100751502)
>
> [MySQL参数优化](https://cloud.tencent.com/developer/article/1655879)
>
> [mysql8.0配置文件优化](https://www.cnblogs.com/john-xiong/p/12099842.html)
>
> 四个维度:
>
> 1.架构
>
> 2.硬件
>
> 3.DB优化
>
> 4.sql优化

##### 架构

> 使用集群负载(MariaDB Galera Cluster，Mysql innoDB cluster，Percona XtraDB cluster )，读写分离，数据库切分

##### 硬件

> 高效的磁盘读写性能

##### DB

> 参数优化(日志不能笑,缓存足够大,连接够用)
>
> my.ini或my.cnf配置文件
>
> ```
> 1.sort/join/read/rnd buffer:4M或8M或16M
> 2.tmp/heap table:96M或128M
> 3.innodb_flush_log_at_trx_commit  # 对redo日志刷盘频率的设定
> 0:缓冲区的redo log会每秒写入到磁盘的日志文件。但每次事务提交不会有任何影响，也就是 log buffer 的刷写操作和事务提交操作没有关系。在这种情况下，MySQL性能最好，但如果 mysqld 进程崩溃，通常会导致最后 1s 的日志丢失
> 1:每次事务提交时,缓冲区redo log保证一定会被写入到磁盘的日志文件。这也是默认值。这是最安全的配置，但由于每次事务都需要进行磁盘I/O，所以也最慢
> 2:每次事务提交时,缓冲区redo log异步写入(不保证)到磁盘的日志文件。这时如果 mysqld 进程崩溃，由于日志已经写入到系统缓存，所以并不会丢失数据；在操作系统崩溃的情况下，通常会导致最后 1s 的日志丢失。
> sync_binlog:binlog刷盘的频率
>
> 4.innodb_flush_log_at_trx_commit和sync_binlog都设置为1 (保证主库和主从库的一致性)
> 5.interactive_timeout:交互模式下超时时间,五分钟或十分钟
> 6.lock_wait_timeout:表锁锁定时间
> 7.time_zone:使用datetime减少性能消耗
> 8.wait_timeout:程序连接mysql超时时间,五分钟或十分钟
> 9.innodb_buffer_pool_size:缓冲池大小(越大,磁盘I/O减少)建议值为系统内存的50%-70%
> 10.innodb_buffer_pool_instances:配置多个缓冲池实例
> 11.tmp_table_size:临时表的最大大小
> 11.max_connections: 代表mysql的最大连接数,默认151,上限为100000,生产建议为5000-10000
> ```

##### sql语句优化

> [mysql](https://www.zhihu.com/question/486105337/answer/2538190061)
>
> **explain:**查看sql的执行计划,检查sql语句定位优化点或开启慢查询定位优化点
>
> **optimizer trace**:查询计划分析器(打开optimizer trace功能,执行命令,到information_schema.OPTIMIZER_TRACE查看)
>
> 优化方向:(避免不要的列|分页优化|索引优化|JOIN优化|排序优化|union优化)
>
> **优化表结构**
>
> ```
> 1.尽量使用数字型字段(引擎在处理查询和连接时会逐个比较字符串中每一个字符，而对于数字型而言只需要比较一次就够了)
> 2.尽可能的使用 varchar 代替 char(变长字段存储空间小，可以节省存储空间)
> 3.索引列大量重复数据时，可以把索引删除掉(比如)
> ```
>
> **索引优化**
>
> ```
> - 合理使用索引(一个表索引不超过5个),避免索引失效
> - 利用覆盖索引
> - 正确使用联合索引
> - 避免索引失效情况
> ```
>
> **避免不要的列**
>
> ```
> - 避免使用select *
> - 多用limit
> - 选择合理的字段类型
> ```
>
> **分页优化(数据量较大)**
>
> ```
> - 延迟关联
> - 书签方式
> ```
>
> **JOIN优化**
>
> ```
> - join表不宜过多(不超过5个)
> - 小表驱动大表
> - 用连接查询代替子查询
> ```
>
> **排序优化**
>
> ```
> 利用索引排序
> ```
>
> **union优化**
>
> ```
> 使用UNION ALL(不去重,所有数据)替代UNION(去重)
> ```

##### 索引失效的情况

> 参考: [索引失效](https://juejin.cn/post/7161964571853815822)

```
(1)联合索引不满足最左匹配原则,联合索引最左边字段必须出现在查询条件中
(2)错误使用like,前导模糊查询，以%开头如 like '%abc',(当like以%结尾索引有效)
(3)错误使用or,or两边字段有一个没有创建索引(where id=2 or name="Tom")或两边为范围查询(where id>10 or id<20),导致失效
(4)索引列参与运算或使用函数, 如where id-1=10, where SUBSTR(id_no,1,3)=100: 索引保存的是索引字段原始值,不是计算后的
(5)类型隐式转换,如where条件上进行了类型转换,比如字段是字符串类型,却填上了数字
(6)两列做比较,即使两列都有索引,也会失效 where id>age
(7)不等于比较,where name!="Tom" 或 where id<>"11" 有可能不走索引,查询结果集较小货走索引否则不走索引
(8)in或not in:IN肯定会走索引,但是当IN的取值范围较大(in在结果集大于30%时候索引失效)时会导致索引失效，走全部扫描
(9)order by:主要是mysql自身优化问题(走索引+回表/不走索引,直接全部扫描)
(8)非空判断(is not null / is null / not in / in / exists / not exists/ )
使用where id_no is not null不走索引,is null走索引
使用not exists 不走索引
使用where id not in (2,3)普通索引则失效,主键走索引
(9)当mysql估计全表扫描速度比索引速度快的时候不会使用索引(order by就是如果是select *则有大量回表,索引不走索引,走全表扫描到内存去排序)
select * 不会直接导致索引失效,不走索引大概率是因为where插叙范围过大导致，无法使用索引覆盖
```

##### MySQL内存优化

> 可以增加某些缓存和缓存区来提高MySQL的性能，可以修改默认配置，以便在内存有限的系统上运行

**全局共享**

```
innodb_buffer_pool_size:定义缓冲池大小,建议值为系统内存的50%-70%,它是存放表/索引/其他数据的
innodb_buffer_pool_instances: 内存较大时，可以将缓冲池分为多个缓冲池实例来提高并发
innodb_log_buffer_size: innoDB日志缓冲的大小
innodb_log_file_size: 
innodb_additional_mem_pool_size：InnoDB存放数据字典和其他内部数据结构的内存大小，5.7已被移除
key_buffer_size：MyISAM缓存索引块的内存大小
query_cache_size：查询缓冲的大小，8.0已被移除
```

**线程独占**

```
thread_stack：每个线程分配的堆栈大小
sort_buffer_size：排序缓冲的大小
join_buffer_size：连接缓冲的大小
read_buffer_size：MyISAM顺序读缓冲的大小
read_rnd_buffer_size：MyISAM随机读缓冲的大小、MRR缓冲的大小
tmp_table_size/max_heap_table_size：内存临时表的大小
binlog_cache_size：二进制日志缓冲的大小
```

##### 优化工具

```
查看数据参数信息: show [session|global] variables
查看数据的状态信息: show [session|global] status
Innodb引擎的所有状态: show engine innodb status
查看当前所有连接的session状态: show processlist
获取语句的执行计划: explain
慢查询记录: slow-log
查看锁状态: show status like '%lock%'; 
杀掉有问题的session: kill SESSION_ID
```



### 索引详解

> 操作系统和磁盘:最小单位是块block
> 操作系统和内存:最小单位是页page
>
> 磁盘I/O:文件系统每次读取一块(默认4K)单位大小到内存
> InnoDB :存储数据以页(page默认16k)为单位,InnoDB 读取一页页读取

#### 索引演化史

> B树和B+树最大区别:
>
> B的非叶子节点可以存储数据，而B+树只有叶子结点才可以存储数据,一个节点可以存储很多数据，所以B树的高度大大减小，
>
> 但是B树相对于B+树来说，在查找数据的时候，由于每一个节点都有可能包含目标数据，所以查找总是从根节点进行向下搜索，这个特点会带来大量的随机io。
>
> 而在B+树种，因为叶子结点才会存储数据（InnoDB），这样子相比B树一个页大小存储的索引数据就更多了（16K），并且叶子结点通过双向指针指向相邻的节点，依次连接。
>
> 并且相邻结点是有序的，所以对于范围查找是非常方便的，获取到第一个符合条件的，然后通过指针，往后获取数据，直到最后一个不满足条件为止。

> **二叉查找树->AVL平衡二叉树->B-Tree(多路平衡查找树)->B+Tree:**
> **B-Tree:**
>
> ```
> 多路平衡查找树,每个节点包含多对(父节点指针,子节点指针,键key,值data),相比于AVL缩减了节点数,
> ```
>
> **B+Tree:**
>
> ```
> 1.非叶子节点(双向链表)只存储键值+叶子节点指针,
> 2.值data顺序存在同一层的叶子节点上，相比于B-Tree每个节点能存储更多的key减少了树的高度和磁盘I/O次数，
> 3.叶子节点之间有指针,链表支持范围查找
> 通过非叶子节点的二分查找以及指针确定数据在哪个页中,进而去数据页查找数据
> 树的高度为1-3:
>   1.叶子节点16k(一条数据一般1k)存16条数据
>   2.非叶子节点存1170个指针=1170*1170*16=21902400**
> ```

#### 什么是索引

> 对一列或多列值进行排序的数据结构(类似目录排序好了的,在小文件查找)

#### mysql有哪些索引?那些字段可以建立对应索引

> 任何标准版最多创建16个索引列
>
> 普通索引：加快查询
> 主键索引：聚簇索引,唯一索引unique唯一且不为NULL
> 复合索引: **多个字段的索引**最多包含16列:where多条件最左原则),可用于包含所有列或第一列,前两列,前三列...等,blob和text也能创建索引, 但是必须指定前面多少位,组合索引查询遵循**最左前缀原则**,能够避免**回表查询**
> 全文索引: char、varchar，text 列上可以创建全文索引,一般不使用,不是mysql专长
> 唯一索引: 唯一性
> 空间索引: 对空间数据类型字段建立索引,mysql有四种:GEOMETRY,POINT,LINESTRING,POLYGON
> **聚簇索引**和**非聚簇索引**：聚簇索引和非聚簇索引的概念比上面的概念要大，属于包含和被包含的关系。例如：InnoDB中主键索引使用的就是聚簇索引
>
> InnoDB存储引擎中，索引分为 **聚簇索引**和**二级索引**，主键索引就是聚簇索引，其它的索引为二级索引

#### 聚集索引和非聚集索引区别

> **都是B+Tree数据结构**
> 聚簇索引：索引的叶节点就是数据节点，叶子节点中数据域存储数据文件本身，索引和数据存储在一起
>
> 非聚簇索引：叶节点仍然是索引节点，索引文件和数据文件是分开的，只不过有一个指针指向对应的数据块，所以查询数据会多一次查询
>
> 因此聚簇索引的查询速度会快于非聚簇索引的查询速度，在Mysql的存储引擎中，「InnoDB支持聚簇索引，MyISAM支持非聚簇索引

#### InnoDB/MyISAM区别

> MyISAM:不支持事务,支持表级别锁(限制了读/写的性能),拥有较高的插入和查询速度,B+的非聚簇索引,通常用于只读或以读为主的场景.
> 怎么快速向数据库插入100万条数据?先用MyISAM插入数据,然后修改存储引擎为InnoDB
> InnoDB:支持事务,支持行/表级别锁,/外键(数据的完整性和一致性更高),采用B+的聚簇索引,通常用于经常更新的场景.

#### InnoDB和MyISAM索引区别

> InnoBD主键索引采用B+的聚簇索引:
>
> 每个InnoDB表都有且只有一个特殊的索引，称为聚簇索引 ，用于存储行数据。通常，聚簇索引与主键同义 。
>
> 1. 表定义了主键,则pk就是聚集索引
> 2. 没有定义主键,第一个非空唯一索引列就是聚集索引
> 3. 否则,InnoDB会创建一个隐藏的row-id作为聚集索引
>
> MyISAM索引采用B+的非聚簇索引:
>
> ```
> 不存储全部数据,只存储数据行的地址
> ```

#### 什么是回表

> where不在主键上，则通过非主键索引查询,select所获取的字段不能通过非主键索引获取到,只能查到主键,需要回表通过主键索引查到完整的数据。
>
> 所以被查询的列，数据能从索引中取得，而不是通过定位符row-locator再到row上获取，即“被查询列要被所建的索引覆盖”，这能够加速度查询。

#### 覆盖索引,非覆盖索引

> 覆盖索引:所查的字段在当前索引叶子节点上存在,不用回表,直接作为结果返回

#### 什么是索引下推

> where多条件判断,对索引中包含的字段先做判断,再去回表没有索引的字段(减少回表次数)

#### 正确使用索引的建议

`索引可以增加查询效率,但是也会降低插入和更新的效率`

**限制每张表上的索引数量**

> **单张表索引不超过5个**

**选择合适的字段建立索引**

> **那些情况适合建立索引?**
>
> 1.频繁查询的字段/被作为条件查询的字段
>
> 2.频繁需要排序的字段(索引已经排序)
>
> 3.关联字段，例如外键字段，student表中的classid,   classes表中的schoolid 等
>
> **什么情况下不推荐使用索引?**
>
> 1.数据唯一性差(比如性别只有两种数据)
> 2.频繁更新的字段不用索引
> 3.不用无序的的值如身份证,uuid无序不能作为索引
> 4.字段不在where语句后出现(where含IS NULL/IS NULL/IS NOT NULL/like "%"等,不用索引)
> 5.过长的字段使用前缀索引(**前缀索引仅限于字符串类型，较普通索引会占用更小的空间**)
> 6.参与计算的字段不适合建立索引
> 7.可能产生乱码的字段作为主键或唯一索引

**尽可能建立联合索引而不是单列索引**

> 每个索引对应一个B+树,多个字段在一个索引上将会节约磁盘空间，修改操作效率也会提升

**避免索引失效**

**减少回表思路**

> 使用索引下推解决回表问题，前提是和联合索引一起使用

### Mysql预编译

> ---
>
> #### Mysql架构
>
> ```
> **连接层**：处理连接/鉴权/安全管理
>
> **服务层**：系统管理/sql接口/缓存/解析/预处理/优化
>
> **引擎层**：具体与文件系统打交道
>
> **存储层**:
> ```
>
> #### sql语句执行流程:
>
> ```
> 1.客户端发送请求
> 2.连接器（验证用户身份，给予权限）
> 3.查询缓存（存在缓存则直接返回，不存在则执行后续操作）
> 4.分析器（对SQL进行词法分析和语法分析操作）
> 5.优化器（主要对执行的sql优化选择最优的执行方案方法）
> 6.执行器（执行时会先看用户是否有执行权限，有才去使用这个引擎提供的接口）
> 7.去引擎层获取数据返回（如果开启查询缓存则会缓存查询结果）
> ```
>
> **SQL语句预编译**
>
> **益处**:加快执行速度,防止sql注入
> **场景**:SQL语句一样,参数不一样,可以对SQL语句预编译
>
> **语法**:prepare name from statement;
>
> 1. 定义:prepare statement_1 from 'select * from user where id=?'; # 通过?进行占位
> 2. 参数:set @id=2;
> 3. 执行.execute statement_1 using @id;
>
> 怎么预防sql注入？
>
> 1. 不信任用户提交的数据(参数过滤,严格检查参数类型,转义,限制长度)
> 2. .mysql预编译(参数化查询,变量绑定)

### Mysql 事务

#### ACID?

> **原子性(Atomicity)**:(undo log回滚日志实现)指一个事务不可分割,是一个最小的操作单元(包含若干个操作),要么全部成功,要么全部失败
> **隔离性(Isolation)**:(锁和mvcc实现)多个事务并发执行,事务之间相互隔离
> **持久性(Durability)**:(redo log实现)InnoDB提供了一个缓存Buffer,读取和写入都先在Buffer中(并同时把操作记录到redo log,防止数据丢失)
> **一致性(Consistency)**:数据处于合法状态(满足预定约束就是合法)
> 从数据库层面，数据库通过原子性、隔离性、持久性来保证一致性。也就是说ACID四大特性之中，C(一致性)是目的，A(原子性)、I(隔离性)、D(持久性)是手段，是为了保证一致性，数据库提供的手段。数据库必须要实现AID三大特性，才有可能实现一致性。
> 从应用层面，通过代码判断数据库数据是否有效，然后决定回滚还是提交数据。
>
> **Innodb如何实现事务的?**
> 以update为例:
>
> ```
> (1).开启事务,Innodb根据接受的update语句,找到数据所在页,并修改该页缓存在Buffer pool(change buffer)中
> (2).执行update,修改Buffer pool中数据
> (3).记录 undo log日志(便于事务回滚和mvcc)并写入Log Buffer中并关联redo log(可刷盘)
> (4).记录 redo log(prepare状态)日志(便于断电恢复数据)并写入Log Buffer中(可刷盘)
> (5).记录bin log(数据表结构变更日志:用于主从复制和数据库恢复)
> (6-1).事务提交,redo log(改为commit状态),可触发redo log刷盘机制
> (6-2).事务回滚,则利用undo log日志进行回滚
> ```
>
> ```
> MVCC多版本控制:实现MVCC时用到了一致性视图，用于支持读提交和可重复读的实现
> 对于一行数据若是想实现可重复读取或者能够读取数据的另一个事务未提交前的原始值，那么必须对原始数据进行保存或者对更新操作进行保存，这样才能够查询到原始值
> 在Mysql的MVCC中规定每一行数据都有多个不同的版本，一个事务更新操作完后就生成一个新的版本，并不是对全部数据的全量备份，因为全量备份的代价太大了
> ```

#### 事务隔离级别

> **问题**
>
>> https://cloud.tencent.com/developer/article/2136022
>>
>
> ```
> 1.脏读:读到其他事务未提交的数据(读取了事务B已修改还没提交的数据)
> 	解决方法:1.事务隔离级别设置为(读提交read commmited)
> 		    2.读取时加共享锁(select ... lock in share mode),修改时加排它锁(select ... for update)
> 2.不可重复读:前后读取的数据不一致(务A中先后多次读取同一个数据，读取的结果不一样(因为B事务在A事务两次读取之前更改了数据))
> 	解决方法:1.事务隔离级别设置为(可重复读repeatable read)
> 			2.读取数据时加共享锁,写入数据时加排它锁
> 	
> 3.幻读:前后读取的记录数量不一致(一个事务中,select执行了两次,第二次返回了第一次没有的行)
> ```
>
> **隔离级别**
>
>> **SQL 标准**提出了四种隔离级别来规避这些现象，隔离级别越高，性能效率就越低，这四个隔离级别如下：
>>
>
> ```
> 读未提交（READ UNCOMMITTED）
> 读提交 （READ COMMITTED）
> 可重复读 （REPEATABLE READ）
> 串行化 （SERIALIZABLE）
> **InnoDB默认是可重复读，实际上线上都设置可重复读(可以避免很多间隙锁,对高并发写的性能明显提升)**
> ```
>
>> MySQL InnoDB 引擎的默认隔离级别虽然是「可重复读」，但是它很大程度上避免幻读现象（并不是完全解决了），解决的方案有两种：
>> 针对快照读（普通 select 语句），是通过 MVCC 方式解决了幻读，因为可重复读隔离级别下，事务执行过程中看到的数据，一直跟这个事务启动时看到的数据是一致的，即使中途有其他事务插入了一条数据，是查询不出来这条数据的，所以就很好了避免幻读问题。
>> 针对当前读（select ... for update 等语句），是通过 next-key lock（记录锁+间隙锁）方式解决了幻读，因为当执行 select ... for update 语句的时候，会加上 next-key lock，如果有其他事务在 next-key lock 锁范围内插入了一条记录，那么这个插入语句就会被阻塞，无法成功插入，所以就很好了避免幻读问题。
>>
>
> | 隔离级别 | 脏读   | 不可重复读 | 幻读   |
> | :------- | ------ | ---------- | ------ |
> | 读未提交 | 可能   | 可能       | 可能   |
> | 读提交   | 不可能 | 可能       | 可能   |
> | 可重复读 | 不可能 | 不可能     | 可能   |
> | 串行化   | 不可能 | 不可能     | 不可能 |
>
> **查看数据库隔离级别**
>
> ```
> show variables like 'transaction_isolation';
> SELECT @@transaction_isolation
> ```
>
> **修改隔离级别**
>
> ```
> set global transaction isolation level read committed; #改为读提交
> ```

### Mysql有几种日志

> 参考: [日志详解](https://javaguide.cn/database/mysql/mysql-logs.html#redo-log)
>
> bin log(二进制日志记录sql):用于数据备份主从
>
> ```
> 记录了数据库所有执行的DDL和DML语句（除了数据查询语句select、show等），以事件形式记录并保存在二进制文件中
> 在事务提交时才写入
> ```
>
> **redo log(重做日志): InnoDB特有，用于数据持久化**
>
> ```
> 记录了对于InnoDB存储引擎的事务日志,重启时使用redolog恢复数据,防止数据丢失，以便数据持久化
> 在事务执行过程中不断写入
> ```
>
> **undo log(回滚日志): InnoDB特有**
>
> ```
> 事务执行失败或调用了rollback,利用该日志进行回滚
> ```
>
> slow uery log(慢查询日志)
>
> ```
> 记录时间内超过long_query_time这个时间的查询语句,用来定位查询语句查询效率，以便进行优化
> ```
>
> general log(一般查询日志)
>
> ```
> 一般查询日志记录了所有对MySQL数据库请求的信息，无论请求是否正确执行
> ```
>
> error log(错误日志)
>
> ```
> 错误日志文件对MySQL的启动、运行、关闭过程进行了记录，能帮助定位MySQL问题
> ```

#### mysql日志是否实时写入磁盘?(log buffer)

> **bin log**
>
> ```
> sync_binlog=0:每次提交事务后不会马上写入到磁盘,先写到page cache,由操作系统决定写入什么时候写入磁盘(有丢失事务日志的风险)
> sync_binlog=1:每次提交事务都会执行fsync写入磁盘(强一致性,性能较低)
> sync_binlog=n:每次提交事务,先写到page cache,积累n个事务才fsync到磁盘(有丢失n个事务日志的风险)
> ```
>
> **redo log()和undo log**
>
> ```
> innodb_flush_log_at_trx_commit=0:每秒(log buffer中提交的事务)写入磁盘,系统并调用fsync写入磁盘(可能丢失一秒的数据,性能高)
> innodb_flush_log_at_trx_commit=1:有事务提交立即调用fsync写入磁盘(不会丢失,性能差)
> innodb_flush_log_at_trx_commit=2:有事务提交都写给操作系统的page cache,由操作系统决定什么时候调用fsync写入磁盘(一系列丢失,性能一般)
> ```

#### binlog有几种录入格式?

> statement: 默认方式,基于SQL语句的复制记录sql语句,文件较小,如时间记录要采用row格式
> row: 基于行的复制,文件较大
> mixed: 前两种混合
>
> MySQL 会判断这条 `SQL`语句是否可能引起数据不一致，如果是，就用 `row`格式，否则就用 `statement`格式

#### 为什么将redo log的数据写到磁盘比将Buffer数据持久化到磁盘要快?

> 1.Buffer数据持久化是随机写I/O,redo log是追加,顺序IO
> 2.Buffer数据持久化是以页page为单位,redo log只需要写入的真正部分(减少了无效I/O)

#### bin log和redo log(两段提交)区别？

> 1.写入redo log(prepare状态)
> 2.写入bing log
> 3.提交事务,redo log(改为commit)

### 锁机制

> **锁种类**
>
>> 按功能：分为共享锁(s)，怕他锁(x)
>>
>> 按粒度：分为表级锁,行级锁
>>
>> **意向锁:** 用到表锁时，需要判断表中记录是否有行锁，一行一行遍历肯定是不行，性能太差。我们需要用到一个叫做意向锁的东东来快速判断是否可以对某个表使用表锁
>>
>> 意向锁是表级锁，共有两种：
>>
>> - **意向共享锁（Intention Shared Lock，IS 锁）**：事务有意向对表中的某些记录加共享锁（S 锁），加共享锁前必须先取得该表的 IS 锁。
>> - **意向排他锁（Intention Exclusive Lock，IX 锁）**：事务有意向对表中的某些记录加排他锁（X 锁），加排他锁之前必须先取得该表的 IX 锁。
>>
>> **意向锁是由数据引擎自己维护的，用户无法手动操作意向锁，在为数据行加共享/排他锁之前，InooDB 会先获取该数据行所在在数据表的对应意向锁**
>>
>> 在 InnoDB 默认的隔离级别 REPEATABLE-READ 下，行锁默认使用的是 Next-Key Lock。但是，如果操作的索引是唯一索引或主键，InnoDB 会对 Next-Key Lock 进行优化 	，将其降级为 Record Lock，即仅锁住索引本身，而不是范围
>>
>
> ```
> 1.锁粒度划分
> 表锁:粒度最大的锁，开销小，加锁快，不会出现死锁，粒度大导致并发性低()
> 页锁：介于行锁和表锁之间的一种锁,页锁是在BDB中支持的一种锁机制，也很少没人提及和使用
> 行锁: 粒度最小，加锁开销性能大，加锁慢，并且会出现死锁，但是行锁的锁冲突的几率低，并发性能高(行锁是InnoDB默认的支持的锁机制，MyISAM不支持行锁)
>
> 2.使用方式划分
> 共享锁、排它锁(如果加排他锁可以使用select …for update语句)
> 加排它锁后，不能对该条数据再加锁，其它事务即不能查询也不能更改数据。
> mysql InnoDB引擎默认的修改数据语句,update,delete,insert都会自动给涉及到的数据加上排他锁
> select语句默认不会加任何锁类型，如果事务T对数据A加上共享锁后，则其他事务只能对A再加共享锁，不能加排他锁，共享锁下其它用户可以并发读取，查询数据。但不能修改，增加，删除数据。资源共享。
> 3.思路划分
> 乐观锁、悲观锁
> ```
>
> **行锁分类:**
>
>> **记录锁(Record Lock):** 属于单个行记录上的锁
>>
>> **间隙锁(Gap Lock): **锁定一个范围，不包括记录本身(用范围条件而不是相	等条件检索数据,并请求共享和排它锁时,InnoDB会给符合条件的的已有记录的索引项加锁),使用间隙锁的目的是位了防止幻读,以满足串行化的隔离级别
>>
>> **临键锁(Next-Key Lock):** Record Lock +Gap Lock 锁定一个范围，包含记录本身，主要目的是为了解决幻读问题，记录锁只能锁住已经存在的记录，为了避免插入新记录，需要依赖间隙锁
>>
>
>> ```
>> select * from user where userid>100 for update; userid的值(1...101)
>> 对于101会加锁,大于101但是记录不存在的也会加锁,防止其他事务在表末尾增加数据
>> ```
>>
>
> **死锁**
>
> 指两个或以上的进程，因争夺资源而互相等待的现象
>
> 关键在于:两个会以上的Session加锁的顺序不一致
>
> 解决关键是: 让不同的Session加锁有序
>
> 排查死锁流程
>
> ```
> 1.查看死锁日志
> show engine innodb status\G  # 查看当前事务内锁的状态
> 2.找出死锁sql
> 3.分析sql加锁情况
> 4.模拟死锁案发
> 5.分析死锁日志
> 6.分析死锁结果
> ```
>
> 死锁在InnoDB中才会出现死锁
>
> ```
> 1.对表有高并发时，尽量对该表执行串行化
> 2.调整SQL 执行顺序， 避免 update/delete 长时间持有锁的SQL在事务前面
> 3.设置参数,innodb_lock_wait_timeout 超时时间
> 4.innodb_deadlock_detect打开,当发现死锁时，自动回滚某个事务
> ```

### 主键方案(自增id/uuid/雪花算法)

> https://www.zhihu.com/question/397289720
> https://juejin.cn/post/7153273187366043661

#### 三种方案:

    1. 自增id
    2. uuid: uuid导致页分裂,性能问题,存储空间较大
    3. 雪花算法及其改进算法

#### 分布式id实现方式:

> **满足条件**:
>
> 1.全局唯一:必须保证ID是全局性唯一的
>
> 2.高性能:ID生成响应要快
>
> 3.趋势递增
>
> **常见方式**
>
> **1.uuid:**
>
> ```
> UUID的核心思想是使用「机器的网卡、当地时间、一个随机数」来生成UUID
> 缺点:
> 1.UUID生成的无序的字符串，查询效率低下，
> 2.不具备自增特性,没有实际的业务含义
> 3.长度过长影响性能
> 所以都不会使用UUID作为分布式ID来使用
> ```
>
> **2.单机数据库自增ID+步长R**
>
> ```
> 数据库的auto_increment自增ID完全可以充当分布式ID
> 缺点:
> 1.DB单点存在宕机风险，无法扛住高并发场景
> ```
>
> **3.redis自增ID**
>
> ```
> 利用redis的 incr命令实现ID的原子性自增
> ```
>
> **4.雪花算法(Snowflake)及其改进算法**
>
> ```
> **雪花算法(保证递增性)**:64位
> 1bit: 正数位
> 41bit: 时间戳
> 5bit: 机器id
> 5bit: 数据中心
> 12bit: 自增值
> ```

### 性能极限

**mysql性能极限**

> mysql单表字段数:建议20-50
> mysql默认单字段大小：最大行长度限制是所有字典的总和,(65535)65532---(21845)21844
> 存储最大空间为1M,可以修改max_allowed_packet=16
> mysql单表：
> 老版mysql3.22中,还是ISAM存储引擎,单表限制为4GB
> 之后为INNODB 单表限制64TB
> 数据库:
> Cmshelp 团队做CMS 系统评测时的结果来看,
> MySQL单表大约在2千万条记录（4G）下能够良好运行，
> 经过数据库的优化后5千万条记录（10G）下运行良好。
> 阿里巴巴《Java 开发手册》提出单表行数超过 500 万行或者单表容量超过 2GB，才推荐进行分库分表。
>
> 分表: 单标数据量太大,索引效率太低了
> 分库: 并发量导致连接数不够了

**PostgreSQL性能极限**

> 最大单个数据库大小:不限
> 最大数据单表大小:32TB
> 单条记录大小:1.6TB
> 单字段最大允许:1GB
> 单表允许最大记录数:不限
> 单表最大字段数:250-1600取决于字段类型
> 单表最大索引数:不限

### 主从方案

> Mysql主从复制中有三个线程:Master(binlog dump thread) Slave(I/O thread,SQL thread)
> 使用binlog+position偏移量进行增量同步
>
> **同步过程**
>
> 1. Master所有变更都记录到binlog中去(MySQL Server层的实现)
> 2. 主节点binlog dump线程,当binlog有变动时,binlog dump线程读取内容并发送给从节点
> 3. 从节点I/O线程接收binlog,并写入到relay log(中继日志)中
> 4. 从节点SQL线程读取relay log并对数据进行重放
>
> **同步策略**
>
> - 同步策略:Master会等待所有的Slave回应后才提交(这个策略严重影响性能)
> - 半同步策略:Master至少等待一个Slave回应后才提交
> - 异步策略:Master不会等待Slave回应就可以提交(默认)
> - 延迟策略:Slave落后Master指定的时间
>
> **同步延迟原因**
>
> ```
> 从服务器的里面读取binlog的线程仅有一个，从服务器sql执行时间过长或sql对表上锁了，主服务器的SQL大量积压，未被同步到从服务器里
> ```
>
> **同步延迟解决**
>
> ```
> 1.选择更好的从服务器，或从服务器只做备份
> 2.sync_binlog=1，innodb_flush_log_at_trx_commit = 1 都设置为1
> 3.
> ```

mysql如何保证主从数据的一致性的？

分片中间件:myCat/shardingSphere

**一主多从:缓解读压力**

1. 主服务配置mysql.cnf:

   > #主服务还需要创建对应权限的用户用于数据同步
   >
   > log-bin=mysql-bin   # 表示启用二进制文件-文件名称
   > server-id=3307      # 表示server编号
   >
2. 从服务执行sql命令

   > \# 1.配置主服务
   >
   > change master to master_host="192.168.1.2",master_port=3306,master_user="copy",master_password="123456",master_log_file="mysql-bin.00001",master_log_pos=154;
   >
   > \# 2.开启主从同步
   >
   > start slave
   >
   > \# 3.查看是否成功
   >
   > show slave status \G;
   >

**双主双从:缓解写压力**

1. 主1配置

   > log-bin=mysql-bin
   >
   > server-id=3301
   >
   > auto_increment_increment=2 # 主键递增步长
   >
   > auto_increment_offset=1   # 从1开始
   >
   > log-slave-updates      # 是否记录binglog
   >
   > sync-binlog=1        # 几次事务记录binlog
   >
2. 主2配置

   > log-bin=mysql-bin
   >
   > server-id=3302
   >
   > auto_increment_increment=2 # 主键递增步长
   >
   > auto_increment_offset=2   # 从1开始
   >
   > log-slave-updates      # 是否记录binglog
   >
   > sync-binlog=1        # 几次事务记录binlog
   >

### 集群

> raft协议:
> MariaDB Galera Cluster
> Mysql innoDB cluster
> Percona XtraDB cluster

### 额外问题及思路

**"Lost connection to MySQL server during query" ?**

> 1网络延迟高
> 2.读/写:导致数据传输超时，net_read_timeout/net_write_timeout
> 3.连接初始化超时,connect_timeout 默认30s
> 4.传输中使用了较大的string field或blob field 导致超过了max_allowed_packet
> https://blog.csdn.net/zyself/article/details/91376690

**数据库的三大范？**

> 为设计冗余小,结构合理的数据库,设计数据库时必须满足一定范式(规则)
> 一般设计都是反范式,通过冗余的数据避免跨表垮库查询,利用空间换时间,提高性能
> 第一范式:表中所有字段是不可分解的原子值
> 第二范式:表中每一列都和主键相关,而不能只与主键一部分相关(针对联合主键)(表中只保存一种数据,不可以把多种数据保存在同一个表中)
> 第三范式:确保每列都和主键直接相关而不是间接相关

#### NULL和‘’的区别

> 不建议使用NULL
>
> 1.''的长度是0不占用空间,NULL需要占用空间
> 2.NULL代表一个不确定的值,不一定相等
> 3.查询NULL时,必须使用IS NULL或IS NOT NULL,不能使用 = !=

#### **varcahr和char区别？**

> char(最多存放255个字节)适用数据大小固定/较小/经常更新/不容易产生内存碎片:
> 1.长度固定,插入数据小于固定长度则用空格填充
> 2.存取速度比varchar快很多(甚至50%),空间换时间
> varchar(最多存放(65535)65532个字节,等价于(21845)21844字符):
> 1.varchar=长度+N(实际长度n>255,用两个字节存放长度.小于255,用一个字节存放长度)
> 2.长度可变,按实际插入数据来存储()
> 3.填写2的n次方,varchar(8),varchar(64)
> 4.因为InnoDB 的数据页默认是 16K，每个页中至少存放 2 行数据，因此建议VARCHAR字段的总长度不要超过 8K=8192字节byte。

> InnoDB表索引前缀长度为767字节,utf-8编码为255(255*3=765)
> 对text,只能添加前缀索引,前缀索引最大能达到1000字节
> 当varchar大于某些值:
> varchar大于255自动变为tinytext
> varchar大于500自动变为tinytext
> varchar大于20000自动变为tinytext
> 当varchar>255,使用varchar或text没有区别

#### **blob和text区别？**

> blob:二进制大对象(存储二进制数据,没有字符集)最大长度16k
> text:大对象,存储大字符串,有字符集(根据字符集的校对规则对值进行排序比较)最大长度16k

#### **DATETIME和TIMESTAMP区别？**

> DATETIME 和 TIMESTAMP 底层也是整型存储,DateTime底层实现是Bigint，索引存储上和Bigint一模一样,所以Bigint支持索引查询,datetime也支持
> 都表示日期和时间,格式一致,存储秒后6位小数
> 区别
> 日期范围:DATETIME(1000-01-01到9999-12-31),TIMESTAMP(1970-01-01到2038-01-09)
> 存储空间: MySQL5.6.4之前(DATETIM为8字节,TIMESTAMP为4字节),MySQL5.6.4开发(DateTime为5~8字节,TimeStamp为4~7字节)
> 时区:DATETIME与时区无关,TIMESTAMP与时区有关
> 默认值:DATETIME默认为null,TIMESTAMP默认为当前时间,不为空(not null)

#### Datetime/TimeStamp/integer 性能对比

> MyISAM 引擎，无索引（推荐）：int > UNIXTIMESTAMP(timestamp) > datetime（直接和时间比较）> timestamp（直接和时间比较）> UNIXTIMESTAMP(datetime)
> MyISAM 引擎，有索引: UNIXTIMESTAMP(timestamp) > int > datetime（直接和时间比较）>timestamp（直接和时间比较）>UNIXTIMESTAMP(datetime)
> InnoDB无索引(不建议):int > UNIXTIMESTAMP(timestamp) > datetime（直接和时间比较） > timestamp（直接和时间比较）> UNIXTIMESTAMP(datetime)
> InnoDB有索引:int > datetime（直接和时间比较） > timestamp（直接和时间比较）> UNIXTIMESTAMP(timestamp) > UNIXTIMESTAMP(datetime)
> 一句话，对于 MyISAM 引擎，采用 UNIX_TIMESTAMP(timestamp) 比较；对于InnoDB 引擎，建立索引，采用 int 或 datetime直接时间比较

#### **in和exists的区别？**

> https://blog.csdn.net/jinjiniao1/article/details/92666614

#### **DECIMAL记录货币？**

> float和double是二进制存储,有误差
> decimal是字符串存储

#### **怎么存储表情包emoji?**

> 字符串存储utf-8+mb4编码

#### 字符集和排序规则

> 参考:
>
> [MySQL建立数据库时字符集和排序规则的选择](https://blog.csdn.net/hsuehgw/article/details/128737673)
>
> [utf8mb4总结](https://blog.csdn.net/qq_17555933/article/details/101445526)

#### **大量外键问题？**

> 不影响select，影响update/insert/delete(当对子表进行写入操作,父表会被加上共享锁,对子表进行高并发时,父表的共享锁长时间不能释放,就不能对父表进行写入而只能读)

> WAL技术(Write-Ahead Logging)RedoLog(对所有页面的操作写入日志文件,实现事务的持久性)

#### **delete删除记录使用binlog回滚？**

> 恢复数据时可以先备份,在停止所有写入操作:flush tables with read lock或 set global read_only=1同时配置文件里设置read_only防止重启失效
>
> 1. 查看binglog是否开启
>
>    ```sql
>    show variables like '%log_bin%';
>    ```
> 2. 查看数据文件存放路径
>
>    ```sql
>    show variables like '%datadir%';
>    show master status;  # 查看当前正在写入的binlog
>    show master logs;    # 查看所有binlog  show binary logs;
>    ```
> 3. 查看binlog日志内容
>
>    ```sql
>    show binlog events in 'mysql-bin.000001'\G;  # 确定需要回滚的事务的position
>    ```
> 4. 将需要恢复的事务里的操作转为sql
>
>    ```shell
>     #使用--start-position或--start-datetime="2022-03-20 10:00:00"
>    /opt/bitnami/mysql/bin/mysqlbinlog  --no-defaults -v --database=database_name --start-position="966048" --stop-position="981142" /bitnami/mysql/data/mysql-bin.000007 > /tmp/mysqllog.sql
>    ```
> 5. 将导出导出sql的delete转换为insert
>
> ``shell cat srliao.sql.bak| sed -n '/###/p' | sed 's/### //g;s/\/\*.*/,/g;s/DELETE FROM/;INSERT INTO/g;s/WHERE/SELECT/g;' |sed -r 's/(@17.*),/\1;/g' | sed 's/@1=//g'| sed 's/@[1-9]=/,/g' | sed 's/@[1-9][0-9]=/,/g' > mysqllogOK.sql ``
>
> 6. 执行insert sql
>
>    ```shell
>    source /tmp/mysqllogOK.sql
>    ```

#### **大公司为什么不使用外键强关联问题？**

> 主要存在以下问题
> 1.在该表进行增删改查会触发查询关联表的记录是否存在,该性能消耗系统是允许的
> 2.数据一致性全部交给数据库,数据库是否能承受
> 3.查询关联表上会做一个内部锁,是否存在高并发死锁情况
> 4.后期的分库分表,外键约束格外离谱
> 这些问题在互联网公司显得很严重,访问量大的时候,mysql系统上无法得到解决的
> https://www.cnblogs.com/JethroYu/p/13570630.html

#### **delete,truncate,drop有什么区别?**

> **执行速度**:drop>truncate>delete

**1.delete**

> 1.属于数据库DML操作语言,只删数据不删表结构,会走事务,执行时触发trigger
> 2.delete执行时,会将删除数据缓存到rollback segement中,事务commit之后生效
> 3.delete删除全部数据,MyISAM会立刻释放磁盘空间,InnoDB不会释放
> 4.delete from table_name where 带条件的MyISAM和InnoDB都不会释放磁盘空间
> 5.delete之后optimize table table_name会立刻释放磁盘空间,不管MyISAM或InnoDB
> 6.delete操作是一行一行删除,且产生删除操作日志,并记录到redo和undo
> 7.delete删除后id会继续递增
> ALTER TABLE TableName AUTO_INCREMENT=1； # 将auto_increment重置

**2.truncate**

> 1.属于DDL定义语言,不走事务,原数据不放到rollback segement中,执行不触发trigger
> 2.truncate table table_name会立刻释放磁盘空间不论MyISAM或InnoDB,类似drop table然后create table,做了优化
> 3.快速清空表,并重置auto_increment的值
> MyISAM：truncate会重置auto_increment为1,delete后不变
> InnoDB: truncate会重置auto_incrment为1,delete后不变(delete之后重启则auto_increment为1)
> 也就是说，InnoDB的表本身是无法持久保存auto_increment。delete表之后auto_increment仍然保存在内存，但是重启后就丢失了，只能从1开始。实质上重启后的auto_increment会从 SELECT 1+MAX(ai_col) FROM t 开始。

> SET FOREIGN_KEY_CHECKS=0;            #取消外键约束
> TRUNCATE TABLE  table_name;
> SET FOREIGN_KEY_CHECKS=1;            #设置外键约束:

**3.drop**

> 1.属于DDL定义的语言
> 2.drop之后立刻释放磁盘空间,不管是MyISAM或InnoDB
> 3.drop且删除表结构,被依赖的约束(constrain),触发器(trigger),索引(index)
> 4.依赖该表的存储过程/函数将保留,状态为invalid
> delete是把目录撕了，truncate是把书的内容撕下来烧了，drop是把书烧了

#### 一个SQL语句在MySQL中执行流程

> https://javaguide.cn/database/mysql/how-sql-executed-in-mysql.html

#### Mysql如何存储IP地址

> MySQL 提供了两个方法来处理 ip 地址
>
> - `INET_ATON()`：把 ip 转为无符号整型 (4-8 位)
> - `INET_NTOA()` :把整型的 ip 转为地址
