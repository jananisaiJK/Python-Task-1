"""
Pyramid of numbers

"""
n= int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
          print(" ",end="")
    for j in range(i+1):
          print("1",end=" ")
    print()        