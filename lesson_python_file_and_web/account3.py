class Account:
    """Bank account, which has balance as cents (1/100 euros)
    """
    # slots leads to less memory and CPU cycle usage, and you can limit
    # the future dynamic options
    __slots__ = ('balance', ) # tuple, which defines all attributes
    def __init__(self, balance):
        self.balance = balance # public by default
    def __str__(self):
        return "Account(%d)" % self.balance

a = Account(500) # 5 euros
print(a)
a.balance += 1000 # add 10 euros
print(a)
# you can no longer add new attributes to this class, because __slots__
# has defined all existing attributes
a.type = "säästö" # this will FAIL!
print(a.type)

        