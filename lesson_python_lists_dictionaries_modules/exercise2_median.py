def median(a):
    a.sort()
    n = len(a)
    if n % 2: 
        return a[int(n/2)] # odd, select the middle value
    else:
        return (a[int(n/2)]+a[int(n/2-1)])/2 # even, average of two middle values

def main():
    numbers = [1, 2, 3]
    print(numbers)
    print(median(numbers))
    numbers2 = [10, 0, 3, -5]
    print(numbers2)
    print(median(numbers2))
    print(numbers2)

if __name__=='__main__':
    main()