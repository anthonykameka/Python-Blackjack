logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """check score, 0 stands for blackhjack"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(logo)
    user_cards = []
    cpu_cards = []
    over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())
    
    
    while not over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"User Cards: {user_cards} // User Score: {user_score}")
        print(f"Computer Card: {cpu_cards[0]}")
        if user_score == 0 or cpu_score == 0 or user_score > 21:
            over = True
        else: 
            keep_going = input("Would you like to draw again? y for yes / n for no")
            if keep_going == "y":
                user_cards.append(deal_card())
            else:
                over = True
    while calculate_score(cpu_cards) < 17:
        cpu_cards.append(deal_card())
    
    print(f"Your hand: {user_cards} -- Your score: {user_score}")
    print(f"Cpu hand {cpu_cards} -- Cpu score: {cpu_score}")
    compare(user_score, cpu_score)
    
        

def compare(user_score, cpu_score):
    if user_score == cpu_score:
        print("It's a Draw....")
    elif user_score > 21:
        print("You lose!")
    elif cpu_score > 21:
        print("You win!")
    else:
        if 21-user_score > 21-cpu_score:
            print("You lose!")
        else: 
            print("You win!")
            
    keep_going = input("Do you want to restart the game  y/n")
    if keep_going == "y":
        play_game()        
    

play_game()
