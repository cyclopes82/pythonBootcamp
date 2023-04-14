""" Truthiness 1 is by default True While 0 is by default False. 0, Empty String, Empty Objects are by default False """

#Below line won't print Anything because 'if 0' is False
if 0:
    print("Yay")
#Below line will print 'Yay?' becyase 'if 1 ' is True
if 1: 
    print("Yay?")

#we can use this truthiness in real life examples as well 
#Below is one such example

print("Enter your Favourite Colour")
colour = input()
#Below condition check if colour is not blank
if colour:
    print(f"{colour} is my favourite too!!")
else:
    print("YOU DIN'T SAY ANYTHING!")