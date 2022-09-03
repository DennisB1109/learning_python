"""
In Python it is easy to deal with numbers i.e python handles the 'type conversion' of natural- decimal- or comlex numbers
automatically (see in the few examples below)
"""
print(2)
print(2.134)
print(-2.3242)
print(3 * 5.5)
print(10 % 3)                                             # Modulo Operator

# Type Conversion
num = 10
print(str(num))                                           # We transform a numeric variable into a string
print(str(num) + " years old")                            # Possible use case for type conversion. Of course print(10, " years old")  will work too

neg_num = -10
print(abs(neg_num))                                       # The abs() function expects a numeric type and returns the absolute value
print(pow(-10, 2))                                        # The pow() function expexts two numeric types and returns the first number to the power of the second number
print(max(1, 5, 10))                                      # The max() function expects an arbitrary amount of numeric types and return the maximum value
print(min(1, 5, 10))                                      # The min() function expects an arbitrary amount of numeric types and return the minimum value

from math import *                                        # Like this we import additional libraries into our program
print(floor(3.7))                                         # Gets rid of the numbers after the decimal point
print(ceil(3.2))                                          # Always round the decimal number up
print(sqrt(49))                                           # Returns the squareroot of the inputed number