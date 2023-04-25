s = {1, 4, 5, 4, 5}

print(s)

#Sets don't have an index hence below in not allowed
#s[0]

#check if 4 is in set s

print(4  in s)

for thing in s:
    print(thing)

cities = ["Leh", "Pune", "Mumbai", "Warora", "Srinagar", "Leh", "Leh"]
print(cities)

city_set = set(cities)
print(city_set)

#convert sets into list
print(list(city_set))

#Len of set
print(len(city_set))

city_set2 = {"Leh", "Nagpur", "London"}

#Union of sets

print(city_set | city_set2)

#Intersection of sets
print(city_set & city_set2)

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
 
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)
 
# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
 
# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
 
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

#SET COMPREHENSION
y = { x ** 2 for x in range(1,10)}

print(y)

z = { x.upper() for x in "Hello"}

print(z)
