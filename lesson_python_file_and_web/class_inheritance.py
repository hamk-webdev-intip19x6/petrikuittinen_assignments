class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Person(%s, %d)" % (self.name, self.age)

class Student(Person):
    def __init__(self, name, age, id):
        # in Python2 super(Student, self).__init__(name,age)
        super().__init__(name, age)
        self.id = id
    def __str__(self):
        return "Student(%s, %d, %s)" % (self.name, self.age, self.id)

jack = Student("Jack Student", 25, "10100")
jack.age += 1
print(jack)

