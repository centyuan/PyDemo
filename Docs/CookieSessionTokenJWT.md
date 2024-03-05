---
title: Cookie|Session|Token|JWT
categories:
  - 权限和认证
tags:
  - 权限和认证
---



#### 概述

>认证(Authentication), 就是验证当前用户的身份，证明"你是你自己"
>
>授权(Authorization),用户授予第三方应用访问该用户某些资源的权限

HTTP是无状态协议,需要去维护一个状态，去告诉服务器请求是那个用户的

#### Cookie

>cookie是服务器发送到用户浏览器并保存在本地的一小块用户相关的数据,随着每次请求时自动带上，用于服务器对请求做标识
>
>cookie是不许跨域的，每个cookie都会绑定到单一域名，一级二级域名允许共享使用
>
>服务端通过响应头:Set-Cookie，来设置cookie
>
>expires: cookie过期时间
>
>secure: cookie是否仅被使用安全协议传输(为true则在https才有效)
>
>httpOnly: 为true，则无法通过js脚本读取cookie信息,一定程度上可以防止xss攻击



#### Session

>记录服务器和客户端的会话，session基于cookie实现的，session存储在服务端,sessionID则存储在cookie中
>
>Session比Cookie更安全,因为用户相关的数据存储在服务端



#### Token

>全称是Access Token,访问资源接口（API）时所需要的资源凭证,Token 使服务端无状态化，不会存储会话信息
>
>简单的Token组成:
>
>​	uid: 用户的唯一标识
>​	time: 当前时间戳
>​    sign: 签名,由token的前几位+盐以哈希算法压缩成一定长的十六进制字符串
>
>**refresh token**：
>
>用于刷新access token的token
>
>参考[Token认证的来龙去脉](https://segmentfault.com/a/1190000013010835)



#### JWT
>深入理解JWT的使用场景和优劣：https://www.cnblogs.com/cokeking/p/10969579.html
>Json Web Token是目前最流行的跨域认证解决方案,是一种认证授权机制
>
>参考:[JWT](http://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html)
>
>**原理:**服务器认证后，生成一个json对象发送给用户
>
>**数据结构**:类似这样，中间用三个点分割成三部分,JWT内部是没有换行的
>
>```
>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.gRG91IiwiaXNTb2NpYWwiOnRydWV9.4pcyMD09olSyXnrXCjTwX
>```
>
>**JWT组成:**
>
>Header.Payload.Signature
>
>`Header:`头部,是一个json对象，描述JWT的元数据
>
>```
>{
>	"alg":"HS256",   # 表示签名的算法
>	"typ": "JWT"     # 表示这个令牌类型
>}
>```
>
>最后，将上面的 JSON 对象使用 Base64URL 算法转成字符串
>
>`Payload:` 负载，也是一个json对象，用来存放实际传递的数据
>
>```
># JWT官方规定的7个字段
>iss: 签发人issuer
>exp: 过期时间expiration time
>sub: 主题subject
>aud: 受众audience
>nbf: 生效时间Not Before
>iat: 签发时间Issued At
>jti: 编号JWT ID
>除了以上字段，还可以定义私有字段
>```
>
> JSON 对象也要使用 Base64URL 算法转成字符串
>
>`Signature:`签名，对Header和Payload签名，防止数据篡改
>
>```
>需要指定一个秘钥secret，存储在服务器上,使用Header指定的签名算法按照一下方式签名
>签名算法(base64UrlEncode(Header)+"."+base64UrlEncode(Payload))
>```
>
>算出签名以后，把 Header、Payload、Signature 三个部分拼成一个字符串，每个部分之间用"点"（`.`）分隔，就可以返回给用户
>
>**最大缺点**
>
>因为服务器不保存状态,token一旦签发，不能在使用过程中废止某个token，直到到期
>
>**JWT和Token**
>
>```
># 相同点
>都是访问资源的令牌
>都可以记录用户的信息
>都是服务端无状态化
># 不通点
>Token验证完后还需要查询数据库
>```
>
>

#### OAuth认证

>OAuth2.0是一种授权机制, **核心就是向第三方应用颁发令牌**
>
>参考[OAuth2.0的四种方式](http://www.ruanyifeng.com/blog/2019/04/oauth-grant-types.html)
>
>规定了四种：
>
>```
>授权码authorization-code
>隐藏式implict
>密码式password
>客户端凭证client credentials
>```
>
>**授权码**
>
>```
>指第三方应用先申请一个授权码，使用授权码申请令牌，最常用安全性最高
>```
>
>**隐藏式**
>
>```
>允许前端颁发令牌，中间没有授权码
>```
>
>**密码式**
>
>```
>允许用户直接把账号密码直接给第三方应用，应用使用账号密码直接申请令牌
>```
>
>**凭证式**



