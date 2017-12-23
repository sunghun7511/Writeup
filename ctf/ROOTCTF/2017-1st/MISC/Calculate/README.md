# ROOT CTF 2017 1st
## Overview
Calculate

167

누가 내 패스워드좀 알려줘! 

Link

## How to solve

받은 `calculate.py` 파일을 열어보면 다음과 같은 파이썬 소스를 준다.

```python
def one(num, size):
    r = num + size
    r += 915
    return r


def two(num, size):
    r = num - size
    r -= 372
    return r


def three(num, size):
    r = num ^ size
    r ^= 826
    return r


def four(num, size):
    size %= 32
    r = num >> (32 - size)
    b = (num << size) - (r << 32)
    return b + r


if __name__ == "__main__":
    result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360,
              4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
    string = raw_input("Input String : ")
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

    print Number
    if Number == result:
        print "Correct!!"
    else:
        print "Incorrect.."
```

이제 각각 `one`, `two`, `three`, `four` 를 역함수를 만들면 되는데,

`four` 는 만들기 귀찮아서 브루트포싱을 하도록 만들었다.

아래는 원래 함수와 역함수, 그것으로 최종 플래그를 얻어내는 소스이다.

```python
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
```

## Flag
```
shgroup@SH-Group:/mnt/e/Writeup/ctf/ROOTCTF/2017-1st/MISC/Calculate$ python ./main.py
Found! 315
Found! 309
Found! 318
Found! 312
Found! 452
Found! 303
Found! 474
Found! 459
Found! 268
Found! 463
Found! 460
Found! 474
Found! 288
Found! 305
Found! 270
Found! 458
Found! 460
Found! 288
Found! 306
Found! 270
Found! 467
Found! 458
Found! 460
Found! 288
Found! 297
Found! 273
Found! 303
Found! 288
Found! 303
Found! 273
Found! 309
Found! 450
FLAG{Rev3rse_P1us_M1nus_X0R_R0L}
```

`FLAG{Rev3rse_P1us_M1nus_X0R_R0L}`