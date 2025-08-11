import numpy as np

#NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

#NumPy program to reverse an array (the first element becomes the last).
# arr = np.array([1, 2, 3, 4, 5])
# reversed_arr = arr[::-1]
# print("Original array:", arr)
# print("Reversed array:", reversed_arr)


#NumPy program to find common values between two arrays
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([4, 5, 6, 7, 8])
# common_values = arr1[np.in1d(arr1, arr2)]
# print("Common values:", common_values)


#NumPy program to repeat array elements.
# arr = np.array([1, 2, 3])
# repeated_arr = np.repeat(arr, 2)
# print("Original array:", arr)
# print("Repeated array:", repeated_arr)


#NumPy program to find the memory size of a NumPy array.
# arr = np.array([1, 2, 3, 4, 5])
# memory_size = arr.size * arr.itemsize
# print("Memory size:", memory_size)


# NumPy program to create an array of ones and zeros.
# ones_array = np.ones((3, 4), dtype=int)   
# zeros_array = np.zeros((2, 5), dtype=int) 
# print("Array of ones:\n", ones_array)
# print("Array of zeros:\n", zeros_array)


#NumPy program to find the 4th element of a specified array.
# arr = np.array([1, 2, 3, 2, 3, 4, 3])
# indices = np.where(arr == 3)
# print("Indices where element is 3:", indices[0])