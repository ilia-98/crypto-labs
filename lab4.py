import lab2
import math
import random
import os
import shutil

def get_C(p):
    c = random.randint(2, p - 1)
    while math.gcd(c, p - 1) != 1:
        c = random.randint(2, p - 1)
    return c


def get_D(c, p):
    d = random.randint(2, p - 1)
    while pow(c * d, 1, p - 1) != 1:
        d = random.randint(2, p - 1)
    return d


cards = {
    101: '2 бубен', 102: '3 бубен', 103: '4 бубен', 104: '5 бубен', 105: '6 бубен', 106: '7 бубен', 107: '8 бубен',
    108: '9 бубен', 109: '10 бубен', 110: 'Валет бубен', 111: 'Дама бубен', 112: 'Король бубен', 113: 'Туз бубены',

    201: '2 червей', 202: '3 червей', 203: '4 червей', 204: '5 червей', 205: '6 червей', 206: '7 червей', 207: '8 червей',
    208: '9 червей', 209: '10 червей', 210: 'Валет червей', 211: 'Дама червей', 212: 'Король червей', 213: 'Туз червей',

    301: '2 треф', 302: '3 треф', 303: '4 треф', 304: '5 треф', 305: '6 треф', 306: '7 треф', 307: '8 треф',
    308: '9 треф', 309: '10 треф', 310: 'Валет треф', 311: 'Дама треф', 312: 'Король треф', 313: 'Туз треф',

    401: '2 пик', 402: '3 пик', 403: '4 пик', 404: '5 пик', 405: '6 пик', 406: '7 пик', 407: '8 пик',
    408: '9 пик', 409: '10 пик', 410: 'Валет пик', 411: 'Дама пик', 412: 'Король пик', 413: 'Туз пик',
}
deck = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
        201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213,
        301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313,
        401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413]
h = 10
p = lab2.generate_prime_number(16)
n = 0
while n < 2 or n > 5:
    n = int(input('Введите кол-во игроков:'))
c_list = []
d_list = []
users_cards = []
print('p - ' + str(p))
print('Колода: ' + str(deck) + '\n')
shutil.rmtree('deck', ignore_errors=True)
os.makedirs('deck')

for player in range(n):
    c = get_C(p)
    d = get_D(c, p)
    print(str(player + 1) + ' игрок: c - ' + str(c) + ', d - ' + str(d))
    c_list.append(c)
    d_list.append(d)
    for card in range(len(deck)):
        deck[card] = pow(deck[card], c_list[player], p)
    random.shuffle(deck)
    print('Колода: ' + str(deck) + '\n')


for player in range(n):
    top_deck = deck[0:h]
    del deck[0:h]
    print(str(player + 1) + ' игрок вытянул 10 карт: ' + str(top_deck))
    for other_player in range(n):
        if other_player != player:
            for card in range(len(top_deck)):
                top_deck[card] = pow(top_deck[card], d_list[other_player], p)
            print(str(other_player + 1) + ' игрок снял свой множитель: ' + str(top_deck))

    for card in range(len(top_deck)):
        top_deck[card] = pow(top_deck[card], d_list[player], p)
    print(str(player + 1) + ' игрок снял свой множитель: ' + str(top_deck))
    with open('deck/' + str(player) + 'игрок.txt', 'w') as file_handler:
        for card in range(len(top_deck)):
            file_handler.write(cards[top_deck[card]] + '\n')
    print('Карты в колоде: ' + str(deck) + '\n')

#print('Карты в прикупе: ', end = '')
#for card in range(len(deck)):
#    print(cards[top_deck[card]], end = ', ')


#сначала карты идут по куругу и все участники покрывают их своими множиителями и мешают
#на втором круге участник вытягивает 10 карт, каждый участник снимает с карт свои множители
# и в конце снимает свой множитель,  мешает и передает дальше