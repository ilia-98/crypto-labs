import random
import math
import sys
import decimal
from random import randrange, getrandbits
import itertools
import PrimeRoot

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


def cyclic_group(n):
    factorlist = list(prime_factors(n))
    print(factorlist)
    finded = False
    while finded == False:
        finded = True
        alpha = generate_prime_candidate(6)
        for p in factorlist:
            print(p)
            b = decimal.Decimal(0)
            b = decimal.Decimal(decimal.Decimal(alpha) ** (decimal.Decimal(n / p)))
            if b == 1:
                finded = False
                break
    return alpha, factorlist


def get_alpha(p, q):
    for i in range(2, p):
        if pow(i, q, p) == 1:
            return i
    return -1


def get_Zq(q):
    return list(filter(lambda x: math.gcd(x, q) == 1, range(0, q)))

def generator(p):
    fact = []
    phi = p - 1
    n = phi
    i = 2
    while i * i <= n:
        if n % i == 0:
            fact.append(i)
            while n % i == 0:
                n /= i
        i = i + 1
    if n > 1:
        fact.append(n)
    res = 2
    while res <= p:
        ok = False
        j = 0
        while j < len(fact):
            if pow(res, int(phi / fact[j]), p) == 1:
                break
            if ok == True:
                return res, fact[j]
            j = j + 1
        res = res + 1
    return -1;


# def cyclic_group(n):
#    factorlist = list(prime_factors(n))
#    print(factorlist)
#    finded = False
#    while finded == False:
#        alpha = generate_prime_candidate(6)
#        for p in factorlist:
#            print(p)
#            b = decimal.Decimal(0)
#            b = decimal.Decimal(decimal.Decimal(alpha) ** (decimal.Decimal(n / p)))
#            if b == 1:
#                break
#        finded = True
#    return alpha, factorlist


user_count = 3
print('Кол-во участников - ' + str(user_count))
x = 71
print('Открытый текст - ' + str(x))
p = generate_prime_number(32)
factorlist = list(prime_factors(p - 1))
q = factorlist[len(factorlist) - 1]
alpha = get_alpha(p, q)
print('p - ' + str(p))
print('q - ' + str(q))
print('alpha - ' + str(alpha))
a_list = []
b_list = []
b = 1
for i in range(user_count):
   ai = generate_prime_number(8)
   a_list.append(ai)
   bi = pow(alpha, ai, p)
   print('Секретный ключ ' + str(i+1) + ' участника - ' + str(ai) + '. Открытый ключ ' + str(i + 1) + ' участника - ' + str(bi))
   b_list.append(bi)
   b *= bi
   b = b % p
print('b - ' + str(b))
print('Подписание:')
k_list = []
y1i_list = []
y1 = 1
for i in range(user_count):
    ki = random.choice(get_Zq(q))
    print('Участник '+ str(i + 1) + ' сгенерировал k - '  + str(ki))
    k_list.append(ki)
    y1i = pow(alpha, ki, p)
    print('Участник ' + str(i + 1) + ' вычислил y1 - ' + str(y1i))
    y1i_list.append(y1i)
    y1 *= y1i
    y1 = y1 % p
E = (y1 * x) % q
print('E - ' + str(E))
y2i_list = []
y2 = 0
for i in range(user_count):
    y2i = (k_list[i] - a_list[i] * E) % q
    print('Участник ' + str(i + 1) + ' вычислил y2 - ' + str(y2i))
    y2i_list.append(y1i)
    y2 += y2i
    y2 %= q
print('y1 - ' + str(y1))
print('y2 - ' + str(y2))
print('Верификация:')
buf1 = pow(b, y1*x, p)
buf2 = pow(alpha, y2, p)
buf3 = (buf1 * buf2) % p
if buf3 == y1:
    print('Проверка пройдена - ' + str(buf3) + ' = ' + str(y1) )
else:
    print('Проверка не пройдена - ' + str(buf3) + ' = ' + str(y1))