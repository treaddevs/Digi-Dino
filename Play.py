
class Game:
    ''' Game: Bowling
        Attributes: style, points
        Methods: score'''

    def __init__(self):
        self.style = 0
        self.points = 0
    
# This is the constructor for the game of bowling
# Starting out the scoreboard is cleared with 0 for both style and points

    def score(self, roll):
        if roll == "TW":
            self.style += 25
            self.points += 10
            print("OOOH! STRIKEEE! You knocked them all down!")
            print("And all the while, you brought the style!")
            print("")
        elif roll == "HB":
            self.style += 15
            self.points += 7
            print("BOOM! SCORE! 7 went to heaven with all those points!")
            print("Crikey! Look at that style! What are you, part crocodile?")
            print("")

# The method is "score" which is determined on how the player rolls
# There are only two options for roll, so both will show a change on the scoreboard

    def __str__(self):
        output = "Style: " + str(self.style) + "\n" \
                 "Points: " + str(self.points)
        return output

# This is the string object the user will see in the main function