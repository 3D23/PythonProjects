S = input('Введите числа через пробел: ')
A,B,C,D,E,F,G = (S.split(' '))
a = int(A)
b= int(B)
c = int(C)
d = int(D)
e = int(E)
f = int(F)
g = int(G)
answer = a + b + c
if (g != 0) and (g <= a) and (g <= b) and (g <= c):
    answer -= 2*g
    a -= g
    b -= g
    c -= g
if (d != 0) and (d <= a) and (d <= b):
    answer -= d
    a -= d
    b -= d
if (e != 0) and (e <= a) and (e <= c):
    answer -= e
    a -= e
    c -= e
if (f != 0) and (f <= b) and (f <= c):
    answer -= f
    b -= f
    c -= f
print(answer)
