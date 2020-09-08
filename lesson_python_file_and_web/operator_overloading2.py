from __future__ import annotations  # for forward references
from dataclasses import dataclass

@dataclass
class Complex:
    real: float
    imag: float

    def __add__(self, other: Complex) -> Complex:
        return Complex(self.real + other.real, self.imag + other.imag)

x = Complex(1, 2)
y = Complex(2, 4)
x = x + y
print(x)

