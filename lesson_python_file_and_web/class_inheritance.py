class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person('{self.name}', {self.age})"

class Student(Person):
    def __init__(self, name, age, id_no):
        # in Python2 super(Student, self).__init__(name,age)
        super().__init__(name, age)
        self.id_no = id_no
    def __str__(self):
        return f"Student('{self.name}', {self.age}, '{self.id_no}')"

jack = Student("Jack Student", 25, "10100")
jack.age += 1
print(jack)  # Student('Jack Student', 26, '10100')
jill = Student("Jill Student", 23, "10101")
jill.name = "Jill Taylor"
print(jill)
jill.address = "Example Street 12"
print(jill.address)
