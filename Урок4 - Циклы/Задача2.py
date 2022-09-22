begin = input('Введите game чтобы начать:')
count = 0
if (begin == 'game'):
    button = ''
    while count != 3:
        number = (input('Введите число (off завершить)'))
        if (number == 'off'):
            break
        count += 1
        if (int(number) == 5):
            print('Вы выиграли')
            break
if (count == 3):
    print('вы проиграли')



