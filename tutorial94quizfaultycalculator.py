import argparse
import sys
def calc(args):
    if args.o == 'add':
        if args.x == 56 and args.y ==9:
            return 77
        else:
            return args.x + args.y
    elif args.o=='multiply':
        if args.x == 45 and args.y ==3:
            return 555
        else:
            return args.x * args.y
    elif args.o=='subtract':
        return args.x - args.y
    elif args.o=='divide':
        if args.x == 56 and args.y ==6:
            return 4
        else:
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