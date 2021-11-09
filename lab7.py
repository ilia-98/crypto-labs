import lab2
import math
import PrimeRoot
import random
import time
import gost as g

sbox = (
    (4, 10, 9, 3, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 2),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
)

def parity(word, nbits):
    if nbits & (nbits - 1):
        raise ValueError("nbits must be power of two")

    while nbits > 1:
        nbits >>= 1
        word ^= (word >> nbits)
    return word & 1

A_key = 84742541368986481176351458511911
B_key = 27885271873329875145935374569819

A_id = 12928128
B_id = 92745297
Ra = 89858235  # lab2.generate_prime_number(10)
Rb = 38681114  # lab2.generate_prime_number(10)
K = 74298441
print('A передает T: ' + str(Ra))

A_gost = g.GostCrypt(A_key, sbox)
B_gost = g.GostCrypt(B_key, sbox)
T_gost = g.GostCrypt(K, sbox)
message = str(K) + str(A_id)
print(message)
print(parity(message, 64))
text = B_gost.encrypt(message)
print(text)
message = str(Ra) + str(B_id) + str(K) + str(text)
print(message)
#print('длина' + str( len( bin(int(message))[2:] ) ) )
text = A_gost.encrypt(int(message))
print(text)
text = A_gost.decrypt(int(text))
print(text)
#print(T_gost.encrypt(Rb - 1))
