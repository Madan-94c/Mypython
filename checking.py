#Write a Python program that checks whether a number is:
#Even and Positive
#Even and Negative
#Odd and Positive
#Odd and Negative

num = int(input("Enter a number: "))

if num % 2 == 0:
  # Even number
  if num > 0:
    print(f"{num} is Even and Positive.")
  elif num < 0:
    print(f"{num} is Even and Negative.")
  else:
    print(f"{num} is Even and Zero.") # Although zero is technically even, it's neither positive nor negative
else:
  # Odd number
  if num > 0:
    print(f"{num} is Odd and Positive.")
  elif num < 0:
    print(f"{num} is Odd and Negative.")
  else:
    print(f"{num} is Odd and Zero.") # Zero cannot be odd, this path should not be reached with integer input other than 0 itself.
