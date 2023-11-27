---
title: Docker Note
categories:
    - K8s和Docker
tags:
    - Docker
---

#### 基本命令

>创建容器
>```
>docker run ubuntu:15.10 /bin/echo "Hello world"
>以ubuntu15.10镜像创建一个新容器,然后在容器里执行 bin/echo "Hello world"(容器里面运行一个程序)，然后输出结果。
>ubuntu:15.10指定要运行的镜像，Docker首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
>```
>
>启动容器
>
>```
>docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"  --name my_ubunut
>
>docker run -i -t ubuntu:15.10 /bin/bash -p 8080:80
>-t:在新容器内指定一个伪终端或终端。
>-i:允许你对容器内的标准输入 (STDIN) 进行交互。
>-d:后台运行容器,并返回容器id
>-p:指定端口映射,格式为本机端口8080:容器端口80,将本机8080端口映射到容器80的端口
>-P:会随机映射一个端口到内部容器开放的网络端口
>-v:volume,绑定一个卷,格式为主机路径:容器路径
>```
>
>查看容器
>
>```
>docker ps -a
>docker start 2b1b7a428627 # 启动已停止运行的容器
>docker stop 2b1b7a428627  # 停止容器
>```
>
>查看日志
>
>```
>docker logs 2b1b7a428627/docker-name
>```
>
>进入容器
>
>```
>docker exec -ti 容器ID /bin/bash
>在使用 -d 参数时，容器启动后会进入后台。此时想要进入容器，可以通过以下指令进入：
>(1.docker attach
>docker attach 容器名称/ID
># 多个窗口同时attach到同一个容器的时候，所有窗口都会同步显示。当某个窗口因命令阻塞时，其他窗口也无法执行操作了。
>(2.docker exec
>docker exec -it 容器ID /bin/bash
># 推荐大家使用 docker exec 命令，因为此命令会退出容器终端，但不会导致容器的停止。
>(3.nsenter工具
>```
>
>打包容器为镜像
>
>```
>docker commit -m  "提示信息"   -a  "作者centyuan"   容器ID（可以简写）  image_name(镜像名称)
>-m:提示信息
>-a:作者
>docker push image_name # 上传镜像到hub.docker.com
>```
>
>镜像导入导出
>
>```
>docker save -o imagename.tar  nginx:latest
>docker save > imagename.tar nginx:latest
>docker export -o name.tar nginx:latest
>-o/>:表示输出到文件
>nginx:latest 表示源镜像名
>docker load  -i imagename.tar
>docker load  <  imagename.tar
>docker import nginx-test.tar nginx:imp
>-i和<表示从文件输入
>```
>
>文件拷贝
>
>```
>1宿主机拷贝到容器：
>sudo docker cp /home/centyuan/file(文件) or /home/centyuan/dir(目录) 容器name or ID:/root/
>2容器拷贝到宿主机：
>sudo docker cp mycontainer:/root/fiel.txt /home/centyuan/
>需要注意的是不管容器有没有启动，拷贝命令都会生效
>```
>
>others
>
>```
>获取一个新的镜像： docker pull ubuntu:13.10
>查找镜像：docker search httpd
>搜索镜像：docker search centos 
>获取镜像：docker pull registry.cn-hangzhou.aliyuncs.com/1hpc/centos
>查看本地所有镜像：docker images
>查看镜像id：docker images -q 
>删除镜像：docker rmi image_id 
>删除所有镜像：docker rmi $(docker images -q) 
>创建容器：docker run --name <container_name> centos:7,container_name是自己定义的容器名 
>查看所有容器：docker ps -a 
>查看运行容器：docker ps 
>查看容器id：docker ps -q
>进入容器：docker exec -it <container_id> bash 
>退出容器：exit 
>删除容器：docker rm <container_id> 
>删除所有容器：docker rm $(docker ps -aq) 
>端口映射：docker run -d -p 8080:80 hub.c.163.com/library/nginx
>启动/停止/重启容器：docker start/stop/restart <container_id>
>获取容器/镜像的元数据：docker inspect <container_id> 
>挂载数据卷：docker run -v host/machine/dir :container/path/dir --name volume_test_container centos:7
>启动mysql容器：docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=qwerasdf -d mysql:5.7 # 默认用户为root，密码qwerasdf
>容器连接：docker run --name some-app --link some-mysql:mysql -d application-that-uses-mysql  mysql容器启动后，其他容器就可以来连接使用了，方法如下：
>查看容器ip地址:docker inspect 容器名称/容器id | grep IPAddress   # docker会每个容器分配一个ip地址
>```
>
>

#### Dockerfile 

