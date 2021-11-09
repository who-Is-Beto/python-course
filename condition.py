age = int(input("How old are you? "))
if age >= 18 and age <= 65:
    print("You are old enough to vote!")
elif age >= 65 and age <= 100:
    print("You are old enough to retire!")
elif age > 100:
    print("How the fuck you still alive?")
else:
    print("You are not old enough to vote!")
