def abc():
    print("hello")
    pass
def cba():
    return "Hi people"
print(abc())
abc() # calling the function directly
print(cba())
print(cba().upper())

def multiply(a, b):
    return a*b
product = multiply(10, 2)
print(product)


# def greet(name):
#     print(f"Hello {name} !")
#
# greet("teja")

import math

print(math.factorial(5))



