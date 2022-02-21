import os 
import sys
import argparse

# an argument create parser 
# my_parser = argparse.ArgumentParser(prog="python_cli",usage='%(prog)s [options] path',description="list of a folder content",epilog="enjoy your program",fromfile_prefix_chars='@')

# # Add the arguments # this is the most basic way to create an argument
# my_parser.add_argument('Path',
#                        metavar='path',
#                        type=str,
#                        help='the path to list')

# my_parser.add_argument('a',
#                        help='a first argument')

# my_parser.add_argument('b',
#                        help='a second argument')

# my_parser.add_argument('c',
#                        help='a third argument')

# my_parser.add_argument('d',
#                        help='a fourth argument')

# my_parser.add_argument('e',
#                        help='a fifth argument')

# my_parser.add_argument('-v',
#                        '--verbose',
#                        action='store_true',
#                        help='an optional argument')

# notice this will make my_parser require all this arguments 
# Execute parse_args()


# argumentes with abreviations
# other_parser = argparse.ArgumentParser()
# other_parser.add_argument('--input',
#                        type=int,
#                        action="store",required=True)
# other_parser.add_argument('--id',
#                        type=int,
#                        action="store")

# args = other_parser.parse_args()
# print(args.input)


# positional arguments vs optional arguments

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')
my_parser.add_argument('-l',
                       '--long',
                       action='store_true',
                       help='enable the long listing format')

# Execute parse_args()
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

for line in os.listdir(input_path):
    if args.long:  # Simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d  %s' % (size, line)
    print(line)

# argument action : 

# store : stores the input value to the Namespace object. (This is the default action.)
# store_const : stores a constant value when the corresponding optional arguments are specified.
# store_true : stores the Boolean value True when the corresponding optional argument is specified and stores a False elsewhere.
# store_false : stores the Boolean value False when the corresponding optional argument is specified and stores True elsewhere.
# append : stores  a list, appending a value to the list each time the option is provided.
# append_const : stores a list appending a constant value to the list each time the option is provided.
# count : stores an int that is equal to the times the option has been provided.
# help : shows a help text and exits.
# version : shows the version of the program and exits.