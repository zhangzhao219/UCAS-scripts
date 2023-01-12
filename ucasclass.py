import smtplib
import requests
import datetime
from urllib import request
from http import cookiejar
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

def postclass(weekname,weekday_name,filename):
    url1 = 'https://jwjz.ucas.ac.cn/jiaowu/classroom/allclassroomforquery0.asp?term=71119'
    url3 = 'https://jwjz.ucas.ac.cn/jiaowu/classroom/allclassroomforquery.asp'

    while True:
        #声明一个CookieJar对象实例来保存cookie
        cookies = cookiejar.CookieJar()
        #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler=request.HTTPCookieProcessor(cookies)
        #通过CookieHandler创建opener
        opener = request.build_opener(handler)
        #此处的open方法打开网页
        response = opener.open(url1)

        name = ""
        cookie = ""
        for item in cookies:
            name = item.name
            cookie = item.value

        cookies = {
            # 'sepuser': '"bWlkPWQ3MTI2NjJhLTU5NGEtNGQ0MC1iZjNhLTc0MzQxYzAzMjczYQ==  "',
            name: cookie,
        }
            
        headers = {
            'Host': 'jwjz.ucas.ac.cn',
            'Connection': 'keep-alive',
            'Content-Length': '64',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
            'Origin': 'https://jwjz.ucas.ac.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://jwjz.ucas.ac.cn/jiaowu/classroom/allclassroomforquery.asp',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        d = {'weekname': weekname, 'weekday_name': weekday_name,'yq':3,'classroom':''}
        response = requests.post(url3,data = d,headers=headers,cookies=cookies)
        response.encoding = 'gb2312'
        print(response.status_code)
        if response.status_code == 200:
            break
    with open('./class_'+filename+'.html','wb') as f:
        f.write(response.content)

def sendEmail(weeknum,weekday,fromaddr,password,toaddrs):
    weekdict = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'日'}

    pdfFile1 = './class_today.html'
    pdfApart1 = MIMEApplication(open(pdfFile1, 'rb').read())
    pdfApart1.add_header('Content-Disposition', 'attachment', filename=pdfFile1.split('/')[-1])
    pdfFile2 = './class_tomorrow.html'
    pdfApart2 = MIMEApplication(open(pdfFile2, 'rb').read())
    pdfApart2.add_header('Content-Disposition', 'attachment', filename=pdfFile2.split('/')[-1])
    m = MIMEMultipart()
    m.attach(pdfApart1)
    m.attach(pdfApart2)
    m['Subject'] = '第' + str(weeknum) + '周-星期' + weekdict[weekday+1] + '教室占用情况'

    try:
        server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr,password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:',e)

if __name__ == '__main__':
    weekdaylist = ['001','010','011','100','101','110','111']
    startdate = datetime.datetime(2023, 2, 20)

#     nowdate = datetime.datetime.now()+ datetime.timedelta(days=2)
#     weeknum = (nowdate - startdate).days // 7 + 1
#     postclass(weeknum,weekdaylist[nowdate.weekday()],'tomorrow')
    
#     nowdate = datetime.datetime.now()+ datetime.timedelta(days=1)
#     weeknum = (nowdate - startdate).days // 7 + 1
#     postclass(weeknum,weekdaylist[nowdate.weekday()],'today')

#     sendEmail(weeknum,nowdate.weekday(),'zhaozhao809@163.com','AIOCPCENXBJSMMCX',['zhangzhao219@sina.com'])
