sale = int(input('Введите скидку:'))
amount = int(input('Введите стоимость:'))
while (amount != 0):
    answer = amount*sale/100
    print('Скидка: ',sale,'%, Цена: ',answer)
    amount = int(input('Введите стоимость:'))