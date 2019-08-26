# tee merkkijono, jossa on tasan 600 kpl x-merkkiä
print("x"*600)
# tee lista, jossa on 1000 kpl lukua nolla
a = [0]*1000
# tee lista, jossa on luvut 1, 2, 3... 1000
a = list(range(1, 1001))
# tee lista, jossa on luvut 1000, 990, 980, 970... 10
a = list(range(1000, 0, -10))
# tee lista, jossa on luvut 1, 4, 9, 16, 25... 10000
a = [x*x for x in range(1, 101)]
print(a)
# same as
a = []
for i in range(1,101):
    a.append(i*i)
print(a)
