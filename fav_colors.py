""" ** kwargs """

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


def special_greetings(**kwargs):
    if "Pratik" in kwargs and kwargs["Pratik"] == "special":
        return "You get a special greeting Pratik!"
    elif "Pratik" in kwargs:
        return f"{kwargs['Pratik']} Pratik!"
    
    return "Not sure who this is... "


fav_colors(Colt="purple", Ruby="red", Ethel="teal")

print(special_greetings(Pratik="special", Sheetal="not so special"))