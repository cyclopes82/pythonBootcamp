#ask for age

age = input("How old are you: ")
# 18-21 Wristband
# if age != "":
# #if age : 
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter, but need a wristband!")
#     # 21+ drink, normal entry
#     elif age > 21:
#         print("You are good to enter and can drink!")
#     # too young, sorry
#     else:
#         print("You can't come in, little one! :(")
# else:
#     print("Please enter an age!")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")