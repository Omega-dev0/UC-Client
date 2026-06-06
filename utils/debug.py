import sys

DEBUG = "debug" in sys.argv


def log(*args):
    print("[\033[1;35mDEBUG\033[0m]", *args)
