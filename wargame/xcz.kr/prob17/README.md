# xcz.kr problem 2

## Overview

### Title

Password Recover...

### Description

Hi, I'M ZZANGHACKER.
I Lost My Password in XCZ.KR T.T
Help Me!! [Download Here](http://xcz.kr/START/prob/prob_files/my_pw.pcapng)

## How to solve

Open `my_pw.pcapng` file with `Wireshark`.

Then, Let's find his/her password.

Add filter to only can see `http` protocol.

![](packets.PNG)

Hmm... Oh! This is his/her password!

![](yourpw.PNG)

# Flag

`IDISLIE`