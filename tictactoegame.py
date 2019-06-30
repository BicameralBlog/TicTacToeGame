################################
# This is the tic-tac-toe game #
################################

markers=['X','O']
player1=""
player2=""
positions=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_board(positions):
    print('\n')
    print(' ' + positions[0] + ' | ' + positions[1] + ' | ' + positions[2])
    print('¯¯¯¯¯¯¯¯¯¯¯')
    print(' ' + positions[3] + ' | ' + positions[4] + ' | ' + positions[5])
    print('¯¯¯¯¯¯¯¯¯¯¯')
    print(' ' + positions[6] + ' | ' + positions[7] + ' | ' + positions[8])
    print('\n')
def game_setup():
    #sets the players up with their preferred marker (X or O)

    global markers
    global player1
    global player2

    print('Welcome to the tic-tac-toe game!\n')

    while player1 not in ['X','O']:
        player1=input('Player 1, do you want to be "X" or "O"? ').upper()

    markers.remove(player1)
    player2=markers[0]

    return markers,player1,player2
def winning_board():
    global positions
    global markers

    return(\
    positions[0] == positions[1] == positions[2] and (positions[0] == 'X' or positions[0] == 'O') or \
    positions[3] == positions[4] == positions[5] and (positions[3] == 'X' or positions[3] == 'O') or \
    positions[6] == positions[7] == positions[8] and (positions[6] == 'X' or positions[6] == 'O') or \
    positions[0] == positions[3] == positions[6] and (positions[0] == 'X' or positions[0] == 'O') or \
    positions[1] == positions[4] == positions[7] and (positions[1] == 'X' or positions[1] == 'O') or \
    positions[2] == positions[5] == positions[8] and (positions[2] == 'X' or positions[2] == 'O') or \
    positions[0] == positions[4] == positions[8] and (positions[0] == 'X' or positions[0] == 'O') or \
    positions[2] == positions[4] == positions[6] and (positions[2] == 'X' or positions[2] == 'O'))
def full_board():
    global positions

    return set(positions) == {'X','O'}

def game():

    print_board(positions)

    while not winning_board() and not full_board():
        player1_move='0'
        while player1_move not in range(1,10):
            player1_move = int(input('Player 1, choose your position: '))
            while (positions[player1_move-1] == 'X') or (positions[player1_move-1] == 'O'):
                player1_move = int(input(
                'That spot is already taken.\nPlayer 1, choose your position: '))

            else:
                positions[player1_move-1]=player1
                print_board(positions)
    
            break

        if (not winning_board() and not full_board()):
            player2_move='0'
            while player2_move not in range(1,10):
                player2_move = int(input('Player 2, choose your position: '))
                while (positions[player2_move-1] == 'X') or (positions[player2_move-1] == 'O'):
                    player2_move = int(input(
                    'That spot is already taken.\nPlayer 1, choose your position: '))

            else:
                positions[player2_move-1]=player2
                print_board(positions)

    else:
        if winning_board():
            print('there is a winner!')
        else:
            print('we have a full board and no winner :(')
def replay():
    global markers
    global player1
    global player2
    global positions

    replay=input('Do you want to play again? (Y/N): ').lower()
    if replay.startswith('y'):
        markers=['X','O']
        player1=""
        player2=""
        positions=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

        run_game()

def run_game():
    game_setup()
    game()
    replay()

run_game()
