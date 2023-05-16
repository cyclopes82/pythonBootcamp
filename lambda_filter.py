names = ['austin', 'penny', 'anthony', 'angel', 'billy']

a_names = filter(lambda n:n[0] == 'a',names)

print(list(a_names))