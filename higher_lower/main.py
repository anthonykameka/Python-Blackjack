#Higher/lower
# game comparing social media followings
# Importing data from data file.
# simple logic

from art import logo, vs
from data import data
import random


def play_game():
    score = 0
    still_playing = True #game runner
    while still_playing:
        print(logo)
        print("Guess who has the bigger social media following. Remember, social media is fake, kids.")
        
        if score == 0:
            print(f"Good luck! Current score: {score}")
        
        print(f"You're Right! Current score: {score}")
        a = data[random.randint(0, len(data)-1)]
        b = data[random.randint(0, len(data)-1)]
        while b == a:
            b = data[random.randint(0, len(data)-1)]
        a_followers = a['follower_count']
        b_followers = b['follower_count']
        winner = None
        if a_followers > b_followers:
            winner = "A"
        else:
            winner = "B"
        
        print(f"Challenger A - {a['name']} - {a['description']} - from {a['country']}")
        print(vs)
        print(f"Challenger B - {b['name']} - {b['description']} - from {b['country']}")
        user_guess = "T"
        while user_guess.upper() != "A" and user_guess.upper() != "B":
                user_guess = input("Who has more followers? Type 'A' or 'B' ")
        
        if user_guess == winner: 
            print("You won!")
            score += 1
        
        else:
            print("Nope - WRONG!")
            print(f"final score: {score}")
            keep_going = input("play again? Y / N")
            if keep_going.upper() == "Y":
                play_game()
            else:
                
                still_playing = False
        
                

        
play_game()