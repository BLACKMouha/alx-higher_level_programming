#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv) - 1
    if len_argv >= 1:
        len_argv = 0
        result = 0
        for arg in sys.argv:
            if len_argv != 0:
                arg = int(arg)
                result += arg
            len_argv += 1
        print(result)
