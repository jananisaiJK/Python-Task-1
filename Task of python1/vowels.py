"""
python program to calculate total number of vowels and count each individual vowel A,E,I,O,U  in the string

"""

sentence = input ("Enter the sentence:")
string = sentence.upper()
print(string)
count = 0
list1 = ["A","E","I","O","U"]
for char in string:
    if char in list1:
        count = count+1
print ("number vowels given in sentense is:",count)       