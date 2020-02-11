"""
vowels = [ 'a', 'e', 'i', 'o', 'u']

word = "Milliways"

for letter in word:
    if letter in vowels:
        print(letter)
"""

found = []
#print(len(found))
found.append('a')
#print(found)
found.append('e')
found.append('i')
found.append('o')
#print (len(found))
#print(found)

if 'u' not in found:
    found.append('u')

print(found)


  

