s = input('Введите строку, состоящую из скобок: ')
length = 1
maxlen = 0
for i in range(0,len(s)-1):
   if (length % 2 != 0) and (s[i] == '(') and (s[i+1] == ')'):
       length += 1
       if (length > maxlen):
           maxlen = length
   elif (length % 2 == 0) and (s[i] == ')') and (s[i+1] == '('):
       length += 1
       if (length > maxlen):
           maxlen = length
   else:
       length = 1
print(maxlen // 2)
