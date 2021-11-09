import random
import string

def generatePassword():
  caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
  password = []
  for i in range(15):
    random_caracter = random.choice(caracter)
    password.append(random_caracter)
  return ''.join(password)

def run():
  password = generatePassword()
  print('your new password is ' + password)

if __name__ == '__main__':
  run()