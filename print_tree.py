import curses
import time
from sys import argv

def print_pic(filename, window):
    tree = open(filename).xreadlines()
    row = 0
    for line in tree:
        window.addstr(row, 0, line)
        row += 1

script, file1, file2, file3 = argv

scr = curses.initscr()

win = curses.newwin(35, 70, 10, 30)
win.box()
win.refresh()
win.getch()
win2 = curses.newwin(30, 65, 14, 32)

i = 0
while i <= 4:
    print_pic(file1, win2)
    win2.refresh()
    time.sleep(1)
    print_pic(file2, win2)
    win2.refresh()
    time.sleep(1)
    i += 1

txt_win = curses.newwin(6, 29, 20, 50)
print_pic(file3, txt_win)
txt_win.refresh()
time.sleep(2)

win.addstr(32, 22, "Press any key to start.")
win.refresh()
win.getch()

curses.endwin()
