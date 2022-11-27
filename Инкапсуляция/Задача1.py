class BankAccount():
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport

    def getpassport(self):
        return self.__passport

    def getbalance(self):
        return self.__balance

    def setpassport(self, number, password):
        if password == '12345':
            self.__passport = number
            print('Номер изменён')
        else:
            print('Неверный пароль')

    def setbalance(self, summa):
        if self.__balance + summa >= 0:
            self.__balance += summa
        else:
            print('У вас не хватает денег...')

    def delpassport(self, password):
        if password == '12345':
            del self.__passport
            print('Номер удалён')
        else:
            print('Неверный пароль')

account = BankAccount('dfdf', 12345, 234)

print(account.getpassport())
print(account.getbalance())
account.setbalance(1234556)
account.setpassport(7388, '1234')
account.delpassport('12345')