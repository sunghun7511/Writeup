from pwn import *

context.arch = "amd64"
context.log_level = "DEBUG"

e = Elf("./babyheap")

isRemote = False
if isRemote:
    p = remote("remote.r", 1010)
else:
    p = process("./babyheap")




p.interactive()