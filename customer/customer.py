

class Customer(object):
"""A simple class."""
subscribers = 0
# docstring
# class attribute

def __init__(self, fname,surname,othername,email,phone):
"""This is the initializer. It's a special
method (see below).
"""
self.fname = fname # special method
self.surname = surname
self.othername = othername
self.email = email
self.phone = phone

def __str__(self):
"""This method is run when Python tries
to cast the object to a string. Return
this string when using print(), etc.
"""
return self.name # special method

# instance attribute
def rename(self, renamed):
# regular method
"""Reassign and print the name attribute."""
self.name = renamed
print("Now my name is {}".format(self.name))

def subscribe(self):

    pass

if __name__='__main__':
    app.run(deburg=True)

