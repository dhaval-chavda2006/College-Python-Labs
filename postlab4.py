#Write a Python program to multiply all the items in a list.

# import math
# my_list = [1, 2, 3, 4, 5]
# result = math.prod(my_list)
# print(f"The product (math.prod): {result}")


#Write a Python program to get the largest number from a list.
# a = [10, 24, 76, 23, 12]
# largest = max(a)
# print(largest)


#Write a Python program to remove duplicates from a list.
# a = [1, 2, 2, 3, 4, 4, 5]
# unique= list(set(a))
# print(unique)


#Write a Python program to get the frequency of elements in a list.
# def get_frequency_specific(input_list, element):
#     return input_list.count(element)

# list = [10, 20, 10, 30, 20, 10]
# elementtofind = 10
# frequency = get_frequency_specific(list, elementtofind)
# print(f"Frequency of {elementtofind}: {frequency}")


#Find common items from two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements_loop = []
# for item in list1:
#     if item in list2:
#         common_elements_loop.append(item)
# print(f"Common elements (using loop): {common_elements_loop}")



#Convert a list of multiple integers into a single integer
a = [1, 2, 3, 4]
result = 0
for num in a:
    result = result * 10 + num
print(result)  