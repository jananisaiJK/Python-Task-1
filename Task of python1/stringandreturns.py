"""
string and returns a new string with all vowels removed

"""

string=input("Enter a string:")

vowels="aeiouAEIOU"

result=""

for character in string:
    if character not in vowels:
       result += character

print(result)    
