import argparse

def say_hello(name="World"):
    print("Hello  ", name, "!")

parser = argparse.ArgumentParser(description='say hello.')

parser.add_argument('--name', type=str, required=False,
                    metavar='name', help='your name',default='Mitchell')
args= parser.parse_args()

say_hello(args.name)