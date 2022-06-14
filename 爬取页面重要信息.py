import requests
import re

"""

# 实例之匹配电话号码
str = 'dsadasdgs031-1564653233adads2312-24644567dZDxz'
pat = '\d{3}-\d{8}|\d{4}-\d{7}'
print(re.compile(pat).findall(str))
"""
# 匹配qq
or_d = """Java技术群： 227270512 （人数：3000）Go开发者群（新）： 14718890861 （人数：2000）PHP开发者群： 460153241 （人数：2000）MySQL/SQL群： 418407075 （人数：2000）大数据开发群： 655154550 （人数：2000）Python技术群： 287904175 （人数：2000）人工智能深度学习： 456236082 （人数：2000）测试工程师群： 415553199 （人数：2000）前端开发者群： 410430016 （人数：2000）C/C++技术群(新)： 629264796 （人数：2000）Node.js技术群(新)： 621549808 （人数：2000）PostgreSQL数据库群： 539504187 （人数：2000）Linux运维技术群： 479429477 （人数：2000）Oracle数据库： 175248146 （人数：2000）C#/ASP.Net开发者： 630493968 （免费，人数：2000）数据分析师群： 397883996 （人数：2000）//更多请阅读：https://www.yiibai.com/python3"""
data = requests.get("https://www.yiibai.com/python3").text
pat = '[1-9]([0-9]{5,11})'
result = re.compile(pat).findall(data)
# qq号去重
qqlist = list(set(result))
# print(result)

# 匹配邮箱
import re

regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
html_content = "邮箱:centyuan@outlook.com qq邮箱：375319412@qq.com,gmail邮箱centyuan@gmail.com，可惜不 centyuan@163.com"
emails = re.findall(regex, html_content)
# print(emails)

# 匹配电报
# 匹配微信


from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<li class="Sevli" open-window="https://www.vcag537.net/OnlineCS" op-width="550px" op-height="735px" op-resize="no" op-name="OCSCenter">
<div class="icon_rLiveService"></div>
<span>在线客服</span>
</li>
<a target="_blank" href="http://wpa.qq.com/msgrd?v=3&amp;uin=965722111&amp;site=qq&amp;menu=yes"><div class="boxBlock"><span class="qq-cont">965722111</span></div></a>
<a target="_blank" href="https://www.rbxxw.com/Chat/Chat?userID=&amp;userName="><span><i><span role="img" aria-label="customer-service" class="anticon anticon-customer-service"><svg viewBox="64 64 896 896" focusable="false" data-icon="customer-service" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M512 128c-212.1 0-384 171.9-384 384v360c0 13.3 10.7 24 24 24h184c35.3 0 64-28.7 64-64V624c0-35.3-28.7-64-64-64H200v-48c0-172.3 139.7-312 312-312s312 139.7 312 312v48H688c-35.3 0-64 28.7-64 64v208c0 35.3 28.7 64 64 64h184c13.3 0 24-10.7 24-24V512c0-212.1-171.9-384-384-384zM328 632v192H200V632h128zm496 192H696V632h128v192z"></path></svg></span></i>&nbsp;在线客服</span></a>
<img src="http://j3.wdyxa.com/mh-mgm/pc/scripts/images/pz.png" alt="">

</body>
</html>
"""

# 匹配url
customer_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
pattern = re.compile(r'(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?')
match_re=[x.group() for x in re.finditer(customer_regex,html_doc)]
print("sssssssss",match_re)



import json

wx_key = ["微信", "wx", "vx", ]
qq_key = ["QQ", "qq"]
tg_key = ['TG', '电报', 'telegram']
email_regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
wx_list, qq_list, tg_list, email_list = [], [], [], []
ht = """

