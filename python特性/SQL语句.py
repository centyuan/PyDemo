# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/24 22:07
"""
mysql -h 主机名 -u root -p  # 连接mysql
show database;
show tables;
#选择数据库
use mysql;
#显示数据表的属性
show columns from user_table;
#显示数据表的详细索引信息
show index from user_table;
#显示数据库runoob所有表的信息
show table status from runoob;
show table status from runoob like 'run%'; #表名以run开头的表信息

#添加mysql用户
insert into user (host,user,password,select_priv,insert_priv,update_priv) values ('localhost','guest',password('guest123'),'Y','Y','Y');

#创建数据库
create database data_name;
#删除数据库
drop database data_name;
#mysql 数据类型：大致三种->数值 日期/时间 字符串(字符)

#创建数据表
create table 'run_tb'(
    'run_id',int unsigend auto_increment,
    'run_title',varchar(100) not null,
    'run_author',varchar(40) not null,
    'sub_data',date,
    primary key('run_id')
)engine=innodb default charset=utf-8;
#删除数据库
drop table run_tb;
#插入数据
insert into table_name(filed1,field2,field3) values(value1,value2,value3)
#查询数据
# order_by sub_date ASC 升序，DESC降序
select column_name1,column_name2 from table_name;
select * from table_name''
select * from run_tbl where run_author='菜鸟'''
update run_tb set run_title='学习', where run_id=3;
delete from run_tb where run_id=3;
select * from run_tb where run_title like '%com' #以com结尾
select * from run_tb where run_title like '%com%'# 保护com
#union 连接两个以上的select的语句的结果组合到一个结果集合中 distinct 删除结果集中重复的数据 all返回索引结果集
select country from websites union select country from apps order by conutry;
#使用group by将数据表进行分组，并统计每个name的多少条记录
select name,count(*) from em_tb group by name;
"""