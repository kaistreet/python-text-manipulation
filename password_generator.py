import random
def password_generator():
  characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  ask_password_length = int(input('How long do you want your password to be? '))
  generated_password = "".join(random.sample(characters,ask_password_length))
  print(generated_password)
  
ask_user_password = str(input('Want a random password generated? [enter y for yes or n for no:] '))
if ask_user_password == 'y':
  password_generator()
else:
  print("alright, i'll let you choose your own password.")
