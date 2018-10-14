'''发送邮件'''

import smtplib  #连接smtp服务器
from email.mime.text import MIMEText  #邮件正文
from email.mime.multipart import MIMEMultipart  #上传附件
import sys
sys.path.append("..")  # 提升包搜索路径到项目路径
from config import config as cf

#发送报告
def send_report():
    msg = MIMEMultipart() #混合格式的邮件
    #邮件正文
    body = MIMEText('测试报告','plain','utf-8') #plain为普通文本，也可以html
    msg.attach(body)
    #邮件头
    msg['From'] = cf.sender
    msg['To'] = cf .receiver
    msg['Subject'] = cf.subject
    #报告附件
    with open(cf.report_file) as f:
        att_file = r.read()
    att1=MIMEText(att_file,'base64','utf-8') #将utf-8转为base64格式作为网络传输
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

    #发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_uset,cf.smtp_password)
    smtp.send(cf.sender,cf.receiver,msg.as_string())
    cf.logging.info("send email done")

if __name__ == '__main__':
    send_report()

