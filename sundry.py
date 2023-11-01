"""
### 基金的收益归因分析可以分为
    --基于净值的分析RBSA
    --基于持仓的归因分析
  净值的归因分析属于Fama-French模型的延申,通常使用Sharpe提出的净值分解模型
  持仓的归因分析属于拥有持仓交易数据的基金管理人、FOF或者托管机构使用,常用的是Brinson模型

### 经典策略
双均线策略-期货
Dual Thrust-期货
R-breaker-期货
菲阿里四价-期货
均值回归策略-股票
小市值-股票
布林线举止回归-股票
alpha对冲-股票+期货
多因子选股-股票
网格交易-期货
指数增强-股票
跨品种套利-期货
日内回转交易-股票
做市商交易-期货
海龟交易发-期货
行业轮动-股票
机器学习-股票



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


### k8s网络模式
k8s-service:
 ClusterIP模式:
   serviceName.namespace.svc.cluster.local
 clusterIP=None的Headless Service:
   podName.serviceName.namespace.svc.cluster.local
   
  

pod开启hostNetwork为true
dnsPolicy使用ClusterFirstWithHostNet

 1.
kubectl rollout restart 
 2.
kubectl sacle deployment -n --replicas=0
kubectl sacle deployment -n --replicas=5

 3.
kubectl delete pod -n


### hash算法:MD5/SHA1/SHA256
MD5:128位散列值(16字节),快速,安全不足
SHA1:160位散列值(20字节)---40个十六进制数表示，一般,安全较高
SHA256:256散列值(32字节)---64个十六进制表示, 较慢,安全高

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

改天写个教程文档
### aerich tortoise-orm迁移工具 pip intall aerich 
1.aerich 初始化
  aerich init -t settings.TORTOISE_ORM  (--location ./migrations 默认)
2.aerich 初始化数据库
  aerich init-db   # 数据库中有相应的表了
3.重新生成迁移文件--一般是修改model后
  aerich migrate   # 迁移文件本质就是sql语句
4.执行迁移-表结构变更到数据库
  aerich upgrade 
5.回退上一个版本
  aerich downgrade 
6.查看历史迁移记录
  aerich history
7. 查看形成当前版本的迁移记录
  aericH heads

### python获取异常信息 
1. try

try
except Exception as e:
  print(e.)

2.sys.exc_info 和last_traceback

3.traceback信息均来源于traceback object对象,这个对象则是通过 sys.exc_info()来获取的
try：
    pass
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()

https://blog.csdn.net/yuanfate/article/details/119916008
https://zhuanlan.zhihu.com/p/614825330

(1: print_tb
  traceback.print_tb(exc_traceback limit=None,file=None)
(2: print_exception
  traceback.print_exception(exc_type,exc_value,exc_traceback,limit=None,file=sys.stdout)
  与print_tb相比,打印信息多了开头的 Traceback(most...)以及最后一行的异常类型和value信息
(3: print_exc 简化版的print_exception，省略了sys.exc_info()
  traceback.print_exc(limit=None,file=None,chain=True)
  traceback.print_exc(file=open("log.txt","w+")) # 将一擦会给你信息写入到文件中
  
(4:format_exc(limit=None,chain=True) 不打印,返回一个字符串,效果和print_exc一致
  print(traceback.format_exc())
  
(5:extract_tb(tb, limit=None)：从traceback对象中提取堆栈跟踪信息，
以元组的形式返回文件名、行号、函数名和源代码的文本行。limit指定提取堆栈的深度。  


### docker build 缓存cache
1.对大多数命令,如果命令未修改,将使用缓存中的版本(COPY 还会检测文件是否被修改)
2.某层layer无法应用缓存,则后续层都不能从层缓存加载
3.



### k8s调度
节点污点Taint: NoSchedule 一定不被
               PreferNoSchedule 尽量不被
               NoExecute:不会调度,并且还会驱逐
               
pod调度策略:
 1.requests/limits
 2.节点标签选择器
 3.节点亲和性:硬亲和和软亲和
 
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

### 绘图程序
https://app.diagrams.net/


### 四舍五入python
1.round
round(80.23456,2) # 80.23 返回无点数的四舍六入
python3中:round如果距离两边一样远，会保留到偶数的一边。比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。 
python2中:round如果距离两端一样远，则保留到离0远的一边。所以round(0.5)会近似到1，而round(-0.5)会近似到-1

浮点数精度问题
round(2.675, 2) 的结果，不论我们从python2还是3来看，结果都应该是2.68的，结果它偏偏是2.67，为什么？
机器中浮点数不一定精确表达,因为换算成一串1和0后可能是无限位数的,机器已经做了截断处理，
那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。这一点点就导致了它离2.67要更近一点点

2.math.ceil(x)将数字x向上舍入到最接近的整数
  math.floor(x)将数字向下舍入到最接近的整数
  
3.decimal.Decimal(传入字符串数字) 浮点数不准确
decimal.Decimal(str_num).quantize(decimal.Decimal("0.01"),rouding="ROUND_HALF_UP")
保留小数方式:
  ROUND_CEILING   总是趋向正无穷大方向取值
  ROUND_FLOOR     总是趋向负无穷大方向取值
  ROUND_DOWN      总是趋向0方向取值
  ROUND_UP        总是趋向0反方向取值
  ROUND_HALF_UP    四舍五入
  ROUND_HALF_DOWN   大于等于5向0方向取整,
  ROUND_HALF_EVEN   四舍六入双五
  ROUND_05UP        最后一位是0/5,
4."%.2f"%float(str_num) 四舍五入

#### yaml语法
直接写成多行字符串,第二行开始必须有一个单空格缩进
|保留换行符: "Foo\nBar\n"
>折叠换行符: "Foo Bar\n"
+表示保留文字块末尾的换行:
-表示删除字符串末尾的换行:


#### yum换源

yum install -y wget 
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
阿里的: wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
网易的：wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo

# 方案1
rm -f /var/lib/rpm/__db.00*  # 删除rpm数据文件
rpm --rebuilddb              # 重建rpm数据文件
# 方案2
rm -f /var/lib/rpm/.rpm.lock 
rm -f /var/lib/rpm/.dbenv.lock

yum clean all  # 清除缓存
yum makecache  # 重新建立缓存

yum install -y memcached  mongodb-org-tools libmemcached-devel

#### sed替换
sed -i 's/word/new_word/g' file_name

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
             书籍: 《深度学习与pytorch》
"""