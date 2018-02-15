# Hackerschool FTZ Level 06

```
login as: level6
level6@192.168.18.131's password:


hint - 인포샵 bbs의 텔넷 접속 메뉴에서 많이 사용되던 해킹 방법이다.


^C
[level6@ftz level6]$ ls
hint  password  public_html  tmp  tn
[level6@ftz level6]$ cat hint


hint - 인포샵 bbs의 텔넷 접속 메뉴에서 많이 사용되던 해킹 방법이다.


[level6@ftz level6]$ cat password
Level7 password is "come together".
[level6@ftz level6]$
```

처음 로그인 하면 힌트가 뜨고 쉘이 뜨지 않는다.

이 때 Ctrl + c 를 사용하면 `SIGINT` 시그널을 보내면서 해당 프로그램을 종료하게 된다.

이를 통해 쉘로 돌아가고 비밀번호 파일을 읽으면 된다.