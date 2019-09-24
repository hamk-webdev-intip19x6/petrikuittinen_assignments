# tee luokka nimeltä Account eli suomeksi pankkitili
# pankkitilillä on vain yksi ominaisuus balance eli suomeksi saldo
# tilille voi panna rahaa metodilla deposit(amount)
# tililtä voi nostaa rahaa metodilla draW(amount)
# tilin saldo ei saa mennä negatiiviseksi, koska kyseessä ei ole luottotili
# saat itse ratkaista miten se olisi järkevää
# esim. a = Account(100)
# a.deposit(200)
# a.draw(150)
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def draw(self, amount):
        self.balance = max(0, self.balance-amount)

a = Account(100)
a.deposit(300)
print(a.balance)
a.draw(250)
print(a.balance)
a.draw(250)
print(a.balance)
