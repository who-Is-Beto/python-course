def is_cousin(number):
  counter = 0
  for i in range(1, number + 1):
    if i == 1 or i == number:
      continue
    if number % i == 0:
      counter += 1
  if counter == 0:
    return True
  return False

def run():
  number = int(input('write a number: '))
  if is_cousin(number):
    print('is Cousin')
  else: print('It was not cousin')
if __name__ == "__main__":
  run()