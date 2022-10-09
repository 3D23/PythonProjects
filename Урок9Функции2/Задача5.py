def F5(_colors,_count):
    dictionary = {}
    for i in range(count):
        key = input('Введите цвет')
        value = input('Введите его HEX-значение')
        dictionary[key] = value
    return(dictionary)

colors = 'Цвета'
count = int(input('Введите количество цветов: '))
print(F5(colors,count))