f = "Mh;y;mR1@OijQhHW6Ah=hB"
q_400A40 = [8, 9, 15, 5, 11, 1, 3, 5, 13, 1, 14, 3, 4, 14, 7, 4, 193, 6, 6, 12, 15, 10, 12, 10, 2, 13, 8, 7, 3, 7, 1, 7, 5, 8, 12, 3, 4, 11, 14, 5, 1, 11, 0, 3, 9, 4, 5, 6, 8, 12, 5, 3, 10, 15, 3, 14, 15, 4, 8, 10, 11, 15, 2]
y = 17
m = 12
d = 21

## r
def r(a):
    for i in range(y):
        a ^= y
        for j in range(m):
            a ^= m
            for k in range(d):
                a ^= d
    return a

## sha
def sha(a):
    return q_400A40[r(a)]

## original
out = ""
for ind, i in enumerate(f):
    out = out + chr(ord(i) ^ sha(ind + 2))

print("original : " + out)

## input
inp = raw_input("Input > ")

if len(inp) > 22:
    inp = "long"
    ## maybe it is fail..

## ch
out = ""
for ind, i in enumerate(inp):
    out = out + chr(ord(i) ^ sha(ind + 2))

if out is not f:
    print("Egg broken..")
else:
    print("Success!")