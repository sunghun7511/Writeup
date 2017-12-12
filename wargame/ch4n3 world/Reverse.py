n = "}?HVUHYHU_ZRQN_XRB_RG{ VL JDOI"
output = ""

key = 23
for ind, k in enumerate(n):
    if ord(k) < ord("A") or ord(k) > ord("Z"):
        output = output + k
    else:
        output = output + chr((ord(k)-ord("A")+key) % 26 + ord("A"))

output = output[::-1]
print(output)

'''
}?HVUHYHU_ZRQN_XRB_RG{ VL JDOI

Can you decode it?
Flag is in upper case.

FLAG IS {DO_YOU_KNOW_REVERSE?}
'''