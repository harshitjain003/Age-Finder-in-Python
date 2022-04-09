# Importing Date Module
from datetime import date

# Let curYear equals to Current Year
currDate = date.today()
currYear = currDate.year

user_DOB = int(input("Enter your Birth of Year : "))
age = currYear - user_DOB
print("Your Age is", age)