''' Testing Dino Class
    CS 5001 Final Project
    Sam Treadwell
    12/11/2022 '''

from Pet import Dino
from Play import Game

# Testing Dino class with user input and with parameters entered inside function
# Both ways show the method "grow" works based on the information entered

def dino_test():
    my_dino = Dino("Bruce")
    print(my_dino)
    feed = input("What do you want to feed him? Enter feed (either P, S): ")
    my_dino.grow(feed)
    print(my_dino)
    print("...")
    my_dino_2 = Dino("Bruce")
    my_dino_2.grow("M")
    print(my_dino_2)
    print("...")

dino_test()

# Testing Game class with user input and with parameters entered inside function
# Both ways show the method "score" works based on the information entered

def game_test():
    my_game= Game()
    print(my_game)
    roll = input("What roll do you want to make? ")
    my_game.score(roll)
    print(my_game)
    print("...")
    my_game_2 = Game()
    my_game_2.score("HB")
    print(my_game_2)

game_test()
