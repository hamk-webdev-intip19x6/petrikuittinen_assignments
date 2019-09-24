class Account:
    """Bank account, which has balance as cents (1/100 euros)
    """
    # __name can be used to simulate private attributes in classes
    
    __slots__ = ('__balance', )  # tuple, which defines all attributes

    def __init__(self, balance):
        self.__balance = balance  # public by default

    def deposit(self, amount):
        """deposit amount cents to account. Return current balance"""
        self.__balance += amount
        return self.__balance
    
    def draw(self, amount):
        """draw amount of cents from account. Return current balance"""
        # make sure balance doesn't go below zero
        self.__balance = max(self.__balance-amount, 0)
        return self.__balance
    
    def __str__(self):
        return "Account(%d)" % self.__balance

    
a = Account(500)  # 5 euros
b = Account(1000)  # 10 euros
print(a)
a.deposit(1000)  # add 10 euros
print(a)
a.draw(300)
print(a)
print(b.draw(100))
print(b.draw(9999999))
print(b.deposit(750))
print(b.__balance)  # this will fail, because __ is private


