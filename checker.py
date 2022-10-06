print("Palindrome Checker")
word = input("Enter Word ->  ")
wordlower = word.lower()
backward = wordlower[::-1]

from PyDictionary import PyDictionary

def palindromecheck(word):
    dictionary = PyDictionary()

    if dictionary.meaning(word,True) is None:
        print(f"It appears '{word}' is NOT a word found in the dictionary.")
    elif dictionary.meaning(word, True) and backward == wordlower:
        print(f"{word} is a palindrome!")
    elif dictionary.meaning(word, True) and backward != wordlower:
        print(f"{word} is not a palindrome.")

palindromecheck(word)  
