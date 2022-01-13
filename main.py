import sys

import lifegame
import os
import curses

data = lifegame.load('inputdata.txt')
cur_board = lifegame.set_board(data)

time = 1000
time_intergration = 0

lifegame.stdscr = curses.initscr()

curses.curs_set(0)
curses.start_color()
curses.init_pair(1, 3, 0)

while(True):
    lifegame.printBoard(cur_board)
    next_board = lifegame.runLifeGame(cur_board)
    cur_board = next_board
    curses.napms(time)

    time_intergration+=time
    if(time_intergration > 5000):
        break

curses.endwin()
