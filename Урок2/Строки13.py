S = input()
line1,line2 = S.split('@')
rInd = line1.rindex(' ')
ind = line2.index(' ')
mail1 = line1[rInd+1::]
mail2 = line2[:ind:]
mail = mail1 + '@' + mail2
print(mail)