# A command-line utility is a way of giving operating system instructions
# using lines of texts. Command-line programs operate via command line or
# PowerShell. It will interact with a command-line script.

# Now let us come to the why part that why we should use the command-line
# utility in our program. We can call a command line program in python or
# any other language into a different language program easily as each
# program has calling support in it for calling the command lines program.
# So in cases, were are writing a program in some other language, but we
# want to perform a task in Python and call it in our program, then the
# command line can help us to do that.

import argparse
import sys
def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o=='multiply':
        return args.x * args.y
    elif args.o=='subtract':
        return args.x - args.y
    elif args.o=='divide':
        return args.x / args.y
    else:
        return "something went wrong"
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="enter first number. this is a utility for calculation")
    parser.add_argument('--y', type=float, default=3.0,
                        help="enter first number. this is a utility for calculation")
    parser.add_argument('--o', type=str, default='add',
                        help="enter the operator. this is a utility for calculation")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))