# write a pgm that displays letter grade
# step1 i/p-int o/p-str

score = int(input("Enter your score of this semester->"))
if score >= 90 and score <= 100:
    print("Your Grade is: A")
elif score >= 80 and score <= 89:
    print("Your Grade is: B")
elif score >= 70 and score <= 79:
    print("Your Grade is: C")
elif score >= 60 and score <= 69:
    print("Your Grade is: D")
elif score > 100 and score <= -1:
    print("Your are impossible !!!!")
else:
    print("Your grade is: F")
