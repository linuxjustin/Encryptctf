from pwn import *
import re
context.log_level='critical'
host = '104.154.106.182'
port= 6969
conn =remote(host,port)
promt = conn.recv()
#print promt
while True:
    try:
        for i in range(100):
            promt = conn.recv()
            ch1=promt.split("[*] CODE:")
            ch = ch1[1]
            print ch
            for j in ch:
                a=conn.sendline(j)
                print a
                promt = conn.recv()
                print promt


    except:
       j=0
       promt =conn.recv()

print (promt)

