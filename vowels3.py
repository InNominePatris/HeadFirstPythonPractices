vowel = ['a', 'e', 'i', 'o', 'u']
word = str ( input("rovide a word to search for vowels: "))

found = []

for letter in word:
    if letter in vowel:
      if letter not in found:
          found.append(letter)
for vowel in found:
    print(vowel)