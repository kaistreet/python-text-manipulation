"""
This script randomly generates a user password based on length preference.


Author: Kai Street
Date: 15 October 2019
"""

import random
def password_generator():
	"""
	Returns a randomly generated password, based on password length input.

	Author: Kai Street
	Date: 15 October 2019

	Precondition: ask_password_length must be int type
	"""

	#Characters that can be used in password
	characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_+=[]|;:,.<>?`~'
	
	#Ask user for length of password; ensure type is interger
	ask_password_length = input('How long do you want your password to be? ')
	assert type(ask_password_length) == int,'User did not enter int type.'

	#Generate password based on available characters and length preference
	generated_password = "".join(random.sample(characters,ask_password_length))

	return generated_password

#Runs script
ask_user_password = str(input('Want a random password generated? [enter y for yes or n for no:] '))
if ask_user_password == 'y':
	password_generator()
else:
	print("alright, i'll let you choose your own password.")
