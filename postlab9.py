import pandas as pd
import numpy as np

#Pandas program to add, subtract, multiple and divide two Pandas Series.

# s1 = pd.Series([10, 20, 30, 40, 50])
# s2 = pd.Series([2, 4, 6, 8, 10])
# print("Addition of two Series:")
# print(s1 + s2)
# print("\nSubtraction of two Series:")
# print(s1 - s2)
# print("\nMultiplication of two Series:")
# print(s1 * s2)
# print("\nDivision of two Series:")
# print(s1 / s2)


#Pandas program to convert a dictionary to a Pandas series.
#dictionary
# data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
# # Convert dictionary to Pandas Series
# series = pd.Series(data)
# # Display the Series
# print(series)


#Pandas program to create a series from a list, numpy array and dict

# list_data = [10, 20, 30, 40]
# series_from_list = pd.Series(list_data)
# print("Series from List:")
# print(series_from_list)

# numpy_data = np.array([5, 15, 25, 35])
# series_from_numpy = pd.Series(numpy_data)
# print("\nSeries from NumPy Array:")
# print(series_from_numpy)

# dict_data = {'a': 100, 'b': 200, 'c': 300}
# series_from_dict = pd.Series(dict_data)
# print("\nSeries from Dictionary:")
# print(series_from_dict)


#Pandas program to stack two series vertically and horizontally

# s1 = pd.Series([10, 20, 30, 40])
# s2 = pd.Series([50, 60, 70, 80])

# vertical = pd.concat([s1, s2])
# print("Vertical Stack (one below another):")
# print(vertical)

# horizontal = pd.concat([s1, s2], axis=1)
# print("\nHorizontal Stack (side by side):")
# print(horizontal)