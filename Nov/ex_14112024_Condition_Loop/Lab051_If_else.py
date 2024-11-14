#Pgm to fin max of 3 num
#step1--i/p----int---o/p---str/int
from operator import ifloordiv

num1 = float(input("Enter num1\n"))
num2 = float(input("Enter num2\n"))
num3 = float(input("Enter num3\n"))

if num1>num2 and num1>num3:
    print("Max number is-",num1)
elif num2>num1 and num2>num3:
    print("Max number is-", num2)
else:
    print("Max number is-", num3)