import os
import sys
import time
import argparse


def tail(filename=None, lines=10, follow=True):
    current_position=0
    list_of_lines = []
    if filename is None:
        file = sys.stdin
    else:
        try:
            file = open(filename, "r", encoding="utf-8")
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
        parser = argparse.ArgumentParser(description="Simple tail")
        parser.add_argument("file", nargs="?", default=None, help="Filename")
        parser.add_argument("--lines", "-n", type=int, default=10, help="Number of lines")
        parser.add_argument("--follow", action="store_true", help="Continue after last line")
        args = parser.parse_args()
        tail(args.file, args.lines, args.follow)
    except TypeError:
        print("Wrong types were given")

