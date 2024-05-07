import ast_comments as ast

from .database import Database


def sort(path: str):
    Database.save(path)

    with open(path, "r") as f:
        source_code = f.read()

    try:
        tree = ast.parse(source_code)
    except Exception as e:
        print("encountered an error while parsing python source code:\n")
        raise Exception(str(e).replace("<unknown>, ", ""))

    for cls in tree.body:
        if isinstance(cls, ast.ClassDef):
            methods = [item for item in cls.body if isinstance(item, ast.FunctionDef)]
            methods_sorted = sorted(methods, key=lambda x: x.name)
            cls.body = [
                item for item in cls.body if not isinstance(item, ast.FunctionDef)
            ]
            for method in methods_sorted:
                cls.body.append(method)

    sorted_content = ast.unparse(tree)

    with open(path, "w") as f:
        f.write(sorted_content)
