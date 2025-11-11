#sum until negative number write a python program using a while loop to keep taking numbers from the user and add them, but stop when a negative number is entered.
total = 0
while True:
    number = int(input("Enter a number (negative number to stop): "))
    if number < 0:
        break
    total += number
print("The sum of entered numbers is:", total)
