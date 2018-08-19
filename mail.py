#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
 
def sendmail(header, msg):
    try:
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header("lili", 'utf-8')
        message['To'] =  Header("licanwei", 'utf-8')
        message['Subject'] = Header(header, 'utf-8')
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException as exc:
        print exc
        print "Error: 无法发送邮件"
    finally:
        smtpObj.quit()
if __name__ == '__main__':
    header = 'hello'
    msg = 'this is a first mail'
    sendmail(header, msg)
