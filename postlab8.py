#Write a Python program to convert degree to radian

# from math import pi
# degree = int(input("ENTER THE DEGREE:"))
# radian = degree * pi/180
# print("RADIAN = ",radian)


#Python program prints the value of the formula
#y=6x^2+4sin(x)

# from math import sin

# x = int(input("ENTER THE VALUE OF X: "))
# y = 6 * (x ** 2) + 4 * sin(x)
# print("THE ANSWER IS:", y)



#	Write a Python function that evaluates the mathematical functions
#   f(x)=cos(2x),f^' (x)=-2 sin⁡(2x),and f^'' (x)=-4 cos⁡(2x). 
#	Return these three values. Write out the results of these values for x=π

import math
def evaluate_functions(x):
    f = math.cos(2 * x)             
    f_prime = -2 * math.sin(2 * x)  
    f_double_prime = -4 * math.cos(2 * x)  
    return f, f_prime, f_double_prime

results = evaluate_functions(math.pi)
print("f(π) =", results[0])
print("f'(π) =", results[1])
print("f''(π) =", results[2])
