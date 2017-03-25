# -*-coding:utf-8-*-

# python当中，一般使用smtplib和email两个模块来进行邮件的发送，
# email负责构造邮件，smtplib负责发送邮件。

# 用email模块来构造邮件
from email.mime.text import MIMEText

email_msg = MIMEText('hello python', 'plain', 'utf-8')

# 通过smtp来发送邮件

# 设定发送人的邮箱和密码
from_email = 'python_ivy@163.com'
password = '123456ab'

# SMTP服务器地址
smtp_server = 'smtp.163.com'

to_email = 'python_ivy@163.com'

import smtplib

server = smtplib.SMTP(smtp_server, 25)

# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)

# login()方法用来登录SMTP服务器
server.login(from_email, password)

# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.sendmail(from_email, to_email, email_msg.as_string())

# 退出
server.quit()


# 我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


# def _format_addr(s):
#     # parseaddr用来解析邮件地址的
#     name, addr = parseaddr(s)
#     return formataddr(( \
#         Header(name, 'utf-8').encode(), \
#         addr.encode('utf-8') if isinstance(addr, unicode) else addr))
#
#
# email_msg['From'] = _format_addr(u'Python新手 <%s>' % from_email)
# email_msg['To'] = _format_addr(u'慧测自动化学员 <%s>' % to_email)
# email_msg['Subject'] = Header(u'终于有一个主题了', 'utf-8').encode()

email_msg['From'] = u'Python <%s>' % from_email
email_msg['To'] = u'ivy <%s>' % to_email
email_msg['Subject'] = Header(u'终于有一个主题了', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)

# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)

# login()方法用来登录SMTP服务器
server.login(from_email, password)

# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.sendmail(from_email, to_email, email_msg.as_string())

# 退出
server.quit()
