# ROOT CTF 2017 1st
## Overview
Do you know ㅁㅁㅁ?

740

어렵디 어려운 이 문제... 누가 풀 것인가..?
복호화 사이트 -> ㅁㅁㅁencryption.com/

Link

## How to solve
```
[0 = 4dog] [2 = 1dog] [4 = 4dog] [5 = 4dog]
[6 = 1dog] [7 = 1dog] [8 = 2dog] [9 = 3dog]
[a = 4dog] [b = 3dog] [c = 3dog] [d = 2dog]
```

이것들을 이렇게 생각했다.

`[value = n개]`

그랬더니 나오는 세트는 1개

b 0 2 5 5 4 4 c
c 0 7 9 8 5 4 4
0 d a c 0 b a a
9 d b 8 a 5 9 6

이걸 다 붙인 다음
[md5encryption.com](http://md5encryption.com) 에서 디코딩하면 된다.

## Flag
![decrypt](MD5_decrypt.PNG)

`FLAG{MD5_3nCryPt_Ye@h!}`