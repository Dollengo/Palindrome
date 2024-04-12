def is_palindrome(s):
    return s == s[::-1]

str = input("Enter a word: ")
if is_palindrome(str):
    print(str, ";", "Is a palindrome")
else:
    print(str, ";", "Is not a palindrome")