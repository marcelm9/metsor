import os
from argparse import ArgumentParser

from metsor.src.checker import check
from metsor.src.sort import sort
from metsor.src.undo import undo

parser = ArgumentParser()
parser.add_argument("function", help="Function to run ('sort' / 'undo')")
parser.add_argument("file", help="Path to the file")
args = parser.parse_args()

function = args.function
path = os.path.abspath(args.file)

check(function, path)

if function == "sort":
    sort(path)
else:
    undo(path)
