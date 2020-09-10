def safe_divide(func):
    def inner(a, b):
        print("Trying to divide", a, "by", b)
        if b == 0:
            print("Division by Zero")
            return
        return func(a, b)

    return inner


@safe_divide
def divide(a, b):
    print(a / b)


divide(7, 2)
divide(5, 0)
