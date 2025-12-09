# We're going to write a program that will ask the user to input an arbitrary
# number of integers, store them in a collection, and then demonstrate how the
# collection would be used with various control structures.

import sys # Used for the sys.exit function

target_int = input("How many integers? ")

# 1. Convert user input to an integer and handle errors.
try:
    target_int = int(target_int)
except ValueError:
    sys.exit("You must enter an integer.")

# Handle the case where the user asks for zero or a negative number of integers
if target_int <= 0:
    print("No integers to collect.")
    sys.exit()

ints = list()
count = 0

# 2. Keep asking for an integer until we have the required number (while loop)
print("\n--- Collecting Integers ---")
while count < target_int:
    new_int_str = input("Please enter integer {0}: ".format(count + 1))
    
    # Try to convert the input to an integer
    try:
        new_int = int(new_int_str)
        # If conversion is successful, add to the list and increment the counter
        ints.append(new_int)
        count += 1
    except ValueError:
        # If conversion fails, print error and loop again without incrementing 'count'
        print("You must enter an integer. Try again.")

print("\n--- Collection Complete ---")
print("The collected list is: " + str(ints))

# 3. Demonstrate control structures using the 'ints' collection


## Iterating with a For Loop (Value-Based)

print("\nUsing a **for loop** (Iterates over *values*)")
# This is the most "Pythonic" way to iterate over a collection.
for value in ints:
    print("Value: " + str(value))


## Iterating with a While Loop (Index-Based)

print("\nUsing a **while loop** (Iterates using *indices*)")
# We use the len function to find the total number of items.
total = len(ints)
count = 0
while count < total:
    print("Index {0} has value: {1}".format(count, str(ints[count])))
    count += 1
