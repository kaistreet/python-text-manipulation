import random
ask_password = str(input('want a random password generated? type y if yes: '))
if ask_password == 'y':
  print("Here's your password: " + "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890',random.randint(0,25))))
else:
  print('Ok, no password for you.')
