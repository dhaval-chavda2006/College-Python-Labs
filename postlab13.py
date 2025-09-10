
#a.	Write a program that reads a text file example.txt and counts the number of lines, 
# words, and characters in the file. Print these counts
# with open("file.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# lines = text.splitlines()
# words = text.split()
# chars = text

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", len(chars))




#Python program to read a text file line by line and store each line in a list. 
# Print the list after reading the entire file

# lines = []

# with open("file.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         lines.append(line.strip())  # strip() removes \n at the end

# print(lines)






#Python program to read data from a CSV file data.csv 
# and print each row to the console.

# import csv

# with open("data-1.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)




#Python program that merges the contents of two text files file1.txt and file2.txt into a third file merged.txt. 
# Ensure that the contents of file1.txt come first.
with open("file.txt", "r") as f1, open("ict1.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as f3:
    f3.write(data1)
    f3.write(data2)
