import os
import sys
import time


def tail(filename=None, lines=10, follow=False):
    current_position=0
    list_of_lines = []
    if filename is None:
        file = sys.stdin
    else:
        try:
            file = open(filename, "r")
            file.seek(0)
        except FileNotFoundError:
            print("File not found")
            return
    while True:
        if filename:
            current_position = file.tell()
        line = file.readline()
        if not line:
            break
        else:
            list_of_lines.append(line)
            sys.stdout.flush()
    print_lines(list_of_lines, lines)
    if follow:
        while True:
            line = file.readline()
            if filename:
                current_position = file.tell()
            if not line:
                time.sleep(0.1)
                if filename:
                    current_size = os.stat(filename).st_size
                    if current_position > current_size:
                        file.seek(current_size)
            else:
                sys.stdout.write(line)
                sys.stdout.flush()


def print_lines(list_of_lines, lines):
    lines_to_show = min(lines, len(list_of_lines))
    position = len(list_of_lines) - lines_to_show
    for i in range(position, len(list_of_lines)):
        print(i, list_of_lines[i])


if __name__ == "__main__":
    try:
        if len(sys.argv) > 3:
            tail(sys.argv[1], int(sys.argv[2]), bool(sys.argv[3]))
        elif len(sys.argv) > 2:
            tail(sys.argv[1], int(sys.argv[2]))
        elif len(sys.argv) > 1:
            tail(sys.argv[1])
        else:
            tail()
    except TypeError:
        print("Wrong types were given")

