from random import shuffle, sample
lotto_numbers = list(range(1, 40))
shuffle(lotto_numbers)
lotto_row = lotto_numbers[:7]
print(sorted(lotto_row))
# this all can be reduced to just 1 line of code!
print("Lotto numbers:", sorted(sample(range(1, 40), 7)))

