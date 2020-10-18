# This is a two-player game where each player chooses one object.  As we know,
# there are three objects, snake, water, and gun. So, the result will be
#
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.
# In situations where both players choose the same object, the result will be a draw.

# Now moving on to instructions:
# You have to use a random choice function that we studied in tutorial 38,
# to select between, snake, water, and gun.
# You do not have to use a print statement in case of the above function.
# Then you have to give input from your side.
# After getting ten consecutive inputs, the computer will show the result based on each iteration.
# You have to use loops(while loop is preferred).
import random
print('------------WELCOME TO SNAKE WATER GUN GAME------------')
computer = 0
player = 0
def game():
    global computer
    global player
    m = 0
    while (m <= 9):
        pc = input(' \n\n ENTER YOUR CHOICE  \n ')
        k = ['snake', 'gun', 'water']
        l = random.choice(k)
        if pc == 'snake':
            if l == 'snake':
                print(f'\n\nCOMPUTER ALSO CHOOSED SNAKE SO IT IS A TIE BOTH WILL GET 1 POINT '
                      f'\nYou are left with {9 - m} chances')
                computer = computer + 1
                player = player + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
                continue
            elif l == 'gun':
                print(f'\n\nCOMPUTER CHOOSED GUN SO IT KILLED YOUR SNAKE YOU GOT 0 '
                      f'\nYou are left with {9 - m} chance')
                computer = computer + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
            elif l == 'water':
                print(f'\n\nCOMPUTER CHOOSED WATER SO YOUR SNAKE DRANKED THE WATER YOU GET 1 POINT'
                      f'\n you are left with {9 - m} chances')
                player = player + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
        elif pc == 'water':
            if l == 'gun':
                print(f'\n\nCOMPUTER CHOOSE GUN AND IT  GOT USELESS IN WATER SO YOU GET 1 POINT '
                      f'\n you are left with {9 - m} chances')
                player = player + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
            elif l == 'water':
                print(f'\n\nCOMPUTER ALSO  CHOOSE WATER SO BOTH GET ONE POINT'
                      f'\n you are left with {9 - m} chances')
                player = player + 1
                computer = computer + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
            elif l == 'snake':
                print(f'\n\nCOMPUTER CHOOSED SNAKE AND IT DRANK ALL WATER SO YOU GET 0 POINT'
                      f'\n you are left with {9 - m} chances')
                computer = computer + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
        elif pc == 'gun':
            if l == 'gun':
                print(f'\n\nCOMPUTER CHOOSE GUN SO BOTH GET 1 POINT '
                      f'\n you are left with {9 - m} chances')
                player = player + 1
                computer = computer + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
            elif l == 'water':
                print(f'\n\nCOMPUTER CHOOSED WATER  SO YOUR GUN GOT  USELESS YOU GET 0 POINT '
                      f'\n you are left with {9 - m} chances')
                computer = computer + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
            elif l == 'snake':
                print(f'\n\nCOMPUTER CHOOSED SNAKE AND YOUR GUN KILLED IT SO YOU GET 1 POINT '
                      f'\n you are left with {9 - m} chances')
                player = player + 1
                print(f'\n\nYOU HAVE {player} POINTS')
                print(f'\nCOMPUTER HAS {computer} POINTS')
                m = m + 1
    if computer > player:
        print('\n\nSO YOU LOSE')
    if computer < player:
        print('\n\nSO YOU WIN')
    if computer == player:
        print('\n\nSO IT\'S A DRAW' )
    return ' '
print(game())