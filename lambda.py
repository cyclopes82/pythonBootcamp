def square(num):
    return num * num

print(square(9))

#Lambda stores in variable, Generally we don't store lambda result in variable

square2 = lambda num : num * num 

print(square2(7))

# lambda to add two numbers

add = lambda a, b : a + b

print(add(7, 8))

print(square.__name__)
print(square2.__name__)
print(add.__name__)