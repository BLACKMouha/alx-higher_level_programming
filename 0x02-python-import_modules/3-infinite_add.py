#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv)
    if len_argv > 1:
        len_argv = 0
        result = 0
        for arg in argv:
            if len_argv != 0:
                arg = int(arg)
                result += arg
            len_argv += 1
        print(result)
