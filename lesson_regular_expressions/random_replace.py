import random, re

def random_suffix(m):
    return m.group(0)+random.choice(("Script", "Basic", "Code", "++"))

s = "I like to code in Java, Python and C#. And I use Visual Studio Code."
print(re.sub(r"Java|Python|Visual|C#|Code", random_suffix, s))

