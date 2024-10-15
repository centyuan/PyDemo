>title: Note

#### URL规范

>1. 不用大写 （强制）
>2. 用中杠-不用下杠_（强制）
>3. 参数列表要encode，编码使用utf-8（强制）
>4. URI中的名词表示资源集合，使用复数形式。（建议）
>5. 增加版本号（建议）

#### 双因子认证

> 认证因素按计算采用的近似顺序列举如下ƒ
> 1. 认知因素(用户知道的事物,密码/PIN码)
> 2.  持有物因素指用户拥有的东西，比如身份证，安全令牌，智能手机或其它移动设备。
> 3.  特征因素，更多时候被称为生物识别因素，是用户自身固有的特性。这些可能是从物理特征映射出来个人属性，比如通过指纹阅读器认证的指纹；其它特征因素还包括面部识别和语音识别。此外还包括一些行为特征，比如击键力度，步态或语音模式。
> 4.  位置因素，通常是指尝试认证时所处的位置，可以特定位置的特定设备来强制限定认证，更常见的方式是跟踪认证来源的 IP 地址或来源于移动电话或其他设备（如GPS数据）的地理信息。
> 5.  时间因素限制用户在特定的时间窗口内认证登录，并在该时间之外限制对系统的访问。
>
> 例如：短信验证、微信或者QQ授权验证、USB令牌、OTP令牌等等。举例1：当你进入公司时，必须打卡（你在公司的身份证件）+指纹验证，这就是双因子认证机制举例2：登录某web网站，输入账号密码之后，还要再输入接收到的短信验证码，这也是双因子认证机制举例3：你在一台新的设备上第一次登录你的微信，除了输入账号密码，还要有一个确认好友的步骤，即在微信给你的N个头像中正确的选出你的好友，或者在原设备登录中的微信，扫描现在微信的授权登录二维码。以上二选其一即可在新设备上登录。



https://cloud.tencent.com/developer/article/2370270

####  RBAC(Role-Based Access Control)

>基于角色的访问控制
>
>判断请求者在某些条件下是否对请求数据具备某个操作API的能力，一个用户通过绑定角色,具备对一些数据的操作能力
>
>(但在复杂的权限管控场景中,RBAC显得力不从心)
>
>- 用户在晚上不能访问这个系统，但是白天可以
>- 用户只能在内网对订单具备修改权限，而在外网就只有查看权限
>
>**实现步骤**
>
>1.设计角色和权限的层次结构
>
>2.将用户分配到合适的角色
>
>3.关联权限到角色,形成访问控制矩阵
>
>4.通过会话管理机制维护权限的有效性
>
>用户表/角色表/菜单权限表
>
>系统登录日志表/用户和角色关联/角色和菜单关联
>
>
>
>

#### ABAC（Attribute Based Access Control）

>基于属性的权限访问控制
>
>



#### NGNC(下一代访问控制)

>基于这样一个假设,你可以用一个图来表示你要保护的系统,这个图代表了你要保护的资源和你的组织结构,



#### 匹配方式

