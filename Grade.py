#Write a Python program to input marks and display the grade as per the following rule:
mark = int(input("Enter the marks:"))
if mark>=90:
  print("Grade A")
elif mark>=70:
  print("Grade B")
elif mark==50:
  print("Grade C")
elif mark>=25:
  print("Grade D")
else:
  print("Grade F")
