import random

def run():
  randomNumber = random.randint(1, 100)
  chosedNumber = int(input('Choose a number between 1 and 100: '))
  while chosedNumber != randomNumber: 
    if chosedNumber < randomNumber:
      print('Try with a bigger number')
    else: 
      print('Try with a smaller number')
    chosedNumber = int(input('Choose another number between 1 and 100: '))
  print('YOU WIN!')
if __name__ == '__main__':
  run()