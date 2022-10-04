class Dog:
    age_factor = 7
    def __init__(self, dog_age) -> None:
        self.dog_age = dog_age
    
    def human_age(self):
        return self.age_factor * self.dog_age
    
bubble = Dog(5)

print(bubble.human_age())