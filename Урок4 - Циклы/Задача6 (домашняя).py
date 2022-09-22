price = int(input('Введите цену товара: '))
amount = 0
while (price > 0):
    amount += price
    price = int(input('Введите цену товара: '))
if (amount == 0):
    print('Вы ничего не купили.')
    exit()
if ((amount%2) == 0):
    while ((amount%2) == 0):
        amount /= 2
    print('К оплате:',amount)
elif ((amount%2) != 0):
    print('К оплате:',amount)

