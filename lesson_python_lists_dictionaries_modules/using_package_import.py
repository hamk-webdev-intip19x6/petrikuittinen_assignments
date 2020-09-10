import mypackage.mymath

numbers = (1, 3.14, 2)
print("Average:", mypackage.mymath.average(numbers))

from mypackage import mymath
print("Average:", mymath.average(numbers))

from mypackage.mymath import average
print("Average:", average(numbers))

import mypackage.mymath
print("Average:", mymath.average(numbers))

import mypackage 
print("Average:", mymath.average(numbers))

