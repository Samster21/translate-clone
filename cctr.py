import argparse, func_definitions as fd

parser = argparse.ArgumentParser()
parser.add_argument("set_1", type=str)
parser.add_argument("-d","--delete", action='store_true')
parser.add_argument("set_2", type=str, default = "")
args = parser.parse_args()


if args.delete == "d":
        print(fd.delete(set1=args.set_1))
else:
    print(fd.translate(set1=args.set_1, set2=args.set_2))