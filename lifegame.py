import curses

def load(path):
    inputfile = open(path ,'r')
    data = inputfile.read()
    inputfile.close()
    return data
def set_board(data):
    game_cell = []
    for i in range(0, 8):
            game_cell.append(data[(i*9) : ((i+1)*9 -1) ])
    cur_board = [[0 for col in range(8)] for row in range(8)]

    for i in range(0, len(game_cell)):
        for j in range(0, len(game_cell)):
            if(game_cell[i][j]=='X'):
                cur_board[i][j]=0
            else:
                cur_board[i][j]=1
    return cur_board

#주변에 박테리아 개수를 세는 함수, 현재 위치와 현재 보드상태를 입력인자로 사용
def count_bacteria(i, j, board):
    count = 0 #박테리아 개수를 저장할 변수

    '''기존의 8*8 2차원 배열은 (0,0)은 3개의 공간만 탐색하면 되지만, (1,1)은 8개의
    공간을 탐색해야함. 모든 좌표에서 탐색하는 공간을 똑같게 만들어주기 위해
    8*8 2차원 배열 테두리에 0을 추가한 test_board라는 10*10 2차원 배열을 만듬'''
    test_board = [[0 for col in range(10)] for row in range(10)]
    for n in range(1, 9):
        for m in range(1, 9):
            test_board[n][m] = board[n-1][m-1]

    #테두리에 0이 추가되었으므로 현재 위치에서 X,Y축으로 +1씩 움직임.
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

    #계산된 카운트값 반환
    return count


def printBoard(board):

    stdscr.clear() #화면 초기화

    stdscr.addstr("\n    LifeGame\n", curses.color_pair(1)) # 게임 제목
    stdscr.addstr("  ┌─────────┐\n") # 테두리

    for i in range(8):
        stdscr.addstr('  │ ') #테두리
        for j in range(8):
            if board[i][j] == 1:
                stdscr.addstr('O', curses.color_pair(1)) #박테리아가 있는 곳은 O로 표기
            else:
                stdscr.addstr(' ') #박테리아가 없는 곳은 공백
        stdscr.addstr('│\n') #테두리

    stdscr.addstr("  └─────────┘\n") #테두리
    stdscr.refresh() #화면에 보여줌

def runLifeGame(board):

    #변경된 내용이 저장될 새로운 8*8 보드 생성 : 모든 초기값 = 0
    new_board = [[0 for col in range(8)] for row in range(8)]
    new_bacteria_count = 0
    for i in range(8):
        for j in range(8):
            #주변 박테리아 개수 탐색
            temp_bacterai_count = count_bacteria(i,j,board)
            #박테리아가 있을 때
            if board[i][j] == 1:
                #박테리아가 1개 이하일 경우 외로워서 사망
                if temp_bacterai_count <= 1:
                    new_board[i][j] = 0
                #박테리아가 4개 이상일 경우 갑갑해서 사망
                elif temp_bacterai_count >= 4:
                    new_board[i][j] = 0
                else: #박테리아 유지
                    new_board[i][j] = 1
                    new_bacteria_count += 1
            #박테리아가 없을 때
            else:
                #주변에 박테리아가 3개 있으면 박테리아가 생성
                if temp_bacterai_count == 3:
                    new_board[i][j] = 1
                    new_bacteria_count += 1

    #완성된 new_board를 반환 해줌
    return new_board
