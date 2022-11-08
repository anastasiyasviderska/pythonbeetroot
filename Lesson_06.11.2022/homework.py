from datetime import datetime, timedelta

class Animal:

    list_of_animals = []

    def __init__(self, kind, name, age):

        self.kind = kind
        self.name = name
        self.age = age
        self.list_of_animals.append(self)

    def __str__(self):
        return 'This is a {} named {} {} years old'.format(
                                                        self.kind,
                                                        self.name,
                                                        self.age)

    def __repr__(self):
        return 'Animal("{}", "{}", {})'.format(
                                            self.kind,
                                            self.name,
                                            self.age)

    @property
    def vaccinated(self) -> bool:
        if self.kind in ['dog', 'cat']:
            last_vaccination = getattr(self, 'vaccination_date', self.n_years_ago(int(self.age)))
            return last_vaccination >= self.year_ago()
        else:
            raise ValueError

    @classmethod        
    def print_list_of_animals(cls):
        print('-'*80)
        for animal in cls.list_of_animals:
            try:
                vaccination = 'vacination is valid' if animal.vaccinated else 'not vaccinated, please, vaccinate'
                print(f"Kind: {animal.kind}, Name: {animal.name},  Age: {animal.age}, Vaccination: {vaccination}")
            except ValueError:
                print(f"Kind: {animal.kind}, Name: {animal.name},  Age: {animal.age}")
        print('-'*80)

                
    @classmethod
    def dog(cls):
        name = input('Your dog name is ')
        age = input('How old is it? ')
        size = input('Size of your dog: ')
        dog = cls('dog', name, age)
        dog.size = size
        return dog

    @classmethod
    def cat(cls):
        name = input('Your cat name is ')
        age = input('How old is it? ')
        cat = cls('cat', name, age)
        return cat

    @staticmethod
    def year_ago():
        return datetime.now() - timedelta(days=365)

    @staticmethod
    def n_years_ago(age: int):
        return datetime.now() - timedelta(days=365*age)

    def get_vaccinated(self):
        try:
            if not self.vaccinated:
                self.vaccination_date = datetime.now()
                print('puff')
        except ValueError:
            print("We will not vaccinate your animal!")


if __name__ == '__main__':

    the_dog = Animal.dog()
    the_humster = Animal('humster', 'Mike', 2)
    Animal.print_list_of_animals()

    the_dog.get_vaccinated()
    the_humster.get_vaccinated()

    Animal.print_list_of_animals()
