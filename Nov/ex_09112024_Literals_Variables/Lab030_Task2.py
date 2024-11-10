# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1
from xml.dom.minidom import ProcessingInstruction

Num1 = int(input("Enter the Number1\t"))
Num2 = int(input("Enter the Number2\t"))

Quotient = Num1/Num2
Reminder = Num1%Num2

print("Quotient\t", Quotient)
print("Reminder\t", Reminder)
