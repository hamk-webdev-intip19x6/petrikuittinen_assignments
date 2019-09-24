# koodatkaa tämä harjoitus1.py nimiseen tiedostoon
# koska jos tiedosto-pääte ei lopu .py, niin editori ei osaa automaattisesti
# valita Python-tilaa
# kysy käyttäjältä merkkijonoa esim. kukka
s = input("?")
# kerro montako merkkiä käyttäjän merkkijonossa on esim. 5
print("pituus:", len(s))
# kerro merkkijonon 1. merkki esim. k
print("1. merkki:", s[0])
# kerro merkkijonon viimeinen merkki esim. a
print("viimeinen merkki:", s[-1])
# kerro merkkijon kaikki merkit, paitsi 1. merkki esim. ukka
print("tokasta eteenpäin:", s[1:])
# kerro merkkijon joka toinen merkki, 1. lähtien esim. kka
print("joka toinen:", s[::2])
# kerro merkit väärinpäin esim. akkuk
print("väärinpäin:", s[::-1])
# kerro merkit ilman välilyöntejä
print("ilman välilyöntejä", s.replace(" ", ""))
# kerro merkit kaikki isolla esim. KUKKA
print("kaikki isolla", s.upper())

