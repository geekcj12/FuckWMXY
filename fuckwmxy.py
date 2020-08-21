import requests
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

submit_url = 'https://reportedh5.17wanxiao.com/sass/api/epmpics'

# 根据情况自行替换
submit_json = {
  "businessType": "epmpics",
  "method": "submitUpInfo",
  "jsonData": {
    "deptStr": {
      "deptid": 111111,
      "text": "班级"
    },
    "areaStr": "地址",
    "reportdate": round(time.time() * 1000), # 提交时间，获取时间戳，此处请保留
    "customerid": "1111",
    "deptid": 111111,
    "source": "alipay",
    "templateid": "pneumonia",
    "stuNo": "学号",
    "username": "你的名字",
    "phonenum": "1111111111",
    "userid": "1111111",
    "updatainfo": [
      {
        "propertyname": "fhhb",
        "value": "2010级"
      },
      {
        "propertyname": "isFFHasSymptom",
        "value": "健康"
      },
      {
        "propertyname": "isConfirmed",
        "value": "否"
      },
      {
        "propertyname": "isTouch",
        "value": "否"
      },
      {
        "propertyname": "isContactFriendIn14",
        "value": "没有"
      },
      {
        "propertyname": "xinqing",
        "value": "健康"
      }
    ],
    "gpsType": 1
  }
}

def sendMail(errorData=None):
  user = '' # 发件邮箱
  password = '' # 发件密码
  to_addr = '' # 接收邮箱
  host = '' # SMTP服务器
  port = 465  # SMTP端口

  if errorData is not None:
    message = MIMEText(errorData['data'], 'plain', 'utf-8')   #发送的内容
    message['From'] = Header("完美校园打卡脚本", 'utf-8')   #发件人
    message['To'] = Header("管理员", 'utf-8')   #收件人
    subject = '健康打卡失败'
    message['Subject'] = Header(subject, 'utf-8')  #邮件标题
  else:
    message = MIMEText('健康打卡成功', 'plain', 'utf-8')   #发送的内容
    message['From'] = Header("完美校园打卡脚本", 'utf-8')   #发件人
    message['To'] = Header("管理员", 'utf-8')   #收件人
    subject = '健康打卡成功'
    message['Subject'] = Header(subject, 'utf-8')  #邮件标题

  #配置服务器
  smtp = smtplib.SMTP_SSL(host, port)
  smtp.login(user, password)

  try:
    smtp.sendmail(user, to_addr, message.as_string())
  except Exception as e:
    print ('邮件发送失败--' + str(e))
  print ('邮件发送成功')

response = requests.post(submit_url, json=submit_json)
result = response.json()

# 如果不需要邮箱通知，可以把代码注释
if (result['code'] == '10000'):
  sendMail()
else:
  sendMail(result)
