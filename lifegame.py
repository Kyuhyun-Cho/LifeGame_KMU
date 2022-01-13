import curses

def load(path):
    inputfile = open(path ,'r')
    data = inputfile.read()
    inputfile.close()
    return data
def set_board(data):
    game_cell = []
    for i in range(0, 8):
            game_cell.append(data[(i*9) : ((i+1)*9 -1)])
    cur_board = [[0 for col in range(8)] for row in range(8)]

    for i in range(0, len(game_cell)):
        for j in range(0, len(game_cell)):
            if(game_cell[i][j]=='X'):
                cur_board[i][j]=0
            else:
                cur_board[i][j]=1
    return cur_board


def count_bacteria(i, j, board):

    count = 0

    test_board = [[0 for col in range(10)] for row in range(10)]
    for n in range(1, 9):
        for m in range(1, 9):
            test_board[n][m] = board[n-1][m-1]

    test_i = i+1
    test_j = j+1


    if test_board[test_i-1][test_j-1] == 1:
        count += 1
    if test_board[test_i-1][test_j] == 1:
        count += 1
    if test_board[test_i-1][test_j+1] == 1:
        count += 1
    if test_board[test_i][test_j-1] == 1:
        count += 1
    if test_board[test_i][test_j+1] == 1:
        count += 1
    if test_board[test_i+1][test_j-1] == 1:
        count += 1
    if test_board[test_i+1][test_j] == 1:
        count += 1
    if test_board[test_i+1][test_j+1] == 1:
        count += 1

    return count


def printBoard(board):

    stdscr.clear()

    stdscr.addstr("\n    LifeGame\n", curses.color_pair(1))
    stdscr.addstr("  ┌─────────┐\n")

    for i in range(8):
        stdscr.addstr('  │ ')
        for j in range(8):
            if board[i][j] == 1:
                stdscr.addstr('O', curses.color_pair(1))
            else:
                stdscr.addstr(' ')
        stdscr.addstr('│\n')

    stdscr.addstr("  └─────────┘\n")
    stdscr.refresh()

def runLifeGame(board):

    new_board = [[0 for col in range(8)] for row in range(8)]
    new_bacteria_count = 0
    for i in range(8):
        for j in range(8):
            temp_bacterai_count = count_bacteria(i,j,board)
            if board[i][j] == 1:
                if temp_bacterai_count <= 1:
                    new_board[i][j] = 0
                elif temp_bacterai_count >= 4:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
                    new_bacteria_count += 1
            else:
                if temp_bacterai_count == 3:
                    new_board[i][j] = 1
                    new_bacteria_count += 1

    return new_board
