try:
    # if an exception is fired in this block go to
    # corresponding exception handler
except ExceptionClass:
    # handle this exception type
except AnotherExceptionClass:
    # handle this exception type
except:
    # catch all exceptions, NOT recommended!
else:
    # executed if no exceptions occured
finally:
    # executed at the end, no matter what happens

