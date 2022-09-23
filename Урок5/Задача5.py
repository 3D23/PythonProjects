numbers = [2]
increases = True
for i in range(1,len(numbers)):
    if (numbers[i] - numbers[i-1] != 1):
        increases = False
    if (increases == False):
        break
if (len(numbers) == 1):
    increases = False
if (increases == True):
    print('Да')
else:
    print('Нет')