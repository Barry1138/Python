import random

player_score = 0
computer_score = 0

def display_hangman(count):
    """Displays the ASCII art based on the number of wrong guesses."""
    graphic = [
        """
             +-------+
             |
             |
             |
             |
             |
            ============
        """,
        """
             +-------+
             |       |
             |
             |
             |
             |
            ============
        """,
        """
             +-------+
             |       |
             |       0
             |
             |
             |
            ============
        """,
        """
             +-------+
             |       |
             |       0
             |       |
             |
             |
            ============
        """,
        """
             +-------+
             |       |
             |       0
             |      -|
             |
             |
            ============
        """,
        """
             +-------+
             |       |
             |       0
             |      -|-
             |
             |
            ============
        """,
        """
             +-------+
             |       |
             |       0
             |      -|-
             |      /
             |
            ============
        """,
        """
             +-------+
             |       |
             |       0
             |      -|-
             |      / \
             |
            ============
        """]
    # Ensure we don't try to access an index that doesn't exist
    if count < len(graphic):
        print(graphic[count])

def game():
    global computer_score, player_score
    
    dictionary = ["gnu", "kernel", "linux", "mageia", "penguin", "mint"]
    word = random.choice(dictionary)
    word_length = len(word)
    clue = ["_"] * word_length
    
    # We have 8 graphics (0-7), so the player gets 7 wrong guesses 
    # before the 8th graphic (the full man) ends the game.
    tries = 7 
    letters_tried = ""
    letters_wrong = 0

    print("\n" + "="*30)
    print("NEW GAME STARTED")
    print("="*30)

    while (letters_wrong < tries) and ("".join(clue) != word):
        # 1. Show the hangman FIRST
        display_hangman(letters_wrong)
        
        # 2. Show the current progress
        print("Word: " + " ".join(clue))
        print(f"Used letters: {letters_tried}")
        print(f"Wrong guesses left: {tries - letters_wrong}")

        # 3. Get the guess
        letter = input("\nTake a guess: ").strip().lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print(">> Please enter exactly one letter.")
            continue
            
        if letter in letters_tried:
            print(f">> You already tried '{letter}'.")
            continue

        # 4. Process the guess
        letters_tried += letter
        if letter in word:
            print(f">> Yes! '{letter}' is in the word.")
            for i in range(word_length):
                if letter == word[i]:
                    clue[i] = letter
        else:
            letters_wrong += 1
            print(f">> Sorry, '{letter}' is not there.")

    # Final Display (Win or Loss)
    display_hangman(letters_wrong)
    
    if "".join(clue) == word:
        print(f"WINNER! The word was: {word}")
        player_score += 1
    else:
        print("GAME OVER.")
        print(f"The word was: {word}")
        computer_score += 1
        
    return play_again()

def play_again():
    answer = input("\nWould you like to play again? (y/n): ").lower()
    return answer.startswith('y')

def scores():
    global player_score, computer_score
    print("\n" + "*"*20)
    print("   FINAL SCORES")
    print(f"   Player:   {player_score}")
    print(f"   Computer: {computer_score}")
    print("*"*20 + "\n")

def start():
    print("Welcome to Linux Hangman!")
    playing = True
    while playing:
        playing = game()
    scores()

if __name__ == '__main__':
    start()
