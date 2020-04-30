#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    from calculator_1 import add, sub, mul, div
    l = len(argv)
    if l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
    elif argv[2] == "-":
        print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
    elif argv[2] == "*":
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
