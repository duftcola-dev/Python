import os 
import sys
import argparse

# creating an argument parser 

arg_parset = argparse.ArgumentParser(description="general purpose CLI")

#add arguments 
arg_parset.add_argument("Path",metavar="path",type=str,help="current path")

# execute the parse_args() method 
args = arg_parset.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))