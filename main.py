#import random for randomizer, data, and art
import random
from game_data import data
from art import vs
from art import logo
def play():
    print(logo)
    score = 0
    #choosing random dictionary from data
    A = random.choice(data)
    #creating loop for looping through elements
    while True:
        #choosing another random dictionary from data
        B = random.choice(data)
        #if B equals A, choosing another dictionary for b
        while B == A:
            B = random.choice(data)
        #printing out interface
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
        #asking user to answer
        ask = input("Who has more followers? Type 'A' or 'B': ").lower()
        #if they choose correctly increment their scores and show it. also making A = B for B replace A for every correct answer
        if ask == 'a' and B['follower_count'] < A['follower_count']:
            score += 1
            A = B
            print(f"You are right. Current score: {score}")
        elif ask == 'b' and A['follower_count'] < B['follower_count']:
            score += 1
            A = B
            print(f"You are right. Current score: {score}")
        #if they go wrong, show the message they lost and their total score. then break the loop
        else:
            print(f"Sorry, pal. Game over. Total score: {score}")
            ask1 = input("Would you like to play again? Type 'Y' or 'N': ").lower()
            if ask1 == 'y':
                play()
            if ask1 == 'n':
                break
play()