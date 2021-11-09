import lab2
import math
import PrimeRoot
import random
import time


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if math.gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
                                                           for powers in range(1, modulo)}]


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


def modm(a, m):
    res = 1
    key = True
    while key == True:
        if pow(res * a, 1, m) == 1:
            key = False
        else:
            res += 1
    return res

primitives = []
while len(primitives) < 10:
    p = lab2.generate_prime_number(10) # 941 #521
    q = lab2.generate_prime_number(10) # 751 #677
    n = p * q
    primitives = PrimeRoot.root_godlike(n)
print('p = ' + str(p))
print('q = ' + str(q))
print('n = ' + str(n))
#print(primitives)
users = 0
k = 0
while users < 1:
    users = int(input('Введите кол-во участников: '))
while k < 1:
    k = int(input('Введите кол-во наборов сообщений: '))
print()
C_list = []
F_list = []
for i in range(users):
    c_user_list = []
    f_user_list = []
    for j in range(k):
        C = random.choice(primitives)
        c_user_list.append(C)
        F = pow(modinv(C, n), 1, n)
        f_user_list.append(F)
    C_list.append(c_user_list)
    F_list.append(f_user_list)
    print(str(i + 1) + ' участник: C: ' + str(c_user_list) + ' F: ' + str(f_user_list))

fi = phi(n)
d = random.randint(2, fi)
flag = False
e = 1
while flag != True:
    try:
        e = pow(modinv(d, fi), 1, fi)
        flag = True
    except:
        d = random.randint(2, fi)
print('d = ' + str(d))
print('e = ' + str(e))
answers = [2, 3]

B_list = []
L_list = []
votes = []
for i in range(users):
    user_answer = int(input('\n Выбирите вариант ответа: Да - 2, Нет - 3: '))
    print(str(i + 1) + ' участник формируют наборы сообщений')
    b_user_list = []
    for index in range(k):
        temp = answers.copy()
        random.shuffle(temp)
        b_user_list.append(temp)
    B_list.append(b_user_list)
    print(str(i + 1) + ' участник: набор сообщений B: ' + str(b_user_list))

    print(str(i + 1) + ' участник накладывает затемняющие множители')
    l_user_list = []
    for index in range(k):
        h_list = []
        for m in range(len(B_list[i][index])):
            h_list.append(pow((C_list[i][index] ** d) * B_list[i][index][m], 1, n))
        l_user_list.append(h_list)
    L_list.append(l_user_list)
    print(str(i + 1) + ' участник: набор сообщений L: ' + str(l_user_list))
    print(str(i + 1) + ' участник передает T свои L')
    J = random.randint(1, k)
    print(str(i + 1) + ' участник получает от T номер сообщения, который T хочет подписать: ' + str(J))
    print(str(i + 1) + ' участник раскрывает T свои маск. множители: ' + str(F_list[i][:J - 1]) + str(F_list[i][J:]))
    T_B_list = []
    for index in range(k):
        temp = []
        if index != J - 1:
            for m in range(len(L_list[i][index])):
                temp.append(pow((F_list[i][index] ** d) * L_list[i][index][m], 1, n))
        T_B_list.append(temp)
    print('T снимает маск. множители с сообщений ' + str(i + 1) + ' участника: ' + str(T_B_list))
    R_list = []
    for m in range(len(L_list[i][J - 1])):
        R_list.append(pow(L_list[i][J - 1][m], e, n))
    print('T передает R '+ str(i + 1) + ' участнику: ' + str(R_list))
    S_list = []
    for m in range(len(R_list)):
        S_list.append(pow(R_list[m] * F_list[i][J - 1], 1, n))
    print(str(i + 1) + ' участник снимает с R маск. множители: ' + str(S_list))
    answer_index = B_list[i][J - 1].index(user_answer)
    print(str(i + 1) + ' участник выбрал: ' + str(S_list[answer_index]))
    print(str(i + 1) + ' участник передает T сообщение: (' +str(user_answer) + ', ' + str(S_list[answer_index]) + ')')
    if pow(S_list[answer_index], d, n) == user_answer:
        print('T проверяет сообщение: проверка пройдена, голос засчитан')
        votes.append(user_answer)
    else:
        print('T проверяет сообщение: проверка не пройдена, голос не засчитан')


print('Голосов Да: ' + str(votes.count(2)) + '\n' + 'Голосов Нет: ' + str(votes.count(3)))