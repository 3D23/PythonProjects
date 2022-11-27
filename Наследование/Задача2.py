class Class_one():
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name + '- гений')

class Class_two(Class_one):
    def print_class_two(self):
        super().print()
        print('Но его отчислять если он не будет учить ООП')

class_two = Class_two('Дима')
class_two.print_class_two()