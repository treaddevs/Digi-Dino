# CS 5001 Final Project
# Rule-Based Chatbot
# Created by Sam Treadwell
# 12/12/2022

from Pet import Dino
from Play import Game

def responses(first_response):
    if first_response.lower() == "a":
        return "A: You can call me Bee. Bzzzz... Just kidding! At the end of the day, my name is really Renee."
    elif first_response.lower() == "b":
        return "B: Find fun? I didn't know it was lost!"
    elif first_response.lower() == "c":
        return "C: My, oh my! No need to be shy!"

def additional_responses(second_response):
    if second_response.lower() == "d":
        return "D: Yes, I have a pet ankylosaurus."
    elif second_response.lower() == "e":
        return "E: Woohoo! My favorite color is BLUE!"

def ready_feed(ready):
    if ready.lower() == "yes":
        print("OKAY GREAT! Here's his info:")
    elif ready.lower() == "no":
        print("PLEASEEE! I promise he doesn't bite!")
        print("")
        print("Here's his info:")

def ready_play(ready2):
    if ready2.lower() == "yes":
        print("HURRAY! LET'S PLAY!")
        print("")
        print("Initial Scoreboard:")
    elif ready2.lower() == "no":
        print("JUST ONE MORE MINUTE OF FUN AND WE'RE DONE!")
        print("")
        print("Initial Scoreboard:")

def main():
    print("")
    print("Well, hello there! I don't believe we've met. What's your name?")
    print("")
    name = input("Enter name here: ")
    print("")
    print("Interesting! I've never met a", name, "before!")
    print("You know", name + ",", "to keep the ball rolling there's more you can ask me:")
    print("")
    print("A (So, what's your name?)")
    print("B (What do you find fun?)")
    print("C (Umm, I'm not sure what to say)")
    print("")
    first_response = input("Enter response (either A, B, C): ")
    print("")
    print(responses(first_response))
    print("")
    print("GO AHEAD, ASK AWAY:")
    print("D (Do you have any pets?)")
    print("E (What's your favorite color? Answer fast!)")
    print("")
    second_response = input("Enter response (either D, E): ")
    print("")
    print(additional_responses(second_response))
    print("")
    print("HEY! I NEED YOUR HELP!")
    print("My pet dinosaur Bruce is feeling hungry")
    print("Please help me feed him but don't forget...")
    print("")
    print("WATCH OUT FOR ANY CHANGES!")
    print("")
    ready = input("Ready to feed him? (Enter Yes or No): ")
    print("")
    ready_feed(ready)
    print("")
    print("MY DINOSAUR'S INFO:")
    print("")
    my_dino = Dino("Bruce")
    print(my_dino)
    print("")
    print("Feed options:")
    print("P (Pizza)")
    print("S (Sandwich)")
    print("")
    feed = input("Enter feed (either P, S): ")
    print("")
    my_dino.grow(feed.lower())
    print(my_dino)
    print("")
    print("AWESOME!")
    print("Now my dino's feeling thirsty! Help him choose a drink!")
    print("")
    print("Drink options:")
    print("C (Cherry Coke)")
    print("M (Mimosa)")
    print("")
    feed = input("Enter drink (either C, M): ")
    print("")
    my_dino.grow(feed.lower())
    print(my_dino)
    print("")
    print("WONDERFUL!")
    print("Since you came, let's play a quick GAME!")
    print("")
    print("Let's get the ball rolling with some BOWLING")
    print("You get to coach my dino!")
    print("")
    ready2 = input("Ready to play? (Enter Yes or No): ")
    print("")
    ready_play(ready2)
    game = Game()
    print(game)
    print("")
    print("In this game you are scored on: STYLE and POINTS!")
    print("How you coach my dino to roll determines your team's score...")
    print("")
    print("DON'T BE A BORE! CHECK YOUR STYLE AT THE DOOR")
    print("")
    print("Roll options:")
    print("TW (Tail whip (Whoosh woosh))")
    print("HB (Headbutt (High-yahhh))")
    print("")
    roll = input("Which roll do you choose? (Enter TW or HB): ").upper()
    print("")
    game.score(roll)
    print(game)
    print("")
    print("Okay, that's all for now!")
    print("Until the next time ", name, "!", sep="")
    print("")
    ascii_art = ''' 
               __
              / •_)
     _.----._/ /
    /         /
 __/ (  | (  |
/__.-'|_|--|_|

'''
    print(ascii_art)
    print("BYE BYE!")

main()
