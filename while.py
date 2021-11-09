def run():
  accountant = 1
  while accountant < 10:
    pow2 = 2**accountant
    print('2 power of ' + str(accountant) + ' is ' + str(pow2))
    accountant = accountant + 1

if __name__ == '__main__':
  run()