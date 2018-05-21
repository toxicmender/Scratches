#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
args = parser.parse_args()

answer = args.x**args.y

if args.verbosity >= 3:
    print("Running '{}'".format(__file__))
if args.verbosity >= 2:
    print("{} to the power {} equals ".format(args.x, args.y), end="")
elif args.verbosity >=1:
    print("{}^{} == ".format(args.x, args.y), end="")
print(answer)
