import myutil
# NOTICE: no .py needed here, just the part before .py
# if you import like this each module has its own name space
# and must be prefixed like below
x = myutil.ask_float("Give me a float?")
print(x)

from myutil import ask_float, lbs_to_kg
# if you import like this then the name is copied to the local name space
# and no prefix is required
x = ask_float("Give me a float?")
print(lbs_to_kg(x))

from myutil import *
# Copy all names from the module to current name space
# WARNING: Do NOT use this often, because local name space becomes polluted!
x = ask_float("Give me a float?")
print(x)

from myutil import ask_float as ask_number
# import with a new name
x = ask_number("Give me a float?")
print(x)
