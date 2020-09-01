# function which takes arguments and returns something
# perhaps the best kind of function IF it has no side effects
# and the return value only depends on the input parameter
def inches_to_cm(inch):
    return inch * 2.54


# function which takes arguments, but doesn't return anything
def print_many(s, n):
    for i in range(n):
        print(s)


# function which has no arguments, but has a return value
def tell_secret():
    return "The secret is you."


# function without parameters nor return value
def the_end():
    print("This is the end.")


print(inches_to_cm(10))
print_many("hello", 5)
print(tell_secret())
the_end()
