# Write a program that displays “Welcome to Python” five times.

for _ in range(5):
    print("Hello, World!")

#Write a program that displays the following table:

#print(f"{'a':<5}{'a^2':<5}{'a^3':<5}")
for a in range(1, 5):
    print(f"{a:<5}{a**2:<5}{a**3:<5}")


#Write a program that displays the result of

a= (9.5*4.5)-(2.5*3)
b= 45.5-3.5
print(a/b)