# nargs_example.py
import argparse

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('--input', action='store', type=int, nargs=3) # this argument spects 3 values or throws error

# args = my_parser.parse_args()

# print(args.input)

# ?: a single value, which can be optional
# *: a flexible number of values, which will be gathered into a list
# +: like *, but requiring at least one value
# argparse.REMAINDER: all the values that are remaining in the command line

# nargs_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('input',
                       action='store',
                       nargs='?', # now this arg allows a single optional argument of any type
                       default='my default value') # default is used if no arg is provided

args = my_parser.parse_args()

print(args.input)