a = [21, 13, 19, 3,11,5]
# Sort the list
def median(x):
    num_list = x[:]
    num_list.sort()
    # Finding the position of the median
    if len(num_list) % 2 == 0:
        first_median = num_list[len(num_list) // 2]
        second_median = num_list[len(num_list) // 2 - 1]
        return (first_median + second_median) / 2
    else:
        return num_list[len(num_list) // 2]


print(a)
print(median(a))
print(a)

