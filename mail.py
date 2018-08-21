#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host=""  #设置服务器
mail_user=""    #用户名
mail_pass=""   #口令


sender = ''
receivers = []  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

def read_config():
    """
    config file:
    #smtp server
    #user name
    #user password
    #sender
    #recevier

    """
    config_file = '/home/code/future/mail.txt'
    f = open(config_file, 'r')
    config = f.readlines()
    f.close()
    mail_host = config[0].strip('\n')
    mail_user = config[1].strip('\n')
    mail_pass = config[2].strip('\n')
    sender = config[3].strip('\n')
    receiver = config[4].strip('\n')
    return mail_host, mail_user, mail_pass, sender, receiver

def sendmail(header, msg):
    mail_host, mail_user, mail_pass, sender, receiver = read_config()
    receivers.append(receiver)
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
