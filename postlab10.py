
#Python program to draw a line with suitable label in the x axis, y axis and a title.


# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, marker='o', linestyle='-')

# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.title("Simple Line Graph")

# plt.show()




#Write a Python program to plot two or more lines on same plot with suitable legends of each line.


# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]   
# y2 = [1, 4, 9, 16, 25]  
# y3 = [5, 7, 9, 11, 13]  

# plt.plot(x, y1, label="y = 2x", marker='o')
# plt.plot(x, y2, label="y = x²", marker='s')
# plt.plot(x, y3, label="y = 2x+3", marker='^')

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Multiple Lines on Same Plot")
# plt.legend()


# plt.show()









# Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7


import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.bar(languages, popularity, color=['blue', 'green', 'red', 'orange', 'purple', 'cyan'])

plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

plt.show()
