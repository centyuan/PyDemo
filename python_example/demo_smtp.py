#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-10 上午8:26
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "centyuan@qq.com"  # 用户名
mail_pass = "asphpnohrvumcagh"  # 口令

sender = 'centyuan@qq.com'
receivers = 'cent_yuan@163.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('钥匙你放在哪里了?', 'plain', 'utf-8')
message['From'] =Header(sender, 'utf-8')
message['To'] = Header(receivers, 'utf-8')

subject = 'Lover'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, ['cent_yuan@163.com','1471889086@qq.com'], message.as_string())#可以传入一个list,一次发给多个人
    #as_string()把MIMEText对象变成str
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件"   ,e)