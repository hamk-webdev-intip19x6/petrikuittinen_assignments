# kysy käyttäjältä merkkijonoa
# laske montako merkkiä merkkijonossa on, poislukien alun ja lopun whitespace
# tulosta merkkijonon viimeinen merkki
# selvitä onko merkkijonossa alimerkkijonoa "bugi"

s = input("Give me a string?")
s = s.strip() # get rid of leading and trailing whitespace
print("length:", len(s))
if len(s)>0:
    print("last character:", s[-1])
    if "bugi" in s:
        print("Bugi found")
    else:
        print("Bugi NOT found")
        

