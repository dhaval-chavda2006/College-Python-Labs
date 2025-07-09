#Write a python code for calculating the Area and Perimeter of a Rectangle
'''
l=int(input("ENTER THE LENGTH OF RECTANGLE:"))
b=int(input("ENTER THE BREADTH OF RECTANGLE:"))

area =l*b
peri =(l+b)*2

print("THE AREA OF RECTANGLE IS:",area)
print("THE PERIMETER OF RECTANGLE IS:",peri)
'''
#Write a python code for testing if a number is even or odd
'''
a=int(input("ENTER A NUMBER:"))
if(a%2==0):
    print(f"{a} is EVEN NUMBER")
else:
    print(f"{a} is ODD NUMBER")
'''
#Write a python code for calculate the area and volume of the Cube.
'''
a=int(input("ENTER LENGTH OF CUBE:"))

vol = a*a*a
area = 6*a*a

print("THE VOLUME OF CUBE IS",vol)
print("the area of cube is",area)
'''
'''
#Write a python code to solve the equation z = (x+y)*(x-y)

x=int(input("ENTER THE FIRST NUMBER:"))
y=int(input("ENTER THE SECOND NUMBER:"))

z =(x+y)*(x-y)

print("the answer is:",z)
'''
#Write a python code to solve the equation z = (x+y)*(x+y)-2xy; write a comment on it.
'''
x=int(input("ENTER THE FIRST NUMBER:"))
y=int(input("ENTER THE SECOND NUMBER:"))

z =(x+y)*(x-y)-2*x*y

print("the answer is:",z)
'''

#Write a python code for Converting Celsius to Fahrenhit

c=int(input("ENTER THE CELCIUS:"))
fahrenheit = (c * 9 / 5) + 32
print("CONVERTED TO FAHRENHEIT:",fahrenheit)