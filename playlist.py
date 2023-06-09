playlist = {
	'title': 'patagonia bus', 
	'author': 'colt steele', 
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}

total_length = 0

for song in playlist['songs']:
    total_length += song['duration']

print(total_length)


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer =  { i[0]:i[1] for i in person}

# There are many potential solutions for this:

# Using a dictionary comprehension 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}
# An alternate solution using a dict comprehension, without any references to list indexes:

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}
# Finally, a really simple solution.  If you have a list of pairs, you can very easily turn it into a dictionary using dict() 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)