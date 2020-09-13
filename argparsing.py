#!/usr/bin/env python
from rich import print
import argparse
import sys

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Python script to test argparsing')
    parser.add_argument('-a','--defa', help='Default option a', action='store_true')
    parser.add_argument('-retstr', help='Default str option q', type=str)

    args = parser.parse_args(args)

    if len(sys.argv) == 1:                       # check if no arguments were provided
        parser.print_help()
        print
        sys.exit(1)

    return args

def main():

    args = getOptions(sys.argv[1:])

    if args.defa:
        print(args.defa)
    elif args.defQ:
        print(args.defQ)


if __name__ == '__main__':
    main()