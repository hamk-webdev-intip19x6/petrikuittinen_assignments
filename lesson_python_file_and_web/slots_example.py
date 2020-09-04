class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

m = MyClass("name", "id")
m.age = 100
print(m.age)

# Same with slots
class MyClass2(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

m = MyClass2("name", "id")
m.age = 100  # will fail!
