#Pass statement example write a python program that iterates through numbers 1 to 10, but uses a pass statement inside the loop(demonstrate its effect)
for i in range(1, 11):
    if i == 5:
        pass  
    else:
        print("Current number:", i)

print("Loop completed.")
