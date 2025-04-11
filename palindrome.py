def is_palindrome(word):
    word=word.lower()
    return word == word[::-1]

uword=str(input("enter a word:"))
if is_palindrome(uword):
    print(""+uword+ " is a palindrome")
else:
    print(""+uword+" is not a palindrome")