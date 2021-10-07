import random as rm

def Game():
    Testing = True
    while Testing:
        num = input('type a number:')
        if not num.isdigit():
            print('Invalid input!')
        else:
            print("Let's Play!")
            num = int(num)
            Testing = False

        unknown = rm.randint(1, num)

        guess = None
        count = 1
    while guess != unknown:
        guess = input('choose a number between 1 and ' + str(num) + ": ")

        if guess.isdigit():
            guess = int(guess)

        if guess == unknown:
            print('\nGreat!')
        else:
            print('Please try again!\n')
            count += 1

    if count == 1:
        print("It took you " + str(count) + " guess\n")
    else:
        print("It took you " + str(count) + " guesses\n")

Game()
while True:
    Ask = str(input('Do you want to play again? (Y/N): '))
    if Ask == 'Y' or Ask == 'y':
        Game()
    else:
        exit()
