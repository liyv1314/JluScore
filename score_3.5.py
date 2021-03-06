# -*- coding:utf8 -*-
# python 3.5

import urllib
import urllib.request
import hashlib
import json
import http.cookiejar

print('This a python application for JluScore')
#username = str(input('your username:'))
#password = str(input('your password:'))
password = 'UIMS'+username+password
password = password.encode('utf-8')
password = hashlib.md5(password).hexdigest()
#print password

CjCookie = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CjCookie))
#opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36')]
url = 'http://cjcx.jlu.edu.cn/score/action/security_check.php'
data = {
        'j_username':username,
        'j_password':password,
        'save_cookie':'month'
        }
postdata = urllib.parse.urlencode(data)
postdata = postdata.encode('utf-8')
#postdata = 'j_username='+username+'&j_password='+password+'&save_cookie=month'
#print postdata
opener.open(url,postdata)
for item in CjCookie:
     phpsession = item.value
#print phpsession

CjCookie = 'JSESSIONID=; loginPage=userLogin.jsp; alu='+username+'; alp='+password+'; ald=month; PHPSESSID='+phpsession
#print CjCookie

headers = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Content-Length':'68',
            'Content-Type':'application/json',
            'Cookie':CjCookie,
            'Host':'cjcx.jlu.edu.cn',
            'Origin':'http://cjcx.jlu.edu.cn',
            'Referer':'http://cjcx.jlu.edu.cn/score/index.php',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
          }
#print  headers
posturl = 'http://cjcx.jlu.edu.cn/score/action/service_res.php'
postdata = '{"tag":"lessonSelectResult@oldStudScore","params":{"xh":"'+username+'"}}'
postdata = postdata.encode('utf-8')
request = urllib.request.Request(posturl,postdata,headers)
response = urllib.request.urlopen(request)
text = response.read()
text = text.decode('utf-8')
#print text
#text = json.loads(text)
#print text
#f = open("JluScore.txt",'wb')
#f.write(text)
#f.close()

#score = open('score.json')
#Json = score.read()
#score.close()
#print Json

Json = json.loads(text)
#print Json['items']
items = Json['items']

finalscore = open(username+'score.txt','w')
finalscore.close()
finalscore = open(username+'score.txt','a')
for item in items:
#    #print item['isReselect']
#    #print item['xkkh']
#    print item['studName']
#    print item['xh']
#    #print str(item['lsrId'])
#    print item['cj']
#    print str(item['gpoint'])
#    #print str(item['zscj'])
#    print str(item['credit'])
#    print item['kcmc']
#    #print str(item['termId'])
#     print item['studName']+' '+item['xh']+' '+item['cj']+' '+str(item['gpoint'])+' '+item['kcmc']
#     text = item['cj']+'        '+str(item['gpoint'])+'        '+item['kcmc']+'\n'
     if item['cj'] == '优秀' or item['cj'] == '良好' or item['cj'] == '及格':
         text = item['cj'].ljust(18)+str(item['gpoint']).ljust(20)+item['kcmc'].ljust(20)+'\n'
     else:   
         text = item['cj'].ljust(20)+str(item['gpoint']).ljust(20)+item['kcmc'].ljust(20)+'\n'
#     print text
     finalscore.write(text)
finalscore.close()
