
"""
write a program that takes that takes string and returns true if its anagram of another string false 

"""

str1=input("enter the string:")
str2=input("enter the string:")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
     print(True)
else:
     Print(False)    