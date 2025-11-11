#Write a Python program using a for loop and continue statement to print numbers from 1 to 20, skipping the multiples of 3.
for num in range(1, 21):
  if num % 3 == 0:
    continue
  print(num)
