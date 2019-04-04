#!/usr/bin/env python
#TokyoWesterns CTF 4th 2018 | Cryptography [Revolutional Secure Angou - 156pts]
#@Abdelkader

import gmpy
from gmpy2 import isqrt
from Crypto.Util.number import *

N = 128966395847456823242327968366437151626287005604571543530020807653481854634432463567505579255075400846802686923763465498393221683867550824071176953747390881926123454738359879186455681851356414261155283802414873885574172144840447882087969615781486331849798315912869390710865738157974501171665601011723385435523
e = 65537
#c = open("flag.enc", "rb").read()
#c = c.encode("hex")
c = int("1899b6cd310966281b1593a420205588f12ab93af850ad7d9d810a502f6fe4ad93a58b5bbb747803ba33ac94cc5f227761e72bdd9857b7b0227f510683596791526b9295b20be39567fc9a556663e3b0e3fcc5b233e78e38a06b29314d897258fbe15b037d8ff25d272822571dd98dfa4ee5d066d707149a313ad0c93e79b4ee", 16)

for k in range(1, 100000):
	q = isqrt(k * N / e)         # q = ((k * N) / e) ^ 2
	for q in range(q-100, q+100):
		if N % q == 0:
			print "[+] Found q: ", q
			print "[+] Calculated p: ", N / q
			print "[+] Calculated phi: ", ((N / q) - 1) * (q - 1)
			print "[+] Calculated d: ", gmpy.invert(e, ((N / q) - 1) * (q - 1))
			print "[+] Decrypted flag.encrypted and Found the message m: ", pow(c, gmpy.invert(e, ((N / q) - 1) * (q - 1)), N)
			m = pow(c, gmpy.invert(e, ((N / q) - 1) * (q - 1)), N)
			print "[+] FLAG is: ", long_to_bytes(m)
			break