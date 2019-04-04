import requests
import re
import hashlib
import urllib
import urllib2
import base64

url = 'http://104.154.106.182:5050/?secret=flag'

#data = {"UID" : "f899139df5e1059396431415e770c6dd" , "FLAG" : "encryptCTF{y0u_c4nt_U53_m3}"}
data = {"UID" : "cfcd208495d565ef66e7dff9f98764da" , "FLAG" : "encryptCTF{y0u_c4nt_U53_m3}"}
#opener = urllib2.build_opener()
s = requests.Session()

r = s.get(url,cookies=data)
resp = r.text
#print r.text

message = resp[resp.find('<!--'):resp.find('-->')][4:44446]
fun = base64.b64decode(message)
print fun 










#reponse = req.read()

#r = re.findall('<!-- \r\n\t\t -->', sa.read(), re.DOTALL)[0]





#print re.findall('FLAG-\S*', req, re.MULTILINE)[0][:-6]
