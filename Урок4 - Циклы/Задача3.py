mail = input('Введите логин:')
symbols = '=?*^$№@_'
for i in symbols:
    if (i in mail):
        print('Запрещенный символ: ',i)