from random import randint
from time import *

count1 = 0
count2 = 0
i = input('Введите имя участника (off - завершить работу): ')
while i != 'off':
    number = randint(1,2)
    sleep(1)
    print('Ваш номер: ',number)
    if (number == 1):
        count1 += 1
    else:
        count2 += 1
    sleep(1)
    print('Участников в первом забеге: ',count1,'. Участников во втором забеге: ',count2)
    sleep(1)
    i = input('Введите имя участника (off - завершить работу): ')
sleep(1)
print()
print('Участников в первом забеге: ',count1,'. Участников во втором забеге: ',count2)