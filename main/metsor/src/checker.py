import os
import sys


def check(function: str, path: str):
    if function not in ("sort", "undo"):
        print(f"invalid function: {function}")
        sys.exit(1)
    if not os.path.exists(path):
        print(f"path does not exist: {path}")
        sys.exit(1)
    if not os.path.isfile(path):
        print(f"path is not a file: {path}")
        sys.exit(1)
    if not path.endswith(".py"):
        print(f"path is not a python file: {path}")
        sys.exit(1)
