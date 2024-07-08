"""

write a program that returns true if it is palindrome else false 

"""

s = input("Enter the value : ")

reverse = s[::-1]

if( s == reverse):
    print("yes it is palindrome")
else:
    print("No it is not a palindrome")    