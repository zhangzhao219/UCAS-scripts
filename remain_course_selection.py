import time
import smtplib
import requests
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def checkclass(classlist):
    url = 'https://jwba.ucas.ac.cn/sc/public/coursePublic'
    page = pd.read_html(url)[0]
    checkclass = page.loc[page["课程编号"].isin(classlist),["课程编号","课程名称","限选人数","已选人数"]]
    checkclass["已选人数"]= checkclass["已选人数"].astype('int')
    checkclass["限选人数"]= checkclass["限选人数"].astype('int')
    print(checkclass)
    checkclass = checkclass[checkclass["已选人数"] < checkclass["限选人数"]]
    if len(checkclass) != 0:
        sendEmail('发送邮箱','发送邮箱客户端密码',['接收邮箱1','接收邮箱2'],checkclass)

    for _,data in checkclass.iterrows():
        if not data[0] in havementionedlist:
            havementionedlist.append(data[0])
            param = {
                'title':data[1] + "有剩余名额！",
                'desp':"课程编号：{}，课程名称：{}，限选人数：{}，已选人数：{}\n".format(data[0],data[1],data[2],data[3])
            }
            requests.get("https://sctapi.ftqq.com/SCTxxxxxxxxxxxxxxxxx.send",params=param) # server酱 https://sct.ftqq.com/ 
            

def sendEmail(fromaddr,password,toaddrs,df):
    m = MIMEMultipart()
    m['Subject'] = "关注课程有剩余选课名额！"
    for _,data in df.iterrows():
        m.attach(MIMEText("课程编号：{}，课程名称：{}，限选人数：{}，已选人数：{}</br>".format(data[0],data[1],data[2],data[3]),'html','utf-8'))
    m.attach(MIMEText('点击下面链接快速选课：<a href="https://jwxk.ucas.ac.cn/courseManage/main">https://jwxk.ucas.ac.cn/courseManage/main</a>','html','utf-8'))
    
    for toaddr in toaddrs:
        try:
            server = smtplib.SMTP('发送邮箱SMTP地址')
            server.login(fromaddr,password)
            server.sendmail(fromaddr, toaddr, m.as_string())
            server.quit()
        except smtplib.SMTPException as e:
            print('error:',e)

if __name__ == '__main__':
    havementionedlist = []    
    classlist = ['课程编号1', '课程编号2']
    while 1:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        try:
            checkclass(classlist)
        except:
            print("临时错误")
        time.sleep(30)
        