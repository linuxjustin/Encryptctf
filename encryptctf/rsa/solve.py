######Enycrypt########
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import gmpy2
import math


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#p = getPrime(512)
#print p
p = 128966395847456823242327968366437151626287005604571543530020807653481854634432463567505579255075400846802686923763465498393221683867550824071176953747390881926123454738359879186455681851356414261155283802414873885574172144840447882087969615781486331849798315912869390710865738157974501171665601011723385435523
q = 128966395847456823242327968366437151626287005604571543530020807653481854634432463567505579255075400846802686923763465498393221683867550824071176953747390881926123454738359879186455681851356414261155283802414873885574172144840447882087969615781486331849798315912869390710865738157974501171665601011723385435523

q = 9896984395151566492448748862139262345387297785144637332499966426571398040295087125558780121504834847289828037371643927199404615218623314326851473129699891

n = 128966395847456823242327968366437151626287005604571543530020807653481854634432463567505579255075400846802686923763465498393221683867550824071176953747390881926123454738359879186455681851356414261155283802414873885574172144840447882087969615781486331849798315912869390710865738157974501171665601011723385435523
#n = p*q
#print n
e = 65537

c = int("1899b6cd310966281b1593a420205588f12ab93af850ad7d9d810a502f6fe4ad93a58b5bbb747803ba33ac94cc5f227761e72bdd9857b7b0227f510683596791526b9295b20be39567fc9a556663e3b0e3fcc5b233e78e38a06b29314d897258fbe15b037d8ff25d272822571dd98dfa4ee5d066d707149a313ad0c93e79b4ee",16)
# n: 128966395847456823242327968366437151626287005604571543530020807653481854634432463567505579255075400846802686923763465498393221683867550824071176953747390881926123454738359879186455681851356414261155283802414873885574172144840447882087969615781486331849798315912869390710865738157974501171665601011723385435523
#c = 17275020364719491859808371262518015401643882797560517391625392937211284468999473536137439171068285311534877114558180717037464867716162396369965371991546416387963338491642596333571547964509769705052630662877232170395422268807645020606651451420898253995981344276501772409409649660898030555164730710013148509422
fi = (p-1)*(q-1)
d = modinv(e, fi)
print ("%x" % pow(c, d, n)).decode("hex")