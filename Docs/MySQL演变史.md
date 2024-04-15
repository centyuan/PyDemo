> title： MySQL演变史

### MySQL版本演变史

#### MySQL1.X

>MySQL 1.0在1995年发布，仅供内部使用

#### MySQL 3.X

>MySQL 3.11.1在1996年发布，直接跳过2.X版本，最早的稳定版本,
>
>**2000年**，ISAM升级为MyISAM存储引擎。同年，MySQL基于GPL协议开放源码

#### MySQL 4.X

>MySQL  4.0在2003年发布,集成了InnoDB存储引擎(该引擎由Innobase公司开发),支持事务、外键、行级锁等特性，以及全文搜索功能，适用于OLTP等高并发场景
>
>MySQL  4.1在2004年发布,增加了子查询，Unicode支持，预备语句等特性

#### **MySQL 5.X**

>MySQL 5.0在2005年发布，加入了存储过程、视图、触发器和游标的支持，同年，Oracle收购Innobase公司
>
>MySQL 5.1在2008年发布，加入了分区表，行级复制，事件调度
>
>MySQL 5.5在2010年发布
>
>```
>默认InnoDB plugin引擎。具有提交、回滚和crash恢复功能、ACID兼容。
>行级锁(一致性的非锁定读 MVCC)。
>表与索引存储在表空间、表大小无限制。
>支持dynamic(primary key缓存内存 避免主键查询引起的IO )与compressed(支持数据及索引压缩)行格式。
>InnoDB plugin文件格式Barracuda、支持表压缩、节约存储、提供内存命中率、truncate table速度更快。
>原InnoDB只有一个UndoSegment，最多支持1023的并发；现在有128个Segments，支持128K个并发（同样，解决高并发带来的事务回滚）。
>Innodb_thread_concurrency默认为0，线程并发数无限制，可根据具体应用设置最佳值。
>Innodb_io_capacity可以动态调整刷新脏页的数量，改善大批量更新时刷新脏页跟不上导致的性能下降问题。Default：200，跟硬盘的IOPS有关。
>充分利用CPU多核处理能力innodb_read_io_threads阈值：1-64innodb_write_io_threads 阈值：1-64根据数据库的读写比灵活设置，充分发挥多CPU、高性能存储设备的性能，不支持动态加载 。
>自适应刷新脏页
>热数据存活更久
>buffer pool多实例 ：innodb_buffer_pool_instances 参数增加innodb_buffer_pool实例个数，大大降低buffer pool的mutex争抢过热情况。
>Linux上实现异步IO
>重新支持组提交
>
>**稳定性提升**
>支持半同步Replication。
>增加Relay Log 自我修复功能。
>Crash recovery。
>引入红-黑树做插入排序的中间数据结构，时间复杂度大大降低，减少恢复时间。
>Thread Pool 分组排队 限流
>```
>
>MySQL 5.6在2013年发布，增加了全文索引，优化跟踪，性能改进
>
>```
>默认参数的改变
>Back_log  排队队列
>支持全文索引
>支持online DDL create,alter,drop
>可以在建表时指定表空间位置
>      create table external (x int unsigned not null primary key)data directory = '/volumes/external1/data';
>新增参数innodb_page_size可以设置page大小
>整合了memcached API，可以使用API来直接访问innodb表，并非SQL（减少SQL解析、查询优化代价）
>innodb只读事务，不需要设置TRX_ID字段，
>减少内部数据结构开销，减少read view
>仅仅非只读事务依然需要TRX_ID
>```
>
>MySQL 5.7在2015年发布
>
>```
>组复制 InnoDB Cluster 多源复制 增强半同步（AFTER_SYNC） 基于WRITESET的并行复制。 在线开启GTID复制。 在线设置复制过滤规则。 在线修改Buffer pool的大小。 在同一长度编码字节内，修改VARCHAR的大小只需修改表的元数据，无需创建临时表。 可设置NUMA架构的内存分配策略（innodb_numa_interleave）。 透明页压缩（Transparent Page Compression）。 UNDO表空间的自动回收。 查询优化器的重构和增强。 可查看当前正在执行的SQL的执行计
>```

#### MySQL8.X

>8.0版本在2018年发布，是目前最新的稳定版本 （截至我的知识更新为止）。
>
>引入了诸如窗口函数、递归SQL语句、角色、默认值、自动管理的Undo表空间、改进的JSON支持、字符集变为utf8mb4等特性。
>
>对索引和数据字典进行了重大改进，包括新增的数据字典，不再使用文件系统级别的元数据存储
