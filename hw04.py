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
        # check if the sentence has the secret word first
        if secret_word in sentence:
            print("You used the secret word!")
            # stops the loop, since the match was found
            break
        # check if the sentence has dog or Dog
        elif "dog" in sentence or "Dog" in sentence:
            # outer single quotes let the inner "dog" quotes show
            print('You used the word "dog" or the word "Dog"!')
            break
        # neither words were used, so the loop repeats
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
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

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
