from PyDictionary import PyDictionary

print("Print the palindromes in a block of text!")
text = input("""Enter Text ->

""")
empty = []
dictionary = PyDictionary()
number_of_palin = 0

for word in text.split():
    if dictionary.meaning(word,True) and word == word[::-1]:
        number_of_palin += 1
        empty.append(word)

print(f"There are {number_of_palin} palindromes in this text, they are {empty}")
     
