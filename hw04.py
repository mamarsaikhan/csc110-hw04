# ------------------------------------------------------
#        Name: Marla Amarsaikhan
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Asks for sentences until the user uses the secret word or dog/Dog."""
    while True:
        sentence = input("Give me a sentence: ")
        # checks if the sentence has the secret word first
        if secret_word in sentence:
            print("You used the secret word!")
            # stops the loop, since the match was found
            break
        # checks if the sentence has dog or Dog
        elif "dog" in sentence or "Dog" in sentence:
            # outer single quotes let the inner "dog" quotes show
            print('You used the word "dog" or the word "Dog"!')
            break
        # neither words are used, so the loop repeats
        else:
            print("Try again")

# Task 2
def check_greater():
    """Asks for two integers, compares them, and says which is greater."""
    while True:
        first_integer = int(input("Give me a first integer: "))
        second_integer = int(input("Give me a second integer: "))
        # compares the two numbers
        if first_integer > second_integer:
            print("First is Greater")
            break
        elif second_integer > first_integer:
            print("Second is Greater")
            break
        # they are equal, so the loop repeats
        else:
            print("Try again")
        
# Task 3
def get_special_numbers():
    """Prints the odd multiples of 3 from 1 to 40, that are not multiples of 5."""
    for num in range(1,41): # the range has to end with 41 for 40 to be included
        # skips even numbers; % gives the remainder
        if num % 2 == 0:
            continue
        # skips numbers that are not multiples of 3; != means not equal
        if num % 3 != 0:
            continue
        # skips multiples of 5
        if num % 5 == 0:
            continue
        # it passes every rule
        print(num)

# Task 4.a
def my_for_loop():
    """Labels the letters of a 2-5 character word as a vowel or consonant."""
    word = input("Give me a string: ")
    # rejects words that have the wrong length or with spaces; " " checks for a space
    if len(word) < 2 or len(word) > 5 or " " in word:
        print("bad word")
        return
    #looks at each letter
    for letter in word:
        if letter in "aeiouAEIOU":
            print(f"letter {letter} is a vowel")
        else:
            print(f"letter {letter} is a consonant")
            
# Task 4.b
def my_while_loop():
    """Shows an a/b/c menu until the user picks b (stop) or c (exit)."""
    while True:
        option = input("Choose on option: a, b, or c: ")
        # a: shows the menu again
        if option == "a":
            continue
        # b: says goodbye and stops the loop
        elif option == "b":
            print("Goodbye")
            break
        # c: ends the whole program
        elif option == "c":
            sys.exit()
        # anything else is not an option
        else:
            print("try again")
        
# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
