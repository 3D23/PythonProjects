category = input()
category = category.lower()
if (category == 'продукты'):
    price = int(input('Введите цену: '))
    if (price > 0) and (price < 100):
        print('Попробуйте нашу выпечку!')
    elif (price >= 100) and (price < 500):
        print('Как насчёт орехов в шоколаде?')
    elif (price >= 500):
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')