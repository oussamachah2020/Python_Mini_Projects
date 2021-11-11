import random as rm

# Function to get the user name
def welcome():
    Username = str(input("Enter your name: "))

    #check if the username is only alphabets
    if Username.isalpha():
        print("Hello " + Username + " Welcome to the game")
    else:
        print("Please enter a name of only alphabets")
        Username = input("Enter here: ")
        print("Hello " + Username)

# Function that allow the user to play again
def play_again():
    ask = input("Do you want to play again? : ")

    if ask == 'Y' or ask == 'y':
        game_run()
    else:
        print("Thanks for playing, hope you had fun!!")
        exit()

#Function that generate random words for the user to guess
def get_word():
    words = ['Python', 'Cool', 'Weather', 'exciting', 'happy']

    #use the choice() methode to generate random word from the words var
    return rm.choice(words).lower()


get_word()


def game_run():
    # the welcome function for user name
    welcome()

    # Define a variable for alphabets
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Initiate a variable to generate random words
    word = get_word()

    # Empty list for guessed words
    guessed_letter = []

    # Number of tries allowed for the user
    tries = 6

    # Set guess to False for control the user guesses
    guessed = False

    print("")
    print("The word contains ", len(word), ' letters')
    print(len(word) * '_')

    #A loop for the game rules
    while guessed == False and tries > 0:
        print("You have ", str(tries), " tries")
        guess = input('Guess a letter in the word or enter the full: ')
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have to enter a letter, check your entry make sure you enter an alphabet not a number: ')
            elif guess in guessed_letter:
                print("You have already guessed the letter before. Try again!: ")
            elif guess not in word:
                print('Sorry, That letter is not part of the word:')
                guessed_letter.append(guess)
                tries -= 1
            elif guess in word:
                print('Great! that letter exists in the word!')
                guessed_letter.append(guess)
            else:
                print('Check your entry! You right have entered the wrong entry')

        elif len(guess) == len(word):
            if guess == word:
                print('Great Job! You guessed the word correctly!')
                # guessed == True
            else:
                print('Sorry, that was not the word we were looking for: ')
                tries -= 1

        else:
            print('The length of your guess is not the same as the length of the correct word.')
            tries -= 1

game_run()
play_again()
