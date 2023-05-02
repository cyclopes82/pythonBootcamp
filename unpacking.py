# Unpacking of argments

def sum_all_num( *args ):
    total = 0 
    for num in args:
        total += num

    return total


nums = [1,2,3,4]
#print(sum_all_num(nums)) -- TypeError: unsupported operand type(s) for +=: 'int' and 'list'

print(sum_all_num(*nums)) #Unpacking of arguments

#Adding that little *  makes a huge difference! Instead of passing in a single item (the list), we're now passing in 121 separate arguments.

nums_tup = (1, 2, 3, 5)

print(sum_all_num(*nums_tup))