```

1. str in str
2. re.findall("词库",input)
3. 三方库thefuzz 
https://www.jianshu.com/p/ed22a82b45d1
https://blog.csdn.net/u010454729/article/details/124231419
"""
两个字符串之间的Levenshtein Distance莱文斯坦距离指的是将一个字符串变为另一个字符串需要进行编辑操作最少的次数。其中，允许的编辑操作有以下三种。不难看出其可用于衡量两个字符串之间的差异，故被广泛应用于拼写纠错检查、DNA分析、语音识别等领域
「替换」：将一个字符替换成另一个字符
「插入」：插入一个字符
「删除」：删除一个字符
ratio计算关键原理：
源代码：/opt/anaconda3/lib/python3.8/difflib.py

解释：T分别是两个序列的元素长度和，M是匹配到的个数。
abc、a：匹配了a，故结果是(2*1)/(3+1) = 0.5
aabc、a：也只匹配了a，虽然前面有两个a，但可以理解为后面匹配到了的a用掉了，故(2*1)/(4+1)=0.4
aabc、aa：匹配到了第一个a、第二个a，共两个，故(2*2)/(4+2)=2/3



#### 文本文件和字符串之间的差异
1.标准类库: diffib 
from difflib import SequenceMatcher
SequenceMatcher(None,"hello world","hi world").ratio()

2.thefuz 四种模糊匹配计算方式：依据 Levenshtein Distance 算法，计算两个序列之间的差异
from thefuzz  import fuzz
from thefuzz  import process 
简单匹配fuzz.ratio :直接调用SequenceMatcher
非完全匹配fuzz.partial_ratio: 
做了简单的处理。再调用Ratio
处理：将两个字符串空格分割开来，得到两个集合a、b。其中
a&b排序拼接在一起得到sorted_sect，交集
(a-b、a&b)排序拼接一起得到combined_1to2。差集+交集
(b-a、a&b)排序拼接一起combined_2to1。另外一个差集+交集
计算ratio(sorted_sect)、ratio(combined_1to2)、ratio(combined_2to1)三者之间的最大值。
忽略顺序匹配fuzz.token_sort_ratio: 做了简单的处理。再调用Ratio
去重子集匹配fuzz.token_set_ratio:  做了简单的处理。再调用Ratio
非完全忽略顺序匹配fuzz.partial_token_sort_ratio: 
非完全去重子集匹配fuzz.partial_token_set_ratio
choices = ["河南省", "郑州市", "湖北省", "武汉市"]
process.extract("郑州", choices, limit=2)



#### ssh代理
ssh   gxac@192.168.100.197 -fNL  0.0.0.0:40122:20.120.47.211:22
Flyingnets@2023
##### Linux登录时:
首先启动/etc/profile ,在启动用户目录下:~/.bash_profile,~/.bash_login, ~/.profile,如果~/.bash_profile文件存在的话,一般还会执行~/.bashrc
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi 
执行顺序:/etc/profile→ (~/.bash_profile | ~/.bash_login | ~/.profile)→~/.bashrc →/etc/bashrc
```

```

opentelemetry-instrument uvicorn gptserver:app  --host 0.0.0.0 --port 8081 --http httptools --loop uvloop  --proxy-headers --forwarded-allow-ips='*' --no-server-header
./configure --enable-optimizations --with-openssl=/usr/local/openssl --prefix=/usr/local/python-3.10



gunicorn gptserver:app  -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8888 -t 300   --daemon 


gunicron text_embedding_in
PROCESS=`ps -ef | grep gunicorn | grep -v grep  | awk '{print $2}'`
for i in $PROCESS
do
    echo "kill the gunicorn process  ${i} "
    sudo kill -9 ${i}
done
nohup python3 app.py > flask.log 2>&1 &
https://192.168.100.197/#/
hl:a.123123


```

#### Python在存储字符串的时候如何节省内存

Python3开始使用Unicode表示str,使用Unicode但却不是utf-8,Unicode的每个字符最大可以占到4字节,从内存角度来说，这中编码有时会比较昂贵

为了减少内存消耗并且提高性能,Python内部使用了三种编码方式表示Unicode

Latin-1编码: 每个字符一字节

UCS2编码: 每个字符两字节

UCS4编码: 每个字符四字节

无论是索引还是切片,以及计算长度，都是基于字符的，更符合人类的思维习惯



#### 字符串检索匹配算法

>Levenshtein Distance莱文斯坦距离算法
>
>```
>两个字符串之间的莱文斯坦距离指的是，将一个字符串变为另一个字符串需要进行编辑操作最少的次数，允许的编辑操作(替换，插入，删除)，广泛用于瓶邪纠错，DNA分析
>```
>
>
>
>

BF(Brute Force):暴力匹配

KMP(Knuth-Morris-Pratt):对BF的改进

BM(Boyer-Moore):

Horspool():是BM算法简化之后的版本,时间复杂度没变,只是更好理解了

CPython 中 str.find() 的实现主要结合了 BM 和 horspool 两种算法





#### Fastgpt修改logo/Title

>**修改title**
>
>vi projects/app/.next/static/chunks/2844-c4c0d1b210d6bf33.js
>:J.JU.systemTitle
>
>**去掉github和帮助文档**
>
>vi projects/app/.next/static/chunks/pages/_app-848999fdd7434aff.js
>
>chatbotUrl
>
>**去掉用户页帮助文档**
>
>grep -rn "Help Document" .
>
>vi projects/app/.next/static/chunks/5440-45aafab60666d17e.js
>
>**去掉登录页**
>
>vi projects/app/.next/static/chunks/pages/login-9479ea369f2c072a.js
>
>**去掉免责声明**
>
>vi chunks/2844-c4c0d1b210d6bf33.js



