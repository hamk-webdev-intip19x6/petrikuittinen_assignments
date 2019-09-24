# luo lista a, jossa on luvut 1, 2, 10
a = [1, 2, 10]
# tulosta listan pituus
print(len(a))
# luo lista b, jossa 1000 kpl lukua nolla
b = 1000*[0]
# tulosta listan b pituus
print(len(b))
# tulosta listan b 50 viimeistä lukua
print(b[-50:])
# luo tyhjä lista c
c = []
# lisää listaan luvut 3, -5 ja 6 erikseen
c.append(3)
c.append(-5)
c.append(6)
# lisää listan alkuun luku 0
c.insert(0,0)
# tulosta lista c väärinpäin
d = c[:]
d.reverse()
print(d)
# tulosta lista c lajiteltuna pienimmästä suurimpaan
d.sort()
print(d)
# tulosta lista c lajiteltuna suurimmasta pienimpään
d.sort(reverse=True)
print(d)



