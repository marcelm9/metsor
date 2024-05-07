from .database import Database


def undo(path: str):
    text = Database.load(path)
    if text == None:
        print(f"Cannot undo: no saves for path {path}")
        exit(1)
    
    with open(path, "w") as f:
        f.write(text)
