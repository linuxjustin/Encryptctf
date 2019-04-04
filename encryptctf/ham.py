from pwn import *
import re
context.log_level='critical'
host = '104.154.106.182'
port =6969
s=remote(host,port)
prompt=s.recv()
while True:
 try:
	for j in range(100):
	    prompt=s.recv()
	    ch1=prompt.split("[*] CODE: ")
	    #print("----------------")
	    #print(ch1)
	    #print("----------------")
	    ch=ch1[1][0:7]
	    #print(ch)
	    list1=[]
	    
	    for i in ch:
		list1.append(int(i))
	    
	    num = [0,0,0]
	    num[0]=list1[3]^list1[4]^list1[5]^list1[6]
	    num[1]=list1[1]^list1[2]^list1[5]^list1[6]
	    num[2]=list1[0]^list1[2]^list1[4]^list1[6]
	    
	    numb_str=""
	    for i in num:
		numb_str+=str(i)
	    numb_int=int(numb_str,2)
	    
	    if numb_int!=0:
		list1[(numb_int-1)]=1-list1[(numb_int-1)]
	    
	    ch = [list1[2],list1[4],list1[5],list1[6]]
	    
	    ph=""
	    
	    for i in ch:
		ph+=str(i)
	    
	    s.sendline(ph) 
	    prompt=s.recv()
	    print(prompt)
	    print(j)
 except:
	j=0
        s=remote(host,port)
print(prompt)
