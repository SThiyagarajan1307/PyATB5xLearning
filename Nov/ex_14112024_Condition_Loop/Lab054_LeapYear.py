# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

Year = int(input("Enter the year:"))

if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print("entered year is Leap Year")
else:
    print("entered year is not leap year")
