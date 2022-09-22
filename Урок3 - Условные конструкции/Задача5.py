Number = int(input())
if ((Number%10)%2 == 0) and (sum(map(int,str(Number)))%3 == 0):
    print('Делится')
else:
    print('Не делится')