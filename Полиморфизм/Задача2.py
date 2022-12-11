class Olympiad_tasks():
    def __init__(self, lastname, number_of_tests, number_of_tests_passed):
        self.lastname = lastname
        self.number_of_tests = number_of_tests
        self.number_of_tests_passed = number_of_tests_passed

class All_or_nothing(Olympiad_tasks):
    def __init__(self, lastname, number_of_tests, number_of_tests_passed, number_of_point):
        super().__init__(lastname, number_of_tests, number_of_tests_passed)
        if self.number_of_tests == self.number_of_tests_passed:
            self.number_of_point = number_of_point

class The_sooner_the_better(Olympiad_tasks):
    def __init__(self, time):



