def decorator_name(func):
    def inner(*args, **kwargs):
        # decorator does its job here
    return inner

# decorator will modify a function
@decorator_name
def something_else():
    # function body
    pass
