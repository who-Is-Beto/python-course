menu = """
  Welcome to the currency converter! 💰
  Please choose an option:
  1. Convert USD to MXN
  2. Convert MXN to USD
  3. Exit
"""

option = int(input(menu))

if option == 1:
  moneyQuantity = float(input("Enter the amount of money in MXN: "))
  mxn = 20
  usd = str(moneyQuantity / mxn)
  print("The amount of money in USD is: $", usd)
elif option == 2:
  usdQuantity = float(input("Enter the amount of money in USD: "))
  mxn = 20
  moneyQuantity = usdQuantity * mxn
  print("The amount of money in MXN is: $", moneyQuantity)
elif option == 3:
  print("See ya")
else:
  print("Invalid option :c")
