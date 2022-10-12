from random import randint

sbornaya1 = []
sbornaya2 = []
count1 = int(input('Введите количество участников в первой сборной: '))
count2 = int(input('Введите количество участников во второй сборной: '))
sport1 = randint(1, count1)
sport2 = randint(1, count2)
print('Пловец ',sport1,' - ','Пловец ',sport2)