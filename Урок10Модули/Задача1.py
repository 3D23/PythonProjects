from time import *

def F1 (begin,timem,times):
    while timem != 0:
        h = input('Сделайте ход (off - завершить работу): ')
        if (h == 'off'):
            exit()
        else:
            end = time()
            minutes = round((times - (end - begin))//60) + 1
            print('Оставшееся время в минутах: ',minutes,'м')
            timem = minutes
            return timem

timem = 30
times = 1800
h = ''
begin = time()
while (timem != 0):
    timem = F1(begin,timem,times)