dictionary = {'1':1,'2':2,'3':3,'4':4,'5':5}
dictionary['1'],dictionary['5'] = dictionary['5'],dictionary['1']
del dictionary['2']
dictionary['new_key'] = 'new_value'
print(dictionary)
