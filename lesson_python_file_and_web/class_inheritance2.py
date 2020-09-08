from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Student(Person):
    id_no: str

jack = Student("Jack Student", 25, "10100")
jack.age += 1
print(jack)  # Student(name='Jack Student', age=26, id_no='10100')

