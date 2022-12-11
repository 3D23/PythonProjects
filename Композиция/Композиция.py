class Profile:
    def __init__(self, name='', last_name='', age=0, password=''):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.password = password

    def print_info(self):
        print('Имя: ' + self.name)
        print('Фамилия: ' + self.last_name )
        print('Возраст: ', self.age)
        print('Пароль: ' + self.password)

class Adress:
    def __init__(self, city='', street='', zipcode=''):
        self.city = city
        self.street = street
        self.zipcode = zipcode

class Role:
    def __init__(self, role='', hours_worked=0):
        self.role = role
        self.hours_worked = hours_worked

class BankAccount:
    def __init__(self, card_number='', balance=0):
        self.card_number = card_number
        self.balance = balance

class Order:
    def __init__(self):
        self.item = ''
        self.date = ''
        self.delivery = ''
        self.price = 0

    def set_parameters(self, item, date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price

class User:
    def __init__(self, name, last_name, age, password):
        self.profile = Profile(name, last_name, age, password)
        self.address = []
        self.role = []
        self.bank_account = []
        self.order = []

    def set_address(self, city, street, zipcode):
        self.address.append(Adress(city, street, zipcode))

    def set_role(self, role, hours_worked):
        self.role.append(Role(role, hours_worked))

    def set_bank_account(self, card_number, balance):
        self.bank_account.append(BankAccount(card_number, balance))

    def add_order(self, item, date, delivery, price):
        self.order.append(Order().set_parameters(item, date, delivery, price))

