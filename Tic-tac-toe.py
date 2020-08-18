import random
#create board
def display_board(board):
    print('-------------- ')
    print(test_board[7] + ' | ' , test_board[8] + ' | ', test_board[9] + ' | ')
    print('-------------- ')
    print(test_board[4] + ' | ', test_board[5] + ' | ',test_board[6] + ' | ')
    print('-------------- ')
    print(test_board[1] + ' | ', test_board[2] + ' | ', test_board[3] + ' | ')

#player input function
def player_input():
    marker = ' '
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose your marker ! (X or O)').upper()
    
    if marker[0] == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
#placemarker function
def place_marker(board, marker, position):
    board[position] = marker
   
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
   
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
    
def space_check(board, position):
     return board[position] == ' '
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
       
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board, position) :
        position = int(input('Choose a position (1-9)'))
    
    return position

def replay():
    answer = ''
    
    while not (answer == 'y' or answer == 'n'):
        answer = input('Do you want to play again? (y or n)')
    if answer.lower() == 'y':
        return True
    else:
        return False
        
##game code

print('Welcome to my first game made on python - Tic Tac Toe!')
# Reset the board
while True:
    test_board = [' ']*10                                   #Display blank board
                                      
    (player1_marker, player2_marker) = player_input()       #Players Choose Marker
    turn = choose_first() 
    print(turn + ' goes first!') 
    
    #Decides who goes first - Game is ready
    ready_check = input('Are you readyyyyyy - Yes or No??')
    if ready_check[0].lower() == 'y':
        game_on = True
    else:
        game_on = False
    
        
# Player1's turn.
    
    while game_on:                                                                             
        if turn == 'player1':
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1_marker, position)
            
            
            
            if win_check(test_board,player1_marker):
                print('Player1 Wins!')
                display_board(test_board)
                game_on = False
            else:
                if full_board_check(test_board):
                    
                    print('Its a tie!')
                    display_board(test_board)
                    break
                else:
                    turn = 'player2'
                    print('Player2 - your turn!')
                    
#player2's turn   
        if turn == 'player2':
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2_marker, position)
           
            
            
            if win_check(test_board,player2_marker):
                print('Player2 Wins!')
                display_board(test_board)
                game_on = False
            else:
                if full_board_check(test_board):
                    print('Its a tie!')
                    display_board(test_board)
                    break
                else:
                    turn = 'player1'
                    print('Player1 - your turn!')
                    
    if not replay():
        print('Thanks for playing !')
        break

