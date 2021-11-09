import lab2
import math
import random
import os

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('!!!')
    else:
        return x % m

p = lab2.generate_prime_number(16)
q = lab2.generate_prime_number(16)
n = p * q
print('p = ' + str(p))
print('q = ' + str(q))
print('n = ' + str(n))
t = 0
while t < 1:
    t = int(input('Введите кол-во циклов:'))
users = 0
while users < 1:
    users = int(input('Введите кол-во участников:'))
s_list = []
v_list = []
print()
for i in range(users):
    s = random.randint(2, n - 1)
    s_list.append(s)
    v = pow(modinv(s**2, n), 1, n)
    if i == 0:
        v += 1
    v_list.append(v)
    print(str(i + 1) + ' участник: s = ' + str(s) + ' v = '+ str(v))
good_rounds = 0
for round in range(t):
    print()
    print('Цикл ' + str(round + 1))
    r = random.randint(2, n - 1)
    x = pow(r, 2, n)
    print('P -> V: x = ' + str(x))
    e_list = []
    for j in range(users):
        e_list.append(random.randint(0, 1))
    print('V -> P: e = ' + str(e_list))
    y = r
    for j in range(len(e_list)):
        if e_list[j] == 1:
            y *= s_list[j]
    y = y % n
    print('P -> V: y = ' + str(y))
    y = y**2
    for j in range(len(e_list)):
        if e_list[j] == 1:
            y *= v_list[j]
    y = y % n
    print('V проверяет: y = ' + str(y) + ' и ' + str(x))
    if x == y:
        print('В цикле ' + str(round + 1) + ' проверка пройдена')
        good_rounds += 1
    else:
        print('В цикле ' + str(round + 1) + ' проверка не пройдена!')
        break
print()
if t == good_rounds:
    print('Аутентификация прошла')
else:
    print('Аутентификация не прошла!')