#### Fastgpt 新增账号

```
db.users.insert({
    status:"active",
    username:"testyuan",
    password:"de6320287d71d412dbd1f69a29985647d8db62cc53ba3ad417bc33bd48e75307",
    avatar:"/icon/human.svg",
    balance:200000,
    promotionRate: 20,
    timezone: "Asia/Shanghai"  
})

db.team.members.insert({
    teamId: ObjectId("65a53ab2dead493c3e2475b6"),
    userId: ObjectId("65a89da76dd0ad698fdc9a58"),
    name: "Owner",
    role: "owner",
    status:"active",
    defaultTeam:true,
    __v:0
})
db.team.members.update({"userId":ObjectId("66471a73b41e6af5b7796a84")},{$set:{"teamId":ObjectId("65a53ab2dead493c3e2475b6")}})
db.teams.insert({
   name: "test team",
   ownerId: ObjectId(),
   avatar: "/icon/logo.svg",
   balance: 99999999,
   maxSize: 1,
   __v: 0
})

db.team.members.update({"userId":ObjectId("65a89da76dd0ad698fdc9a58")},{$set:{"teamId":ObjectId("65a8a9bb6dd0ad698fdc9a5c")}})

```

```

docker run -d --name bge_reranker -p 6006:6006 -e ACCESS_TOKEN=sk-xx
luanshaotong/reranker:v0.1
docker run -d --name bge_reranker -p 6006:6006 luanshaotong/reranker:v0.1
$env:SQL_DSN="cent:123456@tcp(192.168.100.208:3306)/one_api"
$env:REDIS_CONN_STRING="redis://192.168.100.208:6379"
$env:SYNC_FREQUENCY=60
$env:PORT=9999
mysql://root:1qaz%40WSX@192.168.100.208:3306/flygpt

mysqldump -usoc-user -pSocuser@0511 -t -T /var/lib/mysql-files/ temp loophole_cnnvd --where="id<200"  --fields-terminated-by=',' --fields-enclosed-by='\"'
-t: 不写表的创建信息
--fields-terminated-by:输出文件中的字段以给定的字符串结尾
--fields-enclosed-by:输出文件中的字段用给定的字符括起来。


```



#### 如何脱敏有效

>https://cloud.tencent.com/developer/article/1636078
>
>https://blog.csdn.net/qq_41219586/article/details/125618681



#### 排序算法

>https://blog.csdn.net/alzzw/article/details/98100378
>
>比较类排序: 通过比较来决定元素顺序,时间复杂度不能突破O(nlogn),称为非线性时间比较类排序
>
>​	交换排序:  冒泡排序(n平方-稳定)/快速排序(分而治之)
>
>​	插入排序: 简单插入排序(n平方-稳定)/希尔排序(n平方-不稳定:针对插入排序的改进)
>
>​	选择排序: 简单选择排序/堆排序(nlogn)
>
>​	归并排序: 二路归并排序/多路归并排序(nlogn)
>
>​	n平方: 冒泡/插入/选择(**只有选择不稳定**)
>
>​        nlogn: 归并/堆排序/快速排序(可以做到nlogn) **只有归并是稳定的**
>
>​	稳定的选归并,空间复杂度低的选堆排
>
>非比较排序: 
>
>​	桶排序/计数排序/基数排序
>
>​	**桶排序**: 数据要求苛刻(数据容易划分到m个桶中,且数据能均匀分布到各个桶中),适合外部排序(数据存储在磁盘中)数据量大,内存有限的,不均匀的桶在继续划分
>
>​	**计数排序**:是桶排序的一种特殊情况
>
>​	**基数排序**:

​	

#### 多租户

>主流的多租户方案通常三种
>
>```
>1.独立数据库，每个租户单独的数据库，用户数据隔离级别最高，安全性最好，成本最高
>2.共享数据库，共享同一个数据库，但每个租户的schema不同，用户数据隔离级别中等
>3.共享数据库和数据结构，所有租户共享同一个数据库和表，表中根据TenantId字段区分，用户数据隔离级别低，但是成本最低
>```



#### 镜像版本选择

>大小
>python:3.7 > centos:8 > python:3.7-slim > amazonlinux:latest > debian:buster > ubuntu:18.04 > alpine:latest

**传统的Linux分支(Ubuntu TLS,CentOS,Debian)**

**Docker-Compose**

