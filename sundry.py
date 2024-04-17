"""

### 按行或列删除数据
df.drop()
数:
tables:接受str/array,代表要删除的行或列的标签
 按行添加数据  
df.loc[len(df)]=["11","11"]
### 
read_csv(index_col=0)
to_csv(index=False)
### pd设置显示行数列数
pd.set_option("display.max_columns",500)
pd.set_optino("display.max_rows",500)


### ipv4地址段
A类地址：
  0.0.0.0-127.255.255.255
  保留地址：
     127.0.0.0-127.255.255.255 用于做循环测试用
  私有地址：
     10.0.0.0-10.255.255.255
B类地址：
  128.0.0.0-191.255.255.255
  保留地址：
      169.254.0.0-169.254.255.255 当ip地址是自动获取ip地址，而没有找到可用的DHCP服务，将从中临时获得一个ip地址
  私有地址：
      172.16.0.0-172.31.255.255
C类地址：
  192.0.0.0-223.225.255.255
  私有地址：
      192.168.0.0-192.168.255.255


block:存储文件数据,8个扇区组成一个块(一个扇区512字节,是硬盘最小存储单位),是文件存取的最小单位
inode: 索引节点,存储文件元信息(文件权限rwx,文件的属主,属组,文件大小,时间戳) stat可以查看inode信息
   文件名存放在文件目录,目录也是一个文件,每个inode都有一个号,系统通过inode号识别不同文件
   
inode也会消耗空间,一个一般是128或256字节
df -i 可以查看每个硬盘分区的inode总数和已使用量

### linux环境变量
etc/profile 系统级对所有用户有效,为系统所有用户设置环境变量,用户第一个登录时,该文件被执行,只执行一次并从/etc/profile.d目录的配置文件中搜索shell位置
etc/bashrc  系统级对所有用户有效,为每一个运行bash shell的用户执行此文件,没打开一个terminal都会执行bashrc
/.bash_profile  用户级,执行一次
/.bashrc        用户级,打开terminal就执行
/.bash_logout
etc/profile -> (~/.bash_profile | ~/.bash_login | ~/.profile) -> ~/.bashrc  -> /etc/bashrc

### window查看端口占用
netstat -ano | findtsr "8000"
tasklist | findstr
taskkill /T /F /PID 9088

### 查看端口开放
  wget ip:port 
  curl -v ip:port
  telnet ip port
  ssh -v -p port root@ip
  ssh -v ip -p port 
  nc -zv ip port 

  netstat -lntp # 
     -l 列出所有监听端口
     -n 以数字形式显示地址和端口
     -t 列出tcp协议的连接  -u 列出所有udp的连接 -a 列出所有连接
     -p 显示占用该端口的进程
  lsof -i:port

### 
chrome窗口输入badidea或thisisunsafe 告诉chrome跳过证书认证c


 
### 几种数据
jay/feather/hdf5/pickle/parquet/csv

feather/parquet:有数据冗余排除算法,可以节省空间
pickle:实现二进制协议,用于序列化和反序列化python对象结构
pickle不可以保存lambda函数,序列化对象,dill可以保存
字符串类型:
  save速度:feather>parquet>hdf5>pickle/csv>SQL
  read速度:feather>parquet>pickle>hdf5>csv>SQL
  size大小:parquet<feather<csv<SQL<pickle<hdf5
纯数字类型
  save 速度排序: pkl > ftr > hdf5 > pqt > csv
  read 速度排序: pkl > ftr > pqt > hdf5 >csv
  size 大小排序：ftr < pqt < pkl < hdf5 < csv


#### yaml语法
直接写成多行字符串,第二行开始必须有一个单空格缩进
|保留换行符: "Foo\nBar\n"
>折叠换行符: "Foo Bar\n"
+表示保留文字块末尾的换行:
-表示删除字符串末尾的换行:



### mysql 
DDL: Data Definition Language
DDL允许用户定义数据，即创建表、删除表、修改表结构这些操作。通常,DDL由数据库管理员执行
DML: Data Manipulation Language
DML为用户提供添加、删除、更新数据的能力，这些是应用程序对数据库的日常操作。
DQL: Data Query Language
DQL允许用户查询数据，这也是通常最频繁的数据库日常操作。




python相关思考:
https://www.bilibili.com/video/BV13d4y1b7md/?spm_id_from=333.788
基础知识:
1.高等数学/线性代数/概率论基础(张宇/汤家凤)
高等数学-宋浩:https://www.bilibili.com/video/BV1Eb411u7Fw/?spm_id_from=333.337.search-card.all.click
线性代数-宋浩:https://www.bilibili.com/video/BV1aW411Q7x1/?spm_id_from=333.337.search-card.all.click
概率论基础-宋浩:https://www.bilibili.com/video/BV1ot411y7mU/?spm_id_from=333.337.search-card.all.click
2.python
        视频: 小甲鱼,
       书籍:《Python编程从入门到实践第3版》/《利用python进行数据分析第三版》
3.机器学习
       视频: 网易版吴恩达机器学习/吴恩达Deeplearning/李宏毅老师机器学习
        https://www.bilibili.com/video/BV1Pa411X76s/?spm_id_from=333.337.search-card.all.click
       书籍:
           机器学习:《机器学习--西瓜书》/《机器学习精讲》/《机器学习实战》
            深度学习:《神经网络与深度学习》/《深度学习》
4.机器学习框架
        pytorch:
             视频: pytorch龙曲良
             书籍: 《深度学习与pytorch》,《python机器学习:基于Pytorch和Scikit-learn》
"""


### python安全问题
"""
assert:
  不要使用语句来防止用户不能访问的代码段

xml/pickle解析:



"""
