#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        import sys
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
    except TypeError as te:
        import sys
        print("Exception: {}".format(te), file=sys.stderr)
        return False
