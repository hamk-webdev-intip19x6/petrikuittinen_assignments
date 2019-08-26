# WARNING! DO NOT PROGRAM LIKE THIS
# THE FOLLOWING FUNCTION HAS AN UNDOCUMENTED SIDE EFFECT
def mymax(a):
    """Return the item of list a, which has the highest value"""
    a.sort() # sort in ascending order
    return a[-1] # return the last item
    
a = [1, 10, 5, -3, 7]
print(mymax(a))
print(a) # a is sorted as well!

# This version does NOT have a side effect
def mymax2(a):
    """Return the item of list a, which has the highest value"""
    b = a.copy()
    b.sort() # sort in ascending order
    return b[-1] # return the last item
    
a = [1, 10, 5, -3, 7]
print(mymax2(a))
print(a) # a is still in original order