import unittest
class Person:
    def __init__(self, name: str, last_name: str, age: int, gender: str, ) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def __hash__(self) -> int:
        return hash(self.name) ^ hash(self.last_name)

class ToDoTestCase(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Bob", "Johnson", 22, "male")
        self.person_2 = Person("Jane", "Johnson", 32, "female")
        self.person_3 = Person("Bob", "Johnson", 53, "male")

    def test_hash_equal(self):
        self.assertEqual(hash(self.person_1), hash(self.person_3))
    
    def test_hash_not_equal(self):
        self.assertNotEqual(hash(self.person_1), hash(self.person_2))

if __name__ == '__main__':
    unittest.main()




