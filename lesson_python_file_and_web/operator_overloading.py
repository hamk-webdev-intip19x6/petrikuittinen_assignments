class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"


x = Complex(1, 2)
y = Complex(2, 4)
x = x + y
print(x)  # calling __str__ for human readable version
print(repr(x))  # calling __repr__ for string which allows to recreate object
