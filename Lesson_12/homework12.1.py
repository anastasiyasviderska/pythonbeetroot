class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old")
    

person_call = Person("Alex", "Johnson", 25)
person_call.talk()
       