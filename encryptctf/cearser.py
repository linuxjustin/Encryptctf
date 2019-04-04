cip = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ==".decode('base64')
i=1
plain=""
while True:
    for c in cip:
        plain+=chr((ord(c)+i)%256)
    i+=1
    if 'encryptCTF' in plain:
        print plain
        exit()
