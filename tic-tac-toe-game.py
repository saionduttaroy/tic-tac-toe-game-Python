import os

def cls():
    os.system('cls')

#function I made to display the board
def display_board(board):
    cls()
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print("---|---|---")
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print("---|---|---")
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')

#function to assign mamrker to a player & the opposite marker to the other player
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Function to place marker in the board
def place_marker(board, marker, position):
    board[position] = marker

#Function to check all the winning conditions
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random
#Function to randomly choose a player who'll go first (kind of a toss)
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Function to check if there are any blank spaces left in the board
def space_check(board, position):
    
    return board[position] == ' '

#Function to check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Function to choose the position, if that position is available
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): '))
        
    return position

#Function asking players if they want to play again
def replay():
    
    choice = input('Do you want to play again? Enter Yes or No: ')
    return choice == 'Yes'


#Logic to run thre program
#Introduction message
print('WELCOME TO TIC TAC TOE!')

while True:
    # Reset the board
    my_board = [' '] * 10
    # Taking player input as a tuple from player_input() fnction
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    #Ask the user if they are ready to play the game?
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y': #so that it can take either Yes or yes or Y or y
        # This game_on variable is very imp. in our program
        game_on = True
    else:
        game_on = False
    #
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(my_board)
            position = player_choice(my_board)
            place_marker(my_board, player1_marker, position)

            if win_check(my_board, player1_marker):
                display_board(my_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn (same code copied from player1's turn with appropriate changes)
            
            display_board(my_board)
            position = player_choice(my_board)
            place_marker(my_board, player2_marker, position)

            if win_check(my_board, player2_marker):
                display_board(my_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if replay() == False:
        break