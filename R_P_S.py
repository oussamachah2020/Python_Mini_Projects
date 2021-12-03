import random as rm

def check_win_1(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True

def check_win_2(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
        return True

def Play():
    user = str(input("Play 'r' (for rock),'p' (for paper),'s' (for scissor): "))
    choices = ['r', 'p', 's']
    computer = rm.choice(choices)

    if user == computer:
        return print(f'Tie choice {computer}')
    elif check_win_1(user, computer):
        return print(f'Yay! you win {user}')
    elif not check_win_1(user, computer):
        return print(f'You lost {computer}')

def Play_Both():
    player1 = str(input("Play 'r' (for rock),'p' (for paper),'s' (for scissor): "))
    player2 = str(input("Play 'r' (for rock),'p' (for paper),'s' (for scissor): "))

    if player1 == player2:
        return print(f'Tie choice {player1, player2}')
    elif check_win_1(player1, player2):
        return print(f'Yay! you win {player1}')
    elif not check_win_1(player1, player2):
        return print(f'You lost {player2}')

def Players_number():
    Players = int(input("1 <Single Player> | 2 <MultiPlayer>: "))

    if Players == 1:
        Play()
    elif Players == 2:
        Play_Both()

Players_number()

def play_again():
    ask = str(input('Wanna play again?: '))
    if ask == 'y' or ask == 'Y':
        print("\n/*************************/\n")
        Players_number()
    else:
        exit()

while True:
    play_again()
