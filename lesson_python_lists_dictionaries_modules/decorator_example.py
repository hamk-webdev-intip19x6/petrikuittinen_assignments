def safe_divide(func):
    def inner(a, b):
        print("Trying to divide", a, "and", b)
        if b == 0:
            print("Division by Zero")
            return
        return func(a, b)

    return inner


@safe_divide
def divide(a, b):
    print(a / b)


print(divide(7, 2))
print(divide(5, 0))
