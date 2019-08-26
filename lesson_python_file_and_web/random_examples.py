from random import *
print(random()) # random float between 0.0-1.0
print(randrange(1, 7)) # random int between 1..6
print(randint(1, 6)) # random int between 1..6
print(choice(["yes", "no", "maybe"])) # random choice
a = list(range(1, 101))
shuffle(a)
print(a[:10])
lottery = sample(range(1, 41), 7)
print(sorted(lottery))
