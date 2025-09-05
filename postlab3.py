#Write a Python program to reverse a string.

# str1 = "hello"
# reversed_string = str1[::-1]
# print(reversed_string)  



#Python program to check if a string is a palindrome.
# def palindrome_slicing(s):
#   s = s.lower()
#   return s == s[::-1]
# string1 = "madam"
# string2 = "hello"
# string3 = "Racecar"
 
# print(f"'{string1}' is a palindrome: {palindrome_slicing(string1)}")
# print(f"'{string2}' is a palindrome: {palindrome_slicing(string2)}")
# print(f"'{string3}' is a palindrome: {palindrome_slicing(string3)}")


#Python program to check if a string contains only digits.
# pin = "000h" 
# print(pin.isnumeric())


#Python program to find the longest word in a sentence.
# s = "I am learning Python"
# words = s.split()
# res = ""

# for word in words:
#     if len(word) > len(res):
#         res = word

# print(res)



#Python program to find the length of the last word in a sentence.

def lengthOfLastWord(a):
    l = 0
    x = a.strip()

    for i in range(len(x)):
        if x[i] == " ":
            l = 0
        else:
            l += 1
    return l

if __name__ == "__main__":
    inp = "OM SHANTI OMMMMMM "
    print("The length of last word is",
          lengthOfLastWord(inp))