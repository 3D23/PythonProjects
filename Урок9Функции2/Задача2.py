def F2(_distance):
    amount = 4
    help = _distance // 140
    return 4 + 0.25*help

distance = int(input('Введите расстояние: '))
print(F2(distance))