>```text
>sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
>```

**Docker官方的Python镜像**

>alpine<slim<(buster/stretch/jessie)<full official image(python:3.11.3)
>
>buster/stretch/jessie都是基于debian的
>
>```
>buster:Debian 10
>stretch:Debian 9
>jessie:Debian 8
>```

**云计算上的 Linux 镜像 – Amazon Linux 2**

**Alpine 镜像**

>Alpine Linux
>
>GNU C Library(glibc)换成了迷你版的C标准款musl



#### Other

**ASSA**

>export SQL_DSN='root:1qaz@WSX@tcp(192.168.100.208:3306)/ai_gate'
>
>测试环境:
>
>```
>export SQL_DSN='root:1qaz@WSX@tcp(192.168.100.208:3306)/ai_gate_test'
>export PORT=8888
>export SESSION_SECRET=abc123
>export REDIS_CONN_STRING="redis://192.168.100.208:6379"
>export EXP_TIME=be28a46a24a277f94a31fe36ece5c062
>```
>
>```
>go build -ldflags "-s -w -X 'github.com/songquanpeng/one-api/common.Version=$(cat VERSION)' -extldflags '-static'" -o one-api
>go build -ldflags "-s -w  -extldflags '-static'" -o ai-gate
>go build -ldflags "-s -w" -o ai-gate
>
>-ldflags: 用于设置链接器的选项，编译的最后一步就是链接，
>	-s: 去掉符号表信息
>-w: 去掉调试信息
>都是为了减小最终可执行文件的大小
>-extldflag: 设置外部链接器的选项，‘-statis',生成的可执行文件不依赖于系统的任何动态链接库
>
>nohup /home/devpmp/ai-gate/ai-gate >ai-gate.log &2>1 & 
>-w: 禁止生成Debug信息,使用该项后,无法使用gdb进行调试
>-s: 禁用符号表
>-X：可以在编译时定义指定包中string变量值
>-extldflags '-static':静态链接
>```
>

````
可以使用 go mod 来管理模块缓存，常用命令如下：
go mod tidy：用来更新 go.mod 文件以确保所有的依赖包都被准确地记录下来，会添加缺失的模块，删除无用的模块。
go mod download：下载 go.mod 文件中指定的所有依赖包并缓存到本地。
go mod verify：检查依赖的完整性和正确性，会检查 go.sum 文件中的每个依赖是否存在，有没有被修改。
go mod vendor：将依赖项复制到项目的 vendor 目录下，这样可以不使用模块缓存进行构建。
````

>```
>python3 -m nuitka --standalone --show-memory --show-progress --nofollow-imports --include-package=uvicorn --include-package=click --include-package=h11 --include-package=starlette --include-package=fastapi --output-dir=o main.py
>--output-filename
>```
>
>```
>python3 -m nuitka  --show-progress   --nofollow-imports --include-package=gptserver  --onefile gptserver/main.py
>```

```
pyinstaller --hidden-import tortoise.backends.mysql --hidden-import aiomysql  --hidden-import asyncmy.constants --hidden-import aerich   --hidden-import aerich  --hidden-import nb_log  --hidden-import nb_log_config --onefile gptserver/main.py
```





**NOTE**

>Python打包: https://www.v2ex.com/t/970031
>
>FastAPI 验证码: https://github.com/JohnDoe1996/fastAPI-vue/blob/main/backend/app/utils/captcha_code.py



FastAPI的中间件和依赖有什么区别

>中间件：主要用于对请求和响应作出一些额外的操作，例如身份验证/记录日志/错误处理
>
>依赖：主要用于解耦和管理应用程序的各种依赖关系，如数据库连接,依赖项配置,使得代码更加模块化,可重用,易于测试

Python常用的异步库

>Starlette-用于构建高性能服务的轻量级ASGI框架/工具包。
>
>uvicorn-快如闪电的ASGI服务器。
>
>FastAPI-基于类型提示的非常高性能的Python 3.6+ API框架。由Starlette和Pydantic提供支持。
>
>aiokafka -Apache Kafka的客户端。
>
>asyncpg-适用于Python / asyncio的快速PostgreSQL数据库客户端库
>
>aiomysql-用于访问MySQL数据库的库
>
>aioredis - aio-libs Redis客户端（PEP 3156）
>
>httpx-具有请求兼容API的Python 3异步HTTP客户端。
>
>pytest-asyncio-对异步的Pytest支持。
>
>uvloop-在libuv之上的asyncio事件循环的超快速实现。



#### 面试

>一:八股文
>python各版本区别:
>python基础知识:
>框架：Django,FastApi,REST,Celery:
>ORM:django orm,Sqlalchemy,Tortoise 
>数据库mysql,postgresql,redis,mongodb,Elasticsearch:
>
>数据库分类:
>关系型数据库:
> Mysql Postgresql Oracle Sqlserver Sqllite
>非关系型数据库: 
> 键值(key-value)数据库: Redis Memcached
> 列数据库: ClickHouse,HBase
> 面向文档数据库; MongoDB(数据以json文档形式存储)
> 搜索数据库:  Elasticsearch
>  图数据库: Neo4J
>      时序数据库: InfluxDB,Prometheus
> 消息中间件RabbitMQ,Kafka:
>     容器docker k8s：
>     构建工具Pdm，Makefile
>     RPC: gRPC,Nameko
>     CI/CD:Gitlab CI
>     Airflow/Ansible
>     
>
>二:算法
>
>
>三:AI
>从模型训练到部署
>
>1.模型训练(数据预处理,特征提取,模型调参)
>2.模型评估与验证(交叉验证,ROC曲线,混淆矩阵)
>3.模型部署
>离线预测: 定时收集数据并预测，将预测结果写入数据库
>模型内嵌于应用: 模型更新涉及整个应用的更新
>以API形式发布: 
>实时推行模型数据:
>
>项目上遇到的问题和难点：
>First:
>  用户管理模块,类似分销系统,用户之间有层级代理关系,设计用户的层级之间关系管理(代理的变线,修改上下级关系等)，返点计算
>  用户展开关系就是一个多叉树,对这个表主要在读筛选上，写的操作不会太多,考虑计算上级返点需要查找所有下线，所以采用闭包表
>  用户表设计:
>  只记录直属父子节点关系
>如采用领接表,但是在查询所有子节点去计算返点，分红时候,递归去查询每个子节点，效率很慢
>采用闭包表:记录祖先节点和所有后代节点的上下级关系,查找所有下线只需要筛选祖先节点就行了
>采用路径枚举: 记录祖先节点到子节点的路径,可以快速定位直属上下级
>
>Second:
>CTF实战平台：
>  防火墙策略分发优化:同步多线程改成异步分发(使用celery)
>有个flag提交接口(差不多两千行代码),改成六七百行
>
>辅助侦查平台：
>  对页面关键信息抓取(如手机号/邮箱/QQ /微信/姓名等),对 ajax 请求问题，提出采用 Selenium headless 模式解决方式
>部署 APK 分析服务,采用了 MobSF 实现方式,由于开源版本没有手机号和邮箱信息采集，后在源码分析时候，加入了手机号和邮箱的功能
>
>Third:
>湘财:
>登录接口获取持仓信息和获取实盘资金
>   Alpha digital:
>   CNE7模型数据上传,采用Cronjob定时上传,加入重试和告警处理(kafka连接成功，但是消息发送失败)
>   
>   vscode Python相关插件
>Python：Vscode团队开发（代码补全，代码检查，代码格式）
>Python Docstring Generator： 生成docstring代码片段
>Python Type hint： 类型提示
>     Python Preview： 可视化调试过程
>    ms-python.black-formatter：black
>charliermarsh.ruff：ruff
>其他:
>     Github Theme
>office viewer:即时Markdown
>Codelf： 变量命名
>Regex Previewer：正在表达式预览
>
>    **B端项目**
>
>    东方证券
>中信建投
>华夏基金
>海通证券
>中金财富
>湘财证券
>bigalphacapture.com
>admin Z—gLm8yzGrX4GrK
>alphadig.csc108.com/login
>kbtest_whliao Abcd1234!
>bigquant.com
>bigquant !%BBQ2023@March
>bigquant.xcsc.com
>130015806 738152
>Dcoker
>K8s
>Tortoise
>FastAPI
>Pydantic
>Pandas 
>Cython
>Nuitka
>Nameko
>Grpc
>Gitlab CI/CD
>Airflow
>Ansible
>ray
>rabbitmq
>Makefile
>Vscode
>
>中信建投 Alpha Digital Lab 系统
>中信建投 Alpha caputre 系统
>湘财量化交易平台
>东方证券期货资金管理系统


