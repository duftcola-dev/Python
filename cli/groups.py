# groups.py
import argparse

my_parser = argparse.ArgumentParser()
my_group = my_parser.add_mutually_exclusive_group(required=True)

# this ar mutually exclusive groups of arguments
my_group.add_argument('-v', '--verbose', action='store_true')
my_group.add_argument('-s', '--silent', action='store_true')

args = my_parser.parse_args()

print(vars(args))