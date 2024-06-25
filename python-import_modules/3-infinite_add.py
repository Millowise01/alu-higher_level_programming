#!/usr/bin/python3
from sys import argv

def main():
    argc = len(argv) - 1
    sm = 0

    if argc == 0:
        print("0")
        return

    for i in range(1, argc + 1):
        sm += int(argv[i])

    print("{}".format(sm))


if __name__ == "__main__":
    main()
