def timetable():
    print('Пн - 07:00 - 21:00')
    print('Ср - 07:00 - 21:00')
    print('Сб - 07:00 - 21:00')

def price():
    print('Цена за тренировку: 500р')

def number():
    print('+7 (777)-228-23-23')

def location():
    print('Сириус Арена')

def record1():
    rec = input('На какой день хотите записаться? (1- Понедельник, 2 - Среда, 3 - Суббота) off - выйти')
    if rec == '1' or rec == '2' or rec == '3':
        record2()
    elif rec == 'off':
        return
    else:
        print('Не работаем в этот день.')
        record1()

def record2():
    rec2 = input('На какое время хотите записаться? (работаем с 07:00 до 21:00) off - выйти')
    if (rec2[0] + rec2[1] >= '07') and (rec2[-5] + rec2[-4] <= '21'):
        print('Запись сделана.')
    elif rec2 == 'off':
        return
    else:
        print('Не работаем в такое время.')
        record2()

def main(request):

    timetable_l = ['расп', 'график','когд']
    price_l = ['плат','цен','деньг','стои']
    number_l = ['телеф', 'ном','конт','трен']
    location_l = ['наход', 'мест', 'где', 'локац']
    record_l = ['запис', 'пойт', 'абонем']

    for i in range(len(timetable_l)):
        if timetable_l[i] in request.lower():
            timetable()
            return

    for i in range(len(location_l)):
        if location_l[i] in request.lower():
            location()
            return

    for i in range(len(price_l)):
        if price_l[i] in request.lower():
            price()
            return

    for i in range(len(number_l)):
        if number_l[i] in request.lower():
            number()
            return

    for i in range(len(record_l)):
        if record_l[i] in request.lower():
            record1()
            return




