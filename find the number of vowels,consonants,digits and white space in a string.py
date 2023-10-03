#find the number of vowels,consonants,digits and white space in a string

st=input('Number of Vowels')

vow=0
cons=0
digits=0
space=0

for i in st:
    if i in 'seiouAETOU':
       vow += 1
    elif i.isalpha():
        cons += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace:
        space += 1

print('Number of vowels',vow)
print('Number of consonants',cons)
print('Number of digits',digits)
print('Number of whitespace',space)
