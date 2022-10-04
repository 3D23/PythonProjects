def discount(_score):
    if (_score >= 0) and (_score <= 49):
        print('Ваша скидка: 10%')
        return True
    elif (_score >= 50) and (_score <= 99):
        print('Ваша скидка: 15%')
        return True
    elif (_score >= 100):
        print('Ваша скидка: 10%')
        return True
    else:
        print('Количество баллов не может быть отрицательным числом.')
        return False

flag = False
while (flag == False):
    score = int(input('Введите количество баллов: '))
    flag = discount((score))
