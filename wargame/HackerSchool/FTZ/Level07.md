# Hackerschool FTZ Level 07

```
login as: level7
level7@192.168.18.131's password:
[level7@ftz level7]$ ls
hint  public_html  tmp
[level7@ftz level7]$ cat hint


/bin/level7 명령을 실행하면, 패스워드 입력을 요청한다.

1. 패스워드는 가까운곳에..
2. 상상력을 총동원하라.
3. 2진수를 10진수를 바꿀 수 있는가?
4. 계산기 설정을 공학용으로 바꾸어라.


[level7@ftz level7]$ /bin/level7
Insert The Password : ABCD
--_--_- --____- ---_-__ --__-_-
[level7@ftz level7]$ /bin/level7
Insert The Password : mate

Congratulation! next password is "break the world".

[level7@ftz level7]$
```

`/bin/level7` 을 입력하면 패스워드를 입력하라고 하고, 아래에 --_- 와 같이 되있는 문장이 나온다.

-는 1로, _는 0으로 치환한 다음 ascii 로 바꾸면 `mate` 가 된다.

이를 다시 `/bin/level7` 을 실행시키고 `mate` 를 입력하면 된다.