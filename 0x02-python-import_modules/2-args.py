#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv) - 1

    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    elif i == 1:
        print("{} argument:".format(len_argv))
    else:
        print("{} arguments:".format(len_argv))

    if len_argv > 0:
        i = 0
        for arg in argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
