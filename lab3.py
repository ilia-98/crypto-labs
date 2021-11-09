import lab2
import random
import numpy
from functools import reduce
from operator import mul, sub
import copy
import numpy as np
from fractions import Fraction
np.seterr(divide='ignore', invalid='ignore')



def matrix_mod(matrix, b, p, row_count):
    for i in range(row_count):
        for j in range(row_count):
           matrix[i][j] = pow(int(matrix[i][j]), 1, p)
           matrix[i][j] += p if matrix[i][j] < 0 else 0
        b[i] = pow(int(b[i]), 1, p)
        b[i] += p if b[i] < 0 else 0
    return matrix, b

def createone(matrix, b, p, sort_index, row_count):
    matrix, b = matrix_mod(matrix, b, p, row_count)
    j = 1
    koef = matrix[sort_index][sort_index]
    while pow(koef, 1, p) != 1:
        koef = matrix[sort_index][sort_index]
        j += 1
        koef *= j
    for i in  range(sort_index, row_count):
        matrix[sort_index][i] = pow(j * matrix[sort_index][i], 1, p)
    b[sort_index] = pow(j * b[sort_index], 1, p)
    return matrix, b

def gauss(matrix, b, p):
    row_count = len(matrix)

    for i in range(row_count - 1):
        if matrix[i][i] != 0:
            matrix, b = createone(matrix, b, p,i, row_count)
            for j in range(i + 1, row_count):
                mult_element = matrix[j][i] / matrix[i][i]
                for k in range(i, row_count):
                    matrix[j][k] -= matrix[i][k] * mult_element
                b[j] -= b[i] * mult_element
            matrix, b = matrix_mod(matrix, b , p, row_count)

    matrix, b = createone(matrix, b, p, row_count - 1, row_count)
    for i in range(row_count - 1, 0, -1):
        if matrix[i][i] != 0:
            for j in range(i - 1, -1, -1):
                mult_element = matrix[j][i] / matrix[i][i]
                matrix[j][i] -= matrix[i][i] * mult_element
                b[j] -= b[i] * mult_element
            matrix, b = matrix_mod(matrix, b, p, row_count)
    return matrix, b


n = 7
k = 3
m = 111
p = lab2.generate_prime_number(16)
print('m - ' + str(m))
print('p - ' + str(p))
print('n - ' + str(n))
print('k - ' + str(k))
x_list = []
print('\nПодготовительная фаза:')
print('Q = (' + str(m), end='')
for i in range(k - 1):
    x = random.randint(2, p - 1)
    x_list.append(x)
    print(', ' + str(x),end='')
print(')')
print('\nФаза раздачи секрета:')
a_list = []
b_list = []
for i in range(n):
    a_list.append([])
    a = random.randint(2, p - 1)
    a_list[i].append(a)
    b = a * m
    for j in range(k - 1):
        a = random.randint(2, p - 1)
        a_list[i].append(a)
        b += a * x_list[j]
    b = b % p
    b_list.append(b)
    print('Участник ' + str(i + 1) + ' получил b = ' + str(b) + '  a = ' + str(a_list[i]))
print('')
for i in range(n):
    print(str(a_list[i][0]) + '*' + str(m), end='')
    for j in range(k - 1):
        print(' + '+str(a_list[i][j + 1]) + '*' + str(x_list[j]), end = '')
    print(' = ' + str(b_list[i]) + ' mod ' + str(p))

print('\nФаза восстановления секрета:\n')


#print(a_list[0:k])
#print(b_list[0:k])
#M1 = numpy.array(a_list[0:k], dtype='float')
#v1 = numpy.array(b_list[0:k])
#a_list[0].append(b_list[0])
#a_list[1].append(b_list[1])
#a_list[2].append(b_list[2])
#a_list[3].append(b_list[3])
#print(numpy.linalg.solve(M1, v1))


while True:
    users = input('Введите номера участников восстановления:')
    users = users.split(' ')
    if len(users) < k:
        print('Недостаточно участников')
    else:
        break
users_a = []
users_b = []
if len(users) > k:
    users = users[0:k]
for i in range(len(users)):
    print('Участник ' + users[i] + ' учавствует в восстановлении, его параметры b = ' + str(b_list[int(users[i]) - 1]) + '  a = ' + str(a_list[int(users[i]) - 1]))
    users_a.append(a_list[int(users[i]) - 1])
    users_b.append(b_list[int(users[i]) - 1])
print('')
for i in range(len(users)):
    print(str(users_a[i][0]) + '*' + 'x', end='')
    for j in range(k - 1):
        print(' + '+str(users_a[i][j + 1]) + '*' + 'x', end = '')
    print(' = ' + str(users_b[i]) + ' mod ' + str(p))

matrix, b = gauss(users_a,users_b,p)
print('\n'+str(b))