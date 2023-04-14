print("Plase enter your age")
age = int(input())
# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dolloars for everyone else


if not ((age >= 2 and age <= 8) or age >= 65):
    print("YOU PAY 10 dollars and are not a child or senior!")
else:
    print("YOU ARE A CHILD OR SENIOR!")