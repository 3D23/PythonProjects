from time import *

print('Удалить с поля?')
seconds = int(input('Введите количество секунд (2 или 10): '))
if (seconds == 2) or (seconds == 10):
    print('Вы удалены с поля на',seconds,'секунд(-ы)')
    sleep(seconds)
    print('Возвращайтесь на поле')