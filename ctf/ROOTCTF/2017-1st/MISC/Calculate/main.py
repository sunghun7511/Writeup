import sys

def one(num, size):
    r = num + size
    r += 915
    return r

def un_one(r, size):
    r -= 915
    return r - size

def two(num, size):
    r = num - size
    r -= 372
    return r

def un_two(r, size):
    r += 372
    return r + size

def three(num, size):
    r = num ^ size
    r ^= 826
    return r

def un_three(r, size):
    r ^= 826
    return r ^ size


def four(num, size):
    size %= 32
    r = num >> (32 - size)
    b = (num << size) - (r << 32)
    return b + r




result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360,
              4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]

Number = list()

for ind, i in enumerate(result):
    for j in range(10000000):
        if(four(j, 100) == i):
            Number.append(j)
            print("Found! " + str(j))
            break
    
for ind, i in enumerate(Number):
    Number[ind] = un_three(i, 100)
    
for ind, i in enumerate(Number):
    Number[ind] = un_two(i, 100)
    
for ind, i in enumerate(Number):
    Number[ind] = un_one(i, 100)

for i in Number:
    sys.stdout.write(chr(i))

print("")


def number(string):
    result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360,
              4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
    Number = []
    tmp = 0

    for i in string:
        Number.append(ord(i))

    for i in Number:
        Number[tmp] = one(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = two(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = three(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = four(i, 100)
        tmp += 1

    if Number == result:
        Number
        result
    else:
        print "Incorrect.."
