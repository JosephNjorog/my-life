import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Non-blocking input
    height, width = stdscr.getmaxyx()

    while True:
        stdscr.clear()
        for i in range(width // 10):
            y = random.randint(0, height - 1)
            x = i * 10
            stdscr.addch(y, x, chr(random.randint(0x0AB0, 0x0ADF)))
        stdscr.refresh()
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
