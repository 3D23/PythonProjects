def imt(_weight,_height):
    _index = _weight/(_height**2)
    return _index

def imt_analyse(_index_analyse):
    if (_index_analyse < 18.5):
        print('Недостаточный вес')
    elif (_index_analyse >= 18.5) and (_index_analyse <= 25):
        print('ИМТ в норме')
    else:
        print('Избыточный вес')

weight = int(input('Введите ваш вес: '))
height = int(input('Введите ваш рост:' ))
while (weight <= 0):
    print('Вес не может быть отрицательным.')
    weight = int(input('Введите ваш вес: '))
while (height <= 0):
    print('Рост не может быть отрицательным.')
    height = int(input('Введите ваш рост: '))
index = imt(weight,height)
imt_analyse(index)