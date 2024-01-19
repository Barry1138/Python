#Wacky Word Game program
#Part 1: Request the input words.
first_name = input("Type your name, and select enter: ")
print("")
print("Hello " + first_name + ". Let's play a game.")
print("")
adjective1 = input("Tell me an adjective, and select enter. ")
noun1 = input("Tell me a noun (plural), and select enter. ")
noun2 = input("Tell me another noun (plural), and select enter. ")
adjective2 = input("Tell me another adjective, and select enter. ")

#Part 2: Print the poem.
print(first_name + "'s Wacky Word Game")
print("")
print("Roses are " + adjective1)
print(noun1 + " are blue")
print(noun2 + " are " + adjective2)
print("And so are you!")
