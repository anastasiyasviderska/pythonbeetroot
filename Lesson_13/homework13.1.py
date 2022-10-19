class Person:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.age} {self.gender} "

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, hours: int, rate_per_hour: float) -> None:
        super().__init__(first_name, last_name, age, gender)
        self.hours = hours
        self.rate_per_hour = rate_per_hour
    
    def salary(self):
        return self.hours * self.rate_per_hour
    
    def __str__(self) -> str:
        return super().__str__() + str(self.salary())

class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, rank_subject: list) -> None:
        super().__init__(first_name, last_name, age, gender)
        self.rank_subject = rank_subject
    
    def average_rank_all_subjects(self):
        if len(self.rank_subject) == 0:
            return 0
        return sum(self.rank_subject)/len(self.rank_subject)
    
    def __str__(self) -> str:
        return super().__str__() + str(self.average_rank_all_subjects())

teacher_1 = Teacher('John', 'Smith', 50, 'male', 40, 45.5)
assert(str(teacher_1) == 'John Smith 50 male 1820.0')

student_1 = Student('Alex', 'Bush', 20, 'male', [4, 3, 2, 1, 1, 1])
assert(str(student_1) == 'Alex Bush 20 male 2.0') 



        

