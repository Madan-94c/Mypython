Write a function sum_of_n_numbers() that accepts n numbers (entered by the user in a list) and returns their total sum.
def sum_of_n_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

n = int(input("How many numbers do you want to add? "))
nums = []
for i in range(n):
    value = float(input("Enter number: "))
    nums.append(value)
print("Sum of numbers is:", sum_of_n_numbers(nums))
