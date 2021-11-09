def run(): 
  for account in range(1000):
    if account % 2 != 0:
      continue
    print(account)

  for i in range(1, 1001): 
    print(i)
    if i == 19:
      break

if __name__ == '__main__':
  run()