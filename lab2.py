import PrimeRoot
import random
import math
import sys
import decimal
from random import randrange, getrandbits
import numbthy
import itertools

def root(n):
    preCalculatedDeg = [i[0] for i in numbthy.factor(n-1)]
    #fil = filter(lambda x: x > 100, preCalculatedDeg)
    for i in range(2, n-1):
        for j in preCalculatedDeg:
            if pow(i, j, n) == 1:
                return (j, i)
        continue
    print('hmm')

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

def main():
    p = generate_prime_number(32)
    g = root(p)[1]
    x = random.randint(2, p - 1)
    c = random.randint(0, 1)

    #p_list = [23,59,43,43,67,107,167,211,263,347]
    #g_list = [5,2,3,3,2,2,5,2,5,2]
    #b_list = [1,1,1,0,1,0,0,1,0,0]
    #x_list = [11,29,37,22,7,2,50,123,142,270]


    print('p - ' + str(p))
    print('g - ' + str(g))
    odd = x % 2
    print('x - ' + str(x) + ', нечетность - ' + str(odd))
    y = pow(g, x, p)
    print('A -> B: y - ' + str(y))
    print('B -> A: b - ' + str(random.randint(0,1)))
    print('A -> B: x - ' + str(x))
    yB = pow(g, x, p)
    if y == yB:
        print('Проверка прошла - ' + str(yB) + ' = ' + str(y) )
    else:
        print('Проверка не прошла - ' + str(yB) + ' != ' + str(y))