names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

print(min(names, key= lambda n: len(n)))

songs = [
    {"title": "Happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda s: s['playcount']))