>用来构建镜像的文本文件
>
>**ADD和COPY区别**
>
>```
>都是复制文件/目录到容器
>ADD:
>	1.支持url远程复制(推送使用curl/wget,使用ADD会创建更多的镜像层),
>	2.压缩文件会自动解压,不太稳定,尽量使用COPY
>
>COPY:复制本地文件或目录到容器的文件系统
>	只能用于处理本地文件
>ADD命令在实践过程中，有很多功能问题出现，不稳定，官方建议尽可能使用COPY
>```
>
>**一般格式**
>
>```
>FROM centos:6.7  # 指定使用那个镜像
>MAINTAINER  Fisher "centyuan@outlook.com"
>RUN /bin/echo 'root:123456' | chpasswd  # RUN后面build时执行
>RUN useradd centyuan
>RUN /bin/echo 'centyuan:123456'| chpasswd
>RUN /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
>EXPOSE 22
>EXPOSR 80
>CMD /usr/sbin/sshd -D   # CMD后面docker run时执行
>ENTERYPOINT
>tail -f /dev/null       # 防止容器启动后,主线程命令执行完退出
>
># 使用Dockerfile构建镜像, . 为上下文路径 -t为镜像名字及标签,name:tag
>docker build -t centos:V3 .
>exec /bin/bash "$@"
>```



#### Docker-compose

>使用步骤:
>
>1.dockerfile定义应用程序环境镜像
>2.docker-compose.yml定义构成应用程序的服务
>3.docker-compose up启动并运行整个应用程序



#### Docker网络模式

>
>
>```
>1.host模式(--net=host):
>	共享主机的网络空间,使用主机的ip/端口,多个container使用相同的端口会发生端口冲突,没有独立ip,没有network namespace
>
>2.bridge模式(默认的网络模式):
>	没有--net参数默认网桥模式,通过veth-pair实现内部网卡和docker0网桥通信
>	eth0 <---> docker0(bridge) <-veth--ehto-> docker container
>	Network namespace--->veth<--->veth-br--->bridge--->etho(nat转换)--->公网
>	Docker server启动时,会在主机上创建一个名为docker0的虚拟网桥(类似于物理交换机),主机上的所有容器就通过虚拟网桥连在了一个二层网络中,
>
>3.container模式(--net=container:容器name/id):
>	新创建容器没有网卡和ip,而是和指定容器共享ip和端口范围
>
>4.none模式,封闭的网络环境
>
>5.overlay模式
>```
>
>Linux通过network namespace，把网络划分成一个个的独立空间，再通过虚拟网络设备将这些独立空间连接起来形成一个虚拟网络
>
>参考
>
>[手撕Docker网络1](https://zhuanlan.zhihu.com/p/199298498)
>[手撕Docker网络2](https://zhuanlan.zhihu.com/p/206512720)
>
>```
>Network Namespace:网络命名空间
>Linux Bridge:
>	Linux网桥设备，是Linux提供的一种虚拟网络设备，类似物理的网络交换机
>VETH(Virtual Ethernet):
>	虚拟网卡，总是成对出现，两个veth组成一个veth-pair
>	
>```
>
>启用bridge的路由功能连通主机和虚拟网络空间
>
>```
>1.给vbridge-0一个ip地址(该地址需要和虚拟网络空间在同一个子网)
>```



#### Docker文件结构

>container其实是一个进程,与普通进程不同，container通过隔离技术做到了container之间的互相隔离
>
>主要三个隔离核心技术: namespace, cgroups, rootfs
>
>**Namespace:**是Linux内核的一项功能,用于对内核资源进行分区，使一组进程看到一组资源
>
>主要以下几种:
>
>```
>IPC: SystemV IPC（信号量,消息队列和共享内存)和POSIX message queues
>Network: 网络设备，网络栈，端口
>Mount: 文件挂载点
>PID: 进程编号
>User: User 和Group IDs
>UTS: 主机名和NIS域名
>Cgroup: cgroup的根目录
>```
>
>**Cgroups:**control groups，是Linux内核提供的一种可以限制，记录，隔离进程组(process groups)所使用物理资源的机制，主要功能有：资源限制(Resource limiting)，优先级分配(Prioritization)，资源统计（Accounting)，进程控制（Control）
>
>[Cgroups](https://zhuanlan.zhihu.com/p/271808319)
>
>**Rootfs:** 是 docker 容器在启动时**内部进程可见的文件系统**，即 docker 容器的根目录
>
>**overlayFS:**
>
>```
>docker deamon会利用联合挂载技术（Union Mount）在已有的rootfs上再挂一个读写层,overlayFS则是联合挂载技术的一种实现
>```
>
>一个容器完整的层应由三个部分组成:
>
>```
>1.镜像层：也称为rootfs，提供容器启动的文件系统。rootfs也就是我们上一节中分析的image文件。镜像层属于roLayer。
>2.init层： 用于修改容器中一些文件如/etc/hostname，/etc/hosts，/etc/resolv.conf等。init层属于mountedLayer。
>3.容器层：使用联合挂载统一给用户提供的可读写目录。容器层属于mountedLayer
>```
>
>



