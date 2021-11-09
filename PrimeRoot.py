import math

import numbthy
#import Factorization
#import modpow

def phi_p(n):
    return n - 1

def root(n):
    phi = phi_p(n)
    preCalculatedDeg = [int(phi / i) for i in Factorization.prime_factorization(phi).keys()]
    print("Root search...")
    print(preCalculatedDeg)
    g = 0
    powerRangers = True
    while powerRangers:
        g += 1
        t = False
        for i in preCalculatedDeg:
            if (pow(g, i, n) == 1):
                t = True
                break
        if not t:
           powerRangers = False
    return [g, max(preCalculatedDeg)]

def root_godlike(n):
    preCalculatedDeg = [i[0] for i in numbthy.factor(n-1)]#[int(i) for i in list(Factorization.prime_factorization(n-1).keys())]
    #fil = filter(lambda x: x > 100, preCalculatedDeg)
    arr = []
    for i in range(2, n-1):
        for j in preCalculatedDeg:
            if pow(i, j, n) == 1:
                arr.append(i)
                #return (j, i)
        continue
    return arr
    print('hmm')

def Zpx(q):
    return list(filter(lambda x: math.gcd(x, q) == 1, range(0, q)))

if __name__ == "__main__":
    pass