<!DOCTYPE html><html><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1"><meta name=renderer content=webkit><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><link rel=icon href=/icon_people_navbar_plane_s.ico><title>辅助侦查平台</title><link href=/statics/css/app.17e4aa25.css rel=preload as=style><link href=/statics/css/chunk-libs.3dfb7769.css rel=preload as=style><link href=/statics/js/app.774a3cf5.js rel=preload as=script><link href=/statics/js/chunk-elementUI.39a6df87.js rel=preload as=script><link href=/statics/js/chunk-libs.3b78a85d.js rel=preload as=script><link href=/statics/css/chunk-libs.3dfb7769.css rel=stylesheet><link href=/statics/css/app.17e4aa25.css rel=stylesheet></head><body>     <div>
         <span> QQ 357693412</span>
          <p> 【微信】15130390 </p>
          <p> 【vx】1ssss </p>
     </div><div id=app> <span>centyuan@outlook.com  centyuan@gmail.com</span><a href="https://t.me/ay10086" rel="noopener nofollow ugc"> 电报 https://t.me/ay10086 </a></div><script>(function(e){function n(n){for(var r,c,a=n[0],f=n[1],i=n[2],d=0,l=[];d<a.length;d++)c=a[d],Object.prototype.hasOwnProperty.call(u,c)&&u[c]&&l.push(u[c][0]),u[c]=0;for(r in f)Object.prototype.hasOwnProperty.call(f,r)&&(e[r]=f[r]);h&&h(n);while(l.length)l.shift()();return o.push.apply(o,i||[]),t()}function t(){for(var e,n=0;n<o.length;n++){for(var t=o[n],r=!0,c=1;c<t.length;c++){var a=t[c];0!==u[a]&&(r=!1)}r&&(o.splice(n--,1),e=f(f.s=t[0]))}return e}var r={},c={runtime:0},u={runtime:0},o=[];function a(e){return f.p+"statics/js/"+({}[e]||e)+"."+{"chunk-065b8155":"77499851","chunk-15b54914":"3f192ea8","chunk-2b5a67a2":"55041e93","chunk-2d2105d3":"404da312","chunk-2d230fe7":"3bd3f709","chunk-2fd7f7c8":"9319a38d","chunk-4794904a":"245a2b63","chunk-06b187eb":"c372556e","chunk-5d4e8639":"9e8c26c6","chunk-64973eb2":"aff17007","chunk-232db16a":"3f338cfc"}[e]+".js"}function f(n){if(r[n])return r[n].exports;var t=r[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,f),t.l=!0,t.exports}f.e=function(e){var n=[],t={"chunk-065b8155":1,"chunk-15b54914":1,"chunk-2b5a67a2":1,"chunk-2fd7f7c8":1,"chunk-06b187eb":1,"chunk-5d4e8639":1,"chunk-64973eb2":1,"chunk-232db16a":1};c[e]?n.push(c[e]):0!==c[e]&&t[e]&&n.push(c[e]=new Promise((function(n,t){for(var r="statics/css/"+({}[e]||e)+"."+{"chunk-065b8155":"88ba38ea","chunk-15b54914":"f091bff9","chunk-2b5a67a2":"51bca063","chunk-2d2105d3":"31d6cfe0","chunk-2d230fe7":"31d6cfe0","chunk-2fd7f7c8":"363f991c","chunk-4794904a":"31d6cfe0","chunk-06b187eb":"6dfb6933","chunk-5d4e8639":"ccbb5f43","chunk-64973eb2":"08c92832","chunk-232db16a":"9b6ddc32"}[e]+".css",u=f.p+r,o=document.getElementsByTagName("link"),a=0;a<o.length;a++){var i=o[a],d=i.getAttribute("data-href")||i.getAttribute("href");if("stylesheet"===i.rel&&(d===r||d===u))return n()}var l=document.getElementsByTagName("style");for(a=0;a<l.length;a++){i=l[a],d=i.getAttribute("data-href");if(d===r||d===u)return n()}var h=document.createElement("link");h.rel="stylesheet",h.type="text/css",h.onload=n,h.onerror=function(n){var r=n&&n.target&&n.target.src||u,o=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");o.code="CSS_CHUNK_LOAD_FAILED",o.request=r,delete c[e],h.parentNode.removeChild(h),t(o)},h.href=u;var s=document.getElementsByTagName("head")[0];s.appendChild(h)})).then((function(){c[e]=0})));var r=u[e];if(0!==r)if(r)n.push(r[2]);else{var o=new Promise((function(n,t){r=u[e]=[n,t]}));n.push(r[2]=o);var i,d=document.createElement("script");d.charset="utf-8",d.timeout=120,f.nc&&d.setAttribute("nonce",f.nc),d.src=a(e);var l=new Error;i=function(n){d.onerror=d.onload=null,clearTimeout(h);var t=u[e];if(0!==t){if(t){var r=n&&("load"===n.type?"missing":n.type),c=n&&n.target&&n.target.src;l.message="Loading chunk "+e+" failed.\n("+r+": "+c+")",l.name="ChunkLoadError",l.type=r,l.request=c,t[1](l)}u[e]=void 0}};var h=setTimeout((function(){i({type:"timeout",target:d})}),12e4);d.onerror=d.onload=i,document.head.appendChild(d)}return Promise.all(n)},f.m=e,f.c=r,f.d=function(e,n,t){f.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},f.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},f.t=function(e,n){if(1&n&&(e=f(e)),8&n)return e;if(4&n&&"object"===typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(f.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)f.d(t,r,function(n){return e[n]}.bind(null,r));return t},f.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return f.d(n,"a",n),n},f.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},f.p="/",f.oe=function(e){throw console.error(e),e};var i=window["webpackJsonp"]=window["webpackJsonp"]||[],d=i.push.bind(i);i.push=n,i=i.slice();for(var l=0;l<i.length;l++)n(i[l]);var h=d;t()})([]);</script><script src=/statics/js/chunk-elementUI.39a6df87.js></script><script src=/statics/js/chunk-libs.3b78a85d.js></script><script src=/statics/js/app.774a3cf5.js></script></body></html>
