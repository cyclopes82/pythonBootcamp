names = ("Pratik", "Sheetal", "Cartoon")

for name in names:
    print(name)


i = len(names) - 1

while i >= 0:
    print(names[i])
    i -= 1

#returns the number of times value appears in tuple
print(names.count("Pratik"))

print(names.index('Pratik'))