# -*- coding:utf-8 -*-
import re
"""
1、. 匹配任意除换行符“\n”外的字符；
2、*表示匹配前一个字符0次或无限次；+一次或多次，?表示0次或1次
4、+或* 贪婪匹配，即尽可能多的匹配
4、+或*后跟？表示非贪婪匹配，即尽可能少的匹配，如*?；
    5、 .*? 表示匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
如：a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。

"""
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#re.search 扫描整个字符串并返回第一个成功的匹配
#re.findall在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#pattern = re.compile(r'\d+')
#m = pattern.match('one12twothree34four')
#re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
a='C|C++|Java|c#|Python|Javascript'
b='py1aaa2thona123333ja1sss2va43241ccc2++'
c='python 11java  javascript'
d="""centyuan"""
s="ip='230.192.168.78',version='1.0.0',ip='230.192.168.20',version='1.0.0'，ip='230.192.168.100',version='1.0.0'"
result=re.findall("ip='(?P<ip>\d+.\d+.\d+.\d+)",s) ##正则表达式分组(?P<name>)分组命名
result1=re.findall("(?P<ip>\d+.\d+.\d+.\d+)",s)
print("result1",result1)
print(result[1])
print(re.search("ip='(?P<ip>\d+.\d+.\d+.\d+)",s).group('ip'))
a1 = re.findall('Python',a)
print(a1)
#正则表达式分组的概念
b1=re.findall('1[a-z]*2',b)
b2=re.findall('1([a-z]*)2',b)
print(re.findall('c(\d+)',b))
print(b1)
print(b2)
#默认是贪婪的 '[a-z]{3,6}?'非贪婪
c1=re.findall('[a-z]{3,6}',c)
print(c1)
language = 'PythonC#JavaC#PHPC#'
def convert(value):
    mat=value.group()
    return '!!'+mat+'!!'
r=re.sub('C#',convert,language)
print(r)




# 实例之匹配电话号码
strs = 'dsadasdgs031-1564653233adads2312-24644567dZDxz  《《《《 15808939049  《18382972834》'
pat_1 = r'[0-9-()（）]{7,18}' # 国内固话
pat_2 = r"1[35789]\d{9}"  # 国内手机
print('电话匹配')
print('国内固话',re.compile(pat_1).findall(strs))
print('国内手机',re.findall(pat_2,strs))
print(re.findall(r'(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', strs))

# 匹配qq
or_d = """Java技术群： 227270512 （人数：3000）Go开发者群（新）： 14718890861 （人数：2000）PHP开发者群： 460153241 （人数：2000）MySQL/SQL群： 418407075 （人数：2000）大数据开发群： 655154550 （人数：2000）Python技术群： 287904175 （人数：2000）人工智能深度学习： 456236082 （人数：2000）测试工程师群： 415553199 （人数：2000）前端开发者群： 410430016 （人数：2000）C/C++技术群(新)： 629264796 （人数：2000）Node.js技术群(新)： 621549808 （人数：2000）PostgreSQL数据库群： 539504187 （人数：2000）Linux运维技术群： 479429477 （人数：2000）Oracle数据库： 175248146 （人数：2000）C#/ASP.Net开发者： 630493968 （免费，人数：2000）数据分析师群： 397883996 （人数：2000）//更多请阅读：https://www.yiibai.com/python3"""
# data = requests.get("https://www.yiibai.com/python3").text
pat = '[1-9]([0-9]{5,11})'
result = re.compile(pat).findall(or_d)
# qq号去重
qqlist = list(set(result))
print(result)
# 匹配邮箱
regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
html_content = "邮箱:centyuan@outlook.com qq邮箱：375319412@qq.com,gmail邮箱centyuan@gmail.com，可惜不 centyuan@163.com"
emails = re.findall(regex, html_content)


html_doc = """
<li class="Sevli" open-window="https://www.vcag537.net/OnlineCS" op-width="550px" op-height="735px" op-resize="no" op-name="OCSCenter">
</li>
<a target="_blank" href="http://wpa.qq.com/msgrd?v=3&amp;uin=965722111&amp;site=qq&amp;menu=yes"><div class="boxBlock"><span class="qq-cont">965722111</span></div></a>
<a target="_blank" href="https://www.rbxxw.com/Chat/Chat?userID=&amp;userName="><span><i><span role="img" aria-label="customer-service" class="anticon anticon-customer-service"><svg viewBox="64 64 896 896" focusable="false" data-icon="customer-service" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M512 128c-212.1 0-384 171.9-384 384v360c0 13.3 10.7 24 24 24h184c35.3 0 64-28.7 64-64V624c0-35.3-28.7-64-64-64H200v-48c0-172.3 139.7-312 312-312s312 139.7 312 312v48H688c-35.3 0-64 28.7-64 64v208c0 35.3 28.7 64 64 64h184c13.3 0 24-10.7 24-24V512c0-212.1-171.9-384-384-384zM328 632v192H200V632h128zm496 192H696V632h128v192z"></path></svg></span></i>&nbsp;在线客服</span></a>
<img src="http://j3.wdyxa.com/mh-mgm/pc/scripts/images/pz.png" alt="">

"""

# 匹配url
customer_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
pattern = re.compile(r'(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?')
# re.finditer(pattern, string)返回MatchObject对象上的迭代器.
match_re=[x.group() for x in re.finditer(customer_regex,html_doc)]
print("匹配url：",match_re)

# 匹配域名
#  domain_regex = r'([a-zA-Z0-9]([a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,11}'
# domain_regex_1 = r'([a-zA-Z0-9]([a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+(com|net|org|in|me)'