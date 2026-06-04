import random
from itertools import groupby

# Constants
nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = { nine: "9", ten: "10", jack: "J", queen: "Q", king: "K", ace: "A" }

player_score = 0
computer_score = 0

def roll(roll_number):
    numbers = list(range(1, 7))
    dice = [0] * roll_number
    iterations = 0
    while iterations < roll_number:
        iterations = iterations + 1
        dice[iterations-1] = random.choice(numbers)
    return dice

def hand(dice):
    # groupby needs sorted data to group correctly
    sorted_dice = sorted(dice)
    dice_hand = [len(list(group)) for key, group in groupby(sorted_dice)]
    dice_hand.sort(reverse=True)
    
    straight1 = [1, 2, 3, 4, 5]
    straight2 = [2, 3, 4, 5, 6]

    if sorted_dice == straight1 or sorted_dice == straight2:
        return "a straight!"
    elif dice_hand[0] == 5:
        return "five of a kind!"
    elif dice_hand[0] == 4:
        return "four of a kind!"
    elif dice_hand[0] == 3:
        if len(dice_hand) > 1 and dice_hand[1] == 2:
            return "a full house!"
        else:
            return "three of a kind!"
    elif dice_hand[0] == 2:
        if len(dice_hand) > 1 and dice_hand[1] == 2:
            return "two pair."
        else:
            return "one pair."
    else:
        return "a high card."

def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    
    for i in range(len(dice)):
        print("Dice", i + 1, ":", names[dice[i]])

    result = hand(dice)
    print("You currently have", result)

    while True:
        rerolls_input = input("How many dice do you want to throw again (0-5)? ")
        try:
            rerolls = int(rerolls_input)
            if rerolls in (0, 1, 2, 3, 4, 5):
                break
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 0, 1, 2, 3, 4 or 5.")
        
    if rerolls == 0:
        print("You finish with", result)
    else:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = [0] * rerolls
        print("Enter the number of a dice to reroll: ")
        
        iterations = 0
        while iterations < rerolls:
            iterations = iterations + 1
            while True:
                selection_input = input(f"Select dice #{iterations} to change (1-5): ")
                try:
                    selection = int(selection_input)
                    if selection in (1, 2, 3, 4, 5):
                        break
                except ValueError:
                    pass
                print("Oops! I didn't understand that. Please enter 1, 2, 3, 4 or 5.")
            
            dice_changes[iterations-1] = selection - 1
            print("You have marked dice", selection, "for replacement.")

        # Apply the rerolls to the original hand
        iterations = 0
        while iterations < rerolls:
            iterations = iterations + 1
            replacement = dice_rerolls[iterations-1]
            dice[dice_changes[iterations-1]] = replacement

        dice.sort()
        print("\nYour new dice:")
        for i in range(len(dice)):
            print("Dice", i + 1, ":", names[dice[i]])

        result = hand(dice)
        print("You finish with", result)

def play_again():
    answer = input("Would you like to play again? y/n: ").strip().lower()
    if answer in ("y", "yes", "of course!"):
        return True
    else:
        print("Thank you very much for playing our game. See you next time!")
        return False

def scores():
    global player_score, computer_score
    print("\n--- HIGH SCORES ---")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

def game():
    print("\nThe computer will help you throw your 5 dice.")
    throws()
    return play_again()

def start():
    print("Let's play a game of Python Poker Dice.")
    while game():
        pass
    scores()

if __name__ == '__main__':
    start()
