def score_sum(_count):
    _sum = 0
    for _i in range(_count):
        _score = input('Введите количество баллов (в диапозоне от 0 до 50): ')
        if (_score.lower() == 'stop'):
            return _score
        while (int(_score) < 0) or (int(_score) > 50):
            print('Нужно вести количество баллов в диапозоне от 0 до 50')
            _score = input('Введите количество баллов (в диапозоне от 0 до 50): ')
            if (_score.lower() == 'stop'):
                return _score
        _sum += int(_score)
    return _sum

def score_sum_analyse(_sum_analyse):
    if (_sum_analyse > 80):
        print('Наградить дипломом.')
    elif (_sum_analyse > 50) and (_sum_analyse <= 80):
        print('Наградить похвальной грамотой.')
    else:
        print('Выдать грамоту об участии.')

s = input(('Введите имя студента и количество предметов (через пробел) (stop для остановки)'))
while (s.lower() != 'stop'):
    name, c = s.split(' ')
    count = int(c)
    sum = score_sum(count)
    if (sum == 'stop'):
        s = sum
    else:
        print('Итоговый счёт: ',sum)
        score_sum_analyse(sum)
        s = input(('Введите имя студента и количество предметов (через пробел) (stop для остановки)'))
