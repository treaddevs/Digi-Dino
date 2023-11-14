
class Dino:
    ''' Dino: Ankylosaurus
        Attributes: color, height, legs, tail
        Methods: grow'''

    def __init__(self, dino_name, color = "Purple", tail = "Clubbed"):
        self.name = dino_name
        self.color = color
        self.height = 6
        self.legs = 4
        self.tail = tail

# This is the constructor for the Dino object with attributes for: name, color, height, legs, and tail

    def grow(self, feed):
        feed_lower = feed.lower()
        if feed_lower == "p":
            self.height += 9
            print("WOW! HE GREW! Now he's 15 ft TALL!")
            print("")
        elif feed_lower == "m":
            self.legs += 2
            print("OMG! LOOK! He grew TWO new legs!")
            print("Now he has SIX legs!")
            print("")
        else:
            print("WHEW! Nothing changed!")
            print("")

# The method is "grow" and depending on what the user enters as a feed has the potential 
# to change an attribute for either height or legs  

    def __str__(self):
        output = "Name: " + self.name + "\n" \
                 "Color: " + self.color + "\n" \
                 "Height: " + str(self.height) + " ft" + "\n" \
                 "Legs: " + str(self.legs) + "\n" \
                 "Tail: " + self.tail
        return output

# This is the string object the user will see in the main function
