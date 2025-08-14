#Python program to print all odd numbers between 1 to 100 using a while loop

# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#     num += 1




# Python program to find the sum of all natural numbers between 1 to n

# n = int(input("Enter the value of n: "))
# sum_of_numbers = n * (n + 1) // 2
# print("The sum of all natural numbers:",sum_of_numbers)



# Python function to count the number of digits in a number

# def count_digits(number):
#     return len(str(abs(number)))
# num = 123456
# print(f"Number of digits in {num} is:", count_digits(num))



# Python program to find the first and last digits of a number (positive numbers only)

# number = int(input("Enter a positive number: "))

# last_digit = number % 10
# first_digit = number

# while first_digit >= 10:
#     first_digit //= 10

# print(f"The first digit is: {first_digit}")
# print(f"The last digit is: {last_digit}")




# Python program to swap the first and last digits of a number (positive integers)
# number = int(input("Enter a positive integer: "))
# num_str = str(number)

# if len(num_str) == 1:
#     swapped = num_str
# else:
#     swapped = num_str[-1] + num_str[1:-1] + num_str[0]

# swapped_number = int(swapped)
# print(f"Number after swapping first and last digits: {swapped_number}")




# Python program to calculate the product of digits of a number

# number = int(input("Enter a positive integer: "))
# product = 1
# temp = number

# while temp > 0:
#     digit = temp % 10
#     product *= digit
#     temp //= 10

# print(f"The product of digits of {number} is: {product}")




# Python program to enter a number and print its reverse

number = int(input("Enter a number: "))
reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print(f"The reverse of {number} is: {reverse}")