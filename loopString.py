def run():
  wordResponse = str(input('Write something to see it spelled: '))
  for word in wordResponse:
    print(word.upper())

if __name__ == '__main__':
  run()