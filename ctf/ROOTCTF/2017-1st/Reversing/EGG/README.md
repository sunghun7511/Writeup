# ROOT CTF 2017 1st
## Overview
EGG

863

게임을 하는데 캐릭터가 죽어버렸다 
어서 빨리 살려서 다시 게임을 하자 

Link

## How to solve

분석을 해보면 어떠한 입력을 받고, xor 을 한다.

헥스레이로 나온 소스를 보면서 역연산 소스를 짰다.

### Python

```python
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
```

### C
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char f[] = "Mh;y;mR1@OijQhHW6Ah=hB";
int y = 17;
int m = 12;
int d = 21;

int r(int a){
    int i, j, k;
    for(i = 0 ; i < y ; i ++){
        a ^= y;
        for(j = 0 ; j < m ; j ++){
            a ^= m;
            for(k = 0 ; k < d ; k ++){
                a ^= d;
            }
        }
    }
    return a;
}

long long int sha(int a){
    int as[] = {8, 9, 15, 5, 11, 1, 3, 5, 13, 1, 14, 3, 4, 14, 7, 4, 193, 6, 6, 12, 15, 10, 12, 10, 2, 13, 8, 7, 3, 7, 1, 7, 5, 8, 12, 3, 4, 11, 14, 5, 1, 11, 0, 3, 9, 4, 5, 6, 8, 12, 5, 3, 10, 15, 3, 14, 15, 4, 8, 10, 11, 15, 2};
    return (unsigned int)as[(signed int)r(a)];
}

int main(void){
    int i = 0;

    for ( i = 0; i < strlen(f); ++i )
        f[i] ^= sha(i + 2);
    
    printf("%s\n", f);
    return 0;
}
```

왜그랬는지는 모르겠지만 `python` 과 `c` 두개로 짰다.

## Flag
`FLAG{An1v1a_3GGniViA_3Ni6mA}`