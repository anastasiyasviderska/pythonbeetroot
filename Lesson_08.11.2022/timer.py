from time import time
class Employee:
    def __init__(self, name, age, gender, end_time):
        self.start_time = 0
        self.end_time = end_time
        self.total_hours = 0
        self.salary = 0

    def start_working(self):
        self.start_time = time()
        print("Welcome to work!")

    def end_working(self):
        self.end_time = int(input("Please enter your end time: "))
        self.total_hours += (self.start_time - self.end_time ) / 1000
        print(f"Your computer has been hacked :): {self.end_time}")
        self.salary += self.total_hours / 20

class ListOfEmployees:
    def __init__(self):
        self.list_of_employees = ''

    def add_employee(self, employee: Employee):
        self.list_of_employees.append(employee)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list_of_employees):
            temp_index = self.index
            self.index += 1
            return self.list_of_employees[temp_index]
        else:
            raise StopIteration