import datetime
class Person:
    def __init__(self, name: str, last_name: str, age: int, gender: str, ) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def is_adult(self) -> bool:
        return self.age > 18
    
    def is_senior(self) -> bool:
        return self.age > 65

class BusDriver(Person):
    def __init__(self, name: str, last_name: str, age: int, gender: str, license_expiration_date: datetime) -> None:
        super().__init__(name, last_name, age, gender)
        self.license_expiration_date = license_expiration_date

    def is_license_valid(self) -> bool:
        return self.license_expiration_date > datetime.datetime.now()
    
class Student(Person):
    def __init__(self, name: str, last_name: str, age: int, gender: str, avg_rank: float) -> None:
        super().__init__(name, last_name, age, gender)
        self.avg_rank = avg_rank
    
    def is_scholarship_avail(self, pass_for_scholarship: float): 
        return self.avg_rank > pass_for_scholarship

class HospitalPatient(Person):
    def __init__(self, name: str, last_name: str, age: int, gender: str, insurance_limit: float, current_treatment_payment: float) -> None:
        super().__init__(name, last_name, age, gender)
        self.insurance_limit = insurance_limit
        self.current_treatment_payment = current_treatment_payment

    def total_payment_owed(self) -> float:
        return max(self.current_treatment_payment - self.insurance_limit, 0)

bus_driver_Bob = BusDriver('Bob', 'Smith', 25, 'male', datetime.datetime(2026, 10, 14))
print(f"Bob's Licence: {'Valid' if bus_driver_Bob.is_license_valid() else 'Invalid'}")
print(f"Bob {'has senior bonus' if bus_driver_Bob.is_senior() else 'does not have senior bonus'}")

student_Jane = Student('Jane', 'Harper', 17, 'female', 2.1)
print(f"Jane's Scholarship: {'Valid' if student_Jane.is_scholarship_avail(2.0) else 'Invalid'}")
print(f"Student Jane is {'adult' if student_Jane.is_adult() else 'minor'}")

patient_Jim = HospitalPatient('Jim', 'Clark', 67, 'male', 67500.50, 105000.00)
print(f"Jim owes ${patient_Jim.total_payment_owed()}")



    

