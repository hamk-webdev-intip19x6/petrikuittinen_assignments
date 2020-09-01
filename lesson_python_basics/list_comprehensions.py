a = [1, 2, 3, 10, -5, 7]
squared = [x*x for x in a]
print(squared)
odd = [x for x in a if x%2!=0]
print(odd)
b = ['1', "2", '3', "100", "-15", "1234", "1000000", "987654"]
int_list = [int(i) for i in b]
print(int_list)
big_ints = [int(i) for i in b if len(i) > 3]
print(big_ints)
