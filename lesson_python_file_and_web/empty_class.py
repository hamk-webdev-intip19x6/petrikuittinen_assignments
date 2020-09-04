class Person:
    pass    # empty class acts as a dictionary like container

jack = Person() # create new instance of class Person, notice now new keyword
jack.name = "Jack Smith"
jack.age = 24
bob = Person()
bob.name = "Bob Paxton"
bob.age = 66
jill = Person()
jill.name = "Jill Taylor"
jill.age = 21
jill.address = "Example Street 12"
persons = [jack, bob, jill]
for person in persons:
    person.age += 1
    print(person.name, person.age, end='')
    if hasattr(person, "address"):
        print("", person.address)
    else:
        print()

