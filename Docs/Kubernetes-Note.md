---
title: Kubernetes Note
categories:
   - K8s和Docker
tags: 
   - K8s
---
#### 架构图

#### 核心技术概念

##### Mater

> 指集群的控制节点,运行着一组关键进程
>
> ```
> Kube-apiserver: 提供了HTTP Rest接口服务，是Kubernetes所有资源的增删改查等操作的唯一入口
> Kube-controller-manager: Kubernetes所有资源对象的自动化控制中心，保证资源处于预期的状态
> Kube-scheduler: 资源调度，负责决定将Pod放到那个Node上
> Etcd: Kubernetes所有资源对象数据都保存在etcd中
> ```

##### Node

> ```
> kubelet: 负责维护容器的生命周期，同时也负责 Volume 和网络的管理 
> kube-proxy:负责为 Service 提供 cluster 内部的服务发现和负载均衡(实质操作防火墙规则(iptables/ipvs)来实现pod的映射) 
> Container Runtime:负责镜像管理以及 Pod 和容器的真正运行(Kubernetes 支持多个容器运行环境: Docker、 containerd、cri-o、 rktlet 以及任何实现 Kubernetes CRI(容器运行环境接口)) 可以在运行期间动态加入kubernetes集群,一加入集群，Node上的kubelet进程会定时向Master节点汇报自身情报(如操作系统信息，Docker版本，CPU内存情况，Pod信息)，Node超时不上报信息，会被Master判定为“失联",Node被标记为Not Ready，随后Master触发”工作负载大转移"
> ```



##### Pod