"""
soup = BeautifulSoup(ht, 'lxml')
label_list = []
for child in soup.body.descendants:
    print("chilie.string:", child.string)
    print("child.get_text():", child.get_text())
    if child.string:
        print('++++++++++++')
        print(child.name)
        label_list.append(child.string)
        print("#############")

for label in list(set(label_list)):
    for regex in wx_key:
        if re.findall(regex, label):
            wx_list.append(label)
            break
    for regex in qq_key:
        if re.findall(regex, label):
            qq_list.append(label)
            break
    for regex in tg_key:
        if re.findall(regex, label):
            tg_list.append(label)
            break

    if re.findall(email_regex, label):
        email_list.append(label)
print(wx_list, qq_list, tg_list, email_list)

# # 微信号,qq号，TG号，邮箱
# # 文字：wx vx QQ TG 电报 @


# import json
# def get_cdninfo(url):
#     """
#     :param url 域名或者ip
#     """
#     re_url = "http://192.168.8.242:8000/api/cdn"
#     data = {
#         "target": url
#     }
#     res = requests.post(re_url, data=json.dumps(data))
#     pattern = r"\[[\s\S]+?\]"
#     result = json.loads(res.text)
#     print(result)
#     if result.get("code") == '200':
#         data = result.get("data")
#         all_cdn = []
#         if data:
#             for it in data:
#                 try:
#                     cdn_ = re.search(pattern,it).group(0)
#                     all_cdn.append(cdn_)
#                 except Exception as e:
#                     continue
#
#         return set(all_cdn)
# if __name__ == '__main__':
#     # www.2096.cc
#     pattern = r"\[[\s\S]+?\]"
#     res = get_cdninfo("www.jd.com")
#     print(res)
#

"""
www.amazon.com
www.youtube.com
www.facebook.com
www.2096.cc
www.97738ee.com
t663.me
j663.me
x663.me
www.huobo72.com
"""


def get_cdninfo(domain):
    """
    :param url 域名或者ip
    :return cdn_str cdn名字
    """
    re_url = "http://192.168.8.242:8000/api/cdn"
    res = requests.post(re_url, data=json.dumps({"target": domain}))
    pattern = r"\[[\s\S]+?\]"
    result = json.loads(res.text)
    if result.get("code") == '200':
        data = result.get("data")
        print(data)
        if data:
            for it in data:
                try:
                    # cdn_ = re.search(pattern,it).group(0)
                    # print(cdn_)
                    return re.search(pattern, it).group(0)
                except Exception as e:
                    print(e.__traceback__.tb_frame.f_globals['__file__'], e.__traceback__.tb_lineno, e)
                    continue


def get_importinfo(url):
    """
    :param url 页面路径
    :return  wx_list,qq_list,tg_list,email_list
    """
    wx_key = ["微信", "wx", "vx", ]
    qq_key = ["QQ", "qq"]
    tg_key = ['TG', '电报', 'telegram']
    email_regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
    wx_list, qq_list, tg_list, email_list = [], [], [], []
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'lxml')
    label_list = []
    try:
        for child in soup.body.descendants:
            if child.string:
                label_list.append(child.string)

        for label in list(set(label_list)):
            for regex in wx_key:
                if re.findall(regex, label):
                    wx_list.append(label)
                    break
            for regex in qq_key:
                if re.findall(regex, label):
                    qq_list.append(label)
                    break
            for regex in tg_key:
                if re.findall(regex, label):
                    tg_list.append(label)
                    break

            if re.findall(email_regex, label):
                email_list.append(label)

        return wx_list, qq_list, tg_list, email_list

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals['__file__'], e.__traceback__.tb_lineno, e)
        return None
