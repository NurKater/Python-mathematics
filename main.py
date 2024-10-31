import math

def Exponentiation(number,degree):
    print(number**degree)
    """
    Exempel number = 4, degree = 3
    >>> 64
    """

def EvenNumber(number):
    if number % 2 == 0:
        print("It's True")
    else:
        print("It's False")
    """
    Exemple number = 12
    >>> It's True
    number = 15
    >>> It's False
    """

def AreaOfCircle(radius):
    print(radius**2 * math.pi)
    """"
    Exemple radius = 10
    >>> 314.1592653589793
    """

def Equation(example, result):
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            if example(x) == result(y):
                print(f"X = {x}, Y = {y}")

"""
Exemple 
Equation(lambda x: 2 * x + 3, lambda y: y)
 >>> X = -501, Y = -999
 >>> X = -500, Y = -997 ...
"""