> 最基本的概念,每个Pod都有一个特殊容器Pause，还包含一个或多个紧密相关的用户业务容器，Pod里的多个业务容器共享Pause容器的IP和Volume,每个Pod都有一个Pod IP,且集群内任意两个Pod可以通过Pod IP通信
>
> **Endpoint**: 	PodIP+ContainerPort
>
> `分类`:普通Pod和静态Pod(不会存放在Etcd里，而是存放在Node的一个具体文件中，并只在此Node上启动运行)
>
> `资源限制`:
>
> ```
> spec:
> containers:
> -name: db
>  image: mysql
>    resources: 
>       requests:    # 资源最小申请
>         memory: "64Mi"
>         cpu: "250m"
>       limits:      # 资源最大申请
>         memory: "120Mi"
>         cpu: "500m" # m表示千分之一CPU,500m就是0.5个CPU
>    ```
> ```

##### Label

> **Label Selector**
>
> ```
> 基于等式的(Equality-based):
>  name=redis-slave 匹配所有具有标签name=redis-slave的资源对象
>  env!=production 匹配所有不具有标签env=production的资源对象
> 基于集合的(Set-based): 
>  name in (redis-master,redis-slave) 匹配所有具有标签name=redis-master或name=redis-slave的资源对象
>  name not in (php-frontend) 匹配所有不具有标签name=php-fronted的资源对象
> 多个表达式之间用“,”进行分割,关系是AND
>  name=redis-slave,env!=production
> ```

##### RC

> Kubernetes最核心的概念，管理Pod的副本数量
>
> ```
> apiVersion: v1
> kind: ReplicationController
> metadata:
>  name: frontend
> spec:
>  replicas: 1
>  selector: 
>    tier: frontend
>  template:
>    metadata:
>      labels:
>        app: app-demo
>        tier: frontend
>    spec:
>      containers:
>       - name: tomcat-demo
>         image: tomcat
>         imagePullPolicy: IfNotPresent
>         env:
>          - name: GET_HOSTS_FROM
>            value: dns
>         ports:
>          - containerPort: 80
> ```
>
> `手动scale`
>
> ```
> kubectl scale rc redis-slave --replicas=3
> ```
>
> 通过RC的机制，Kubernetes很容易实现滚动升级(Rolling Update)

##### RS

> Kubernetes1.2后支持Replication Set，下一代的RC，最大的区别RS支持基于集合的Label Selector(Set-based selector),RC只支持基于等式的Label Selector(Equality-based selector)

##### Deployment

> Kubernetes1.2后引入的概念,是为了更好的解决Pod的编排问题，相对于RC的一个最大升级是我们可以随时知道当前Pod"部署"进度
>
> `例子`
>
> ```
> apiVersion: extensions/v1beta1
> kind: Deployment
> metadata:
>  name: frontend
> spec:
>  replicas: 1
>  selector:
>    matchLabels:
>      tier: frontend
>    matchExpressions:
>      - {key: tier, operator: In, values: [frontend]}
>  template:
>    metadata:
>      labels:
>        app: app-demo
>        tier: frontend
>    spec:
>      containers:
>       - name: tomcat-demo
>         image: tomcat
>         imagePullPolicy: IfNotPresent
>         ports:
>          - containerPort: 8080
>        
> ```
>
> `创建查看`
>
> ```
> kubectl create -f tomcat-deployment.yaml
> kubectl get deployments 
> kubectl get rs
> ```

##### HPA

> Horizontal Pod Autoscalinig Pod横向自动扩容，与RC,Deployment一样属于Kubernetes的资源对象，通过追踪分析所有RC控制的所有Pod的负载变化，来针对性调整目标Pod的副本数
>
> **Pod负载度量标准**
>
> ```
> CPUUtilizationPercentage
> 应用程序自定义的度量指标，比如服务在每秒内的相应的请求数(TPC或QPS)
> ```

##### Service

> 每个Service就是微服务架构中的一个"微服务",定义了一个服务的访问入口地址
>
> Service一旦创建，Kubernetes就会自动为它分配一个可用Cluster IP,在Service的整个生命周期,Cluster IP不会发生改变
>
> 服务发现: 用Service Name与Service Cluster IP做一个DNS域名映射
>
> `例子`
>
> ```
> apiVersion: v1
> kind: Service
> metadata:
>  name: tomcat-service
> spec: 
>  ports:
>   - name: service-port
>     port: 8080         # 定义了Service的虚端口
>     targetPort: 8080   # 容器所暴露EXPOSE
>   - name: shutdown-port
>     port: 8005
>     targetPort: 8005
>  selector:
>    tier: frontend
> ```
>
> `查看Endpoint`
>
> ```
> kubectl get endpoints
> ```
>
> `查看svc`
>
> ```
> kubectl get svc tomcat-service -o yaml
>
> ```
>
> ##### 三种IP
>
>> **Node IP:** Node节点的IP地址
>> 是Kubernetes集群中每个节点的物理网卡的IP地址
>>
>> **Pod IP:**
>>
>>     Docker Engine 根据docker0网桥的ip地址段进行分配的，通常是一个虚拟的二层网络
>>
>> **Cluster IP:**
>>
>>     Service的虚拟IP,无法被Ping,没有一个“实体网络对象"来响应，Cluster IP 只能结合Service Port组成一个具体的通信端口
>>
>
> **NodePort**
>
> 在每个Node上为需要外部访问的Service开启一个对应的TCP监听端口
>
> ```
> apiVersion: v1
> kind: Service
> metadata:
>  name: tomcat-service
> spec:
>  type: NodePort
>  ports:
>   - port: 8080
>     nodePort: 31002
>  selector:
>    tier: frontend
> ```

##### Volume

> 是Pod中能够被多个容器访问的共享目录
>
> `例子`
>
> ```
> spec:
>  volumes:
>   - name: datavol
>     emptyDir: {}
>  containers:
>   - name: tomcat-demo
>     image: tomcat
>     volumeMounts:
>      - mountPath: /mydata-data
>      	name: datavol
>     imagePullPolicy: IfNotPresent
> ```
>
> **Volume类型:**
>
> ```
> emptyDir:
>   一个emptyDir Volume是在pod分配到Node时创建的,无需指定宿主机上对应的目录,由Kubernetes自动分配，当Pod从Node上移除时,emptyDir也被永久删除
> 使用场景:临时空间
>
> volumes:
> - name: datavol
>   emptyDir: {}
> ```
>
> ```
> hostPath:
>   为在Pod上挂载宿主机上的文件或目录
> 使用场景:容器生成的日志文件需要永久保存在宿主机上的文件系统
> 注意:
>   1.不同Node的具有相同配置的Pod可能会因为宿主机上的目录和文件不同而导致对Volume上目录和文件的访问结果不一致
>   2.使用了资源管理，Kubernetes无法将hostPath在宿主机上是使用的资源纳入管理
>   
> volumes:
> - name: "persistent-storage"
>   hostPath: 
>     path: "/data"
> ```
>
> ```
> NFS:
>   使用网络文件系统
>
> volumes:
> - name: nfs
>   nfs: 
>     server: nfs-server.localhost
>     path: "/"
>
> ```
>
> ```
> gcePersistentDisk
>   使用谷歌公有云提供的永久磁盘(Persistent Disk,PD)
> ```
>
> ```
> awsElasticBlockStor
>   使用亚马逊公有云提供的EBS Volume存储数据
> ```

##### Persistent Volume

> 网络存储，可以理解成Kubernetes集群中的某个网络存储中对应的一块存储
>
> **类型:**
>
> ```
> GCE Persistent Disks,NFS,RBD,iSCSCI,AWS ElasticBlockStor,GlusterFS
> ```
>
> `NFS类型PV yaml例子`
>
> ````
> apiVersion: v1
> kind: PersistentVolume
> metadata:
>  name: pv03
> spec:
>  capacity:
>    storage: 5Gi
>  accessModes:
>   - ReadWriteOnce
>  nfs:
>    path: /somepath
>    server: 172.17.0.2
> # accessModes属性: 
> # ReadWriteOnce: 读写权限，只能被单个Node挂载
> # ReadOnlyMany: 只读权限，允许被多个Node挂载
> # ReadWriteMany: 读写权限，允许被多个Node挂载
> ````
>
> **PV状态**
>
> ```
> Available: 空闲状态
> Bound: 已经绑定大道某个PVC上
> Released: 对应的PVC已经删除，单资源还没被集群收回
> Failed: PV自动回收失败
> ```
>
> **某个Pod想申请某种条件的PV，首先需要定义一个PVC(PersistentVolumeClaim)**
>
> ```
> apiVersion: v1
> kind: PersistentVolumeClaim
> metadata:
>  name: myclaim
> spec:
>  accessModes:
>   - ReadWriteOnce
>  resources:
>    requests:
>      storage: 8Gi
> ```
>
> **然后再Pod的Volume定义中引用上述PVC**
>
> ```
> volumes:
> - name: mypd
>   persistentVolumeClaim:
>     claimName: myclaim
> ```

##### Namespace命名空间

> 实现多租房的资源隔离，集群启动后，会创建一个名为“default"的Namespace,如果不指名Namespace，资源会被创建到default的空间上
>
> 通过命令查看: kubectl get namespaces

##### Annotation注解

> 用户任意定义的“附加"信息，用来记录如下信息
>
> ```
> build信息，release信息，Docker镜像信息
> 日志库,监控库
> ```

#### 安装

##### Kubeadm工具快速安装

##### 二进制方式安装

#### Docker 网络





OCI(open container initiative) 开放容器计划

容器运行时/容器分发/容器镜像

容器引擎: docker/podman(不需要守护进程/不需要root特权)

构建镜像: docker/buildah(包含在podman cli)

容器运行时: runc(GO编写)/crun(redhat用c编写的)/containerd(docker默认的运行时,后台依赖于runc)

镜像检查分发: docker(dockr inspect)/Skopeo

Lniux虚拟化技术:Linux Containers(LXC:Linux容器)
