"""
write a program that takes that takes two strings and return most frequent character in it

"""

str=input("Enter String")
l=list(str)
freq=[l.count(ele) for ele in l]
d=dict(zip(l,freq))
print(d)