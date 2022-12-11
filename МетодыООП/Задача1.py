from datetime import date

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(self.name)
        print(self.age)

    @classmethod
    def generation(cls, year):
        return Person('Дима', date.today().year - year)

    @staticmethod
    def check_age(age):
        if age >= 18:
            return 'Является совершеннолетним'
        return 'Не является совершеннолетним'

dima_one = Person('lvcv', 20)
dima_two= dima_one.generation(1980)
print(dima_one.check_age(dima_one.age))
print(dima_two.check_age(dima_two.age))
