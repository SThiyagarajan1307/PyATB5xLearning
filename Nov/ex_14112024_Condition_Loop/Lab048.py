# write a pgm  to take user age  and let him  know if he can go to club or not age=21
# #step 1 i/p int----o/p str
#age>21 print go age<21 print dont go

age=float(input("Enter your age:"))
if age>=21:
    print("You can go to club")
else:
    print("You cannot go to club! You should be above 21 to be eligible")