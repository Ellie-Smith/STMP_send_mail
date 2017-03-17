#coding=utf-8
import smtplib

from email.header import Header

from email.mime.text import MIMEText

from_addr = 'xxxx@163.com'  # 发送邮箱的地址

password = 'xxxxx'  # 发送邮箱的客户端登陆密码，可能和网页登陆密码不同，需要单独设置

smtp_server = 'smtp.163.com'

to_addr = 'xxxxx@163.com'  # 接收邮箱地址

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

msg['From'] = 'xxxx@163.com'  # 发送邮箱地址

msg['Subject'] = Header(u'text', 'utf8').encode()  # 邮件主题

server = smtplib.SMTP(smtp_server, 25)  # 连接SMTP服务器

server.login(from_addr, password)  # 登陆

server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送

server.quit()