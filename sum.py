# * args



""" Below function need to have fixed number of parameter/arguments """

def sum_of_all_nums(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

print(sum_of_all_nums(1, 2, 3, 4))

""" With *args we can manage any number of parameters/arguments """

def sum_of_nums_args( *args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_of_nums_args(1,2,3,4,5,6,7,8,9))


def ensure_correct_info(*args):
    if "Pratik" in args and "Patil" in args:
        return "Welcome back Master!!"
    return "Not sure who you are...."

print(ensure_correct_info(1, True, "Pratik", "Patil"))
print(ensure_correct_info(1, 2))

