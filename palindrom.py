def palindrom(oration):
  oration = oration.replace(' ', '').lower()
  if oration == oration[::-1]:
    return True
  return False

def run():
  oration = str(input('Wirite an oration: '))
  is_palind = palindrom(oration)
  if is_palind:
    print('Is a palindrom oration')
  else:
    print('Is not a palindrom oration')

if __name__ == '__main__':
  run()