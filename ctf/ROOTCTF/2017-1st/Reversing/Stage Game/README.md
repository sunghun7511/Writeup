# ROOT CTF 2017 1st
## Overview
Stage Game

229

인내의 시간.. 
Stage Level 1~10 

Link

## How to solve

`Ollydbg` 라는 툴을 사용해서 분석을 해보면,

스테이지마다 sleep 를 호출한다.

그래서 그냥 CALL sleep 를 NOP로 패치했다.

## Flag
![FLAG](./wait.png)

`FLAG{Y0ur_p4t1enc3_1s_gr3at!}`