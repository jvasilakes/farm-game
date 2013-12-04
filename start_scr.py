import curses
import time


def print_pic(file, window):
    row = 0
    for line in file:
        window.addstr(row, 0, line)
        row += 1

def animation():
    tree1 = open('tree1').readlines()
    tree2 = open('tree2').readlines()
    farm = open('farm').readlines()

    scr = curses.initscr()

    win = curses.newwin(35, 70, 10, 30)
    win.box()
    win.refresh()
    win2 = curses.newwin(30, 65, 14, 32)

    i = 0
    while i <= 4:
        print_pic(tree1, win2)
        win2.refresh()
        time.sleep(1)
        print_pic(tree2, win2)
        win2.refresh()
        time.sleep(1)
        i += 1

    txt_win = curses.newwin(6, 29, 20, 50)
    print_pic(farm, txt_win)
    txt_win.refresh()
    time.sleep(2)

    win.addstr(32, 22, "Press any key to start.")
    win.refresh()
    win.getch()
