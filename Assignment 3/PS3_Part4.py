print("This program will find the frequency of letters in a string.")
print("The string you enter must have letters only, no spaces or other characters.")
s = input("Please enter the string: ")
letters = [0]*26
s = s.lower()
print(s)
for i in range(0,len(s)):
    value = ord(s[i]) - 97
    letters[value] += 1
charval = 97    
for i in letters:
    print(chr(charval)+":",i)
    charval += 1
