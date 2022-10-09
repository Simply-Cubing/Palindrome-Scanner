from PyDictionary import PyDictionary

print("Print the palindromes in a block of text!")
text = input("""Enter Text ->

""")
empty = []
dictionary = PyDictionary()
number_of_palin = 0

for word in text.split():
    if dictionary.meaning(word,True) and word == word[::-1] and len(word) > 1:
        number_of_palin += 1
        empty.append(word)

if len(empty) > 1:
    print(f"There are {number_of_palin} palindromes in this text, they are {empty}")
elif len(empty) == 1:
    print(f"There is one palindrome in this text, it is '{empty[0]}'")    
elif len(empty) == 0:
    print("There are no palindromes in this text")      
