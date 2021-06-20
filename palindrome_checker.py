"""
This script checks if a string is a palindrome.

Author: Kai Street
Date: 22 September 2019
"""


def reverse(palindrome_checker):
	"""
	This function reverses a string and returns reversed string

	Author: Kai Street
	Date: 22 September 2019

	Parameter palindrome_checker: a string to reverse
	Precondition: palindrome_checker must be string type
	"""
	palindrome_checker = palindrome_checker[::-1]
	return palindrome_checker

#Asks user for a word
palindrome_checker = input('Enter a word: ')
assert type(palindrome_checker) == str,repr(palindrome_checker)+' is not string type.'

#Checks user input to see if it's a palindrome and tells user whether it is
if palindrome_checker == reverse(palindrome_checker):
	print('this is a palindrome')
else:
    print("this isn't a palindrome")
