# kysy käyttäjältä kokonaislukua N
# varmista että kokonaisluku on välillä 1-100
# tulosta luvut 1...N
# esim. anna luku? 3
# 1, 2, 3
while True:
    try:
        s = input("Give me a number?")
        n = int(s)
        if 1 <= n <= 100:
            for i in range(1, n+1):
                print(i)
            break
        else:
            print("Number must between 1 and 100")
    except ValueError:
        print("invalid number")
    
