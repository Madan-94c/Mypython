#Find the mark result using if-elif-else conditions.
mark = int(input("Enter the marks:"))
if mark>=90:
  print("Excellent")
elif mark>=70:
  print("Very Good")
elif mark==50:
  print("Average")
elif mark>=25:
  print("Just pass")
else:
  print("Fail")
