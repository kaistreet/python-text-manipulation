#A program that asks the user for a string and prints out whether this string is a palindrome or not.
def reverse(palindrome_checker):
	palindrome_checker = palindrome_checker[::-1]
	return palindrome_checker

palindrome_checker = str(input('Enter a word: '))
if palindrome_checker == reverse(palindrome_checker):
	print('this is a palindrome')
else:
    print("this isn't a palindrome")
