import argparse, sys, func_definitions as fd

parser = argparse.ArgumentParser()
parser.add_argument("-d","--delete", action='store_true')
parser.add_argument("set_1", help="The first set of character(s)")
parser.add_argument("set_2", nargs="?", default = " ")
args = parser.parse_args()

if sys.stdin.isatty():  # Check if input is from the terminal
    text = input("Please enter a text: ")
else:  # Input from pipe
    text = sys.stdin.read().strip()

    
if args.delete:
        print(fd.delete(user_input=text,set1=args.set_1))
else:
    print(fd.translate(user_input=text,set1=args.set_1, set2=args.set_2))