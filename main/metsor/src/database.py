import json
import os
from hashlib import sha256

db_path = os.path.join(os.path.dirname(__file__), "db")
mapping_path = os.path.join(db_path, "mapping.json")


class Database:

    def __safety_check():
        if not os.path.exists(mapping_path):
            with open(mapping_path, "w") as f:
                f.write("{}")

    @staticmethod
    def save(path: str):
        Database.__safety_check()

        sha_name = sha256(path.encode()).hexdigest()

        with open(mapping_path, "r") as f:
            mapping: dict = json.load(f)
        mapping[path] = sha_name
        with open(mapping_path, "w") as f:
            json.dump(mapping, f)

        with open(path, "r") as source, open(os.path.join(db_path, sha_name), "w") as target:
            target.write(source.read())

    @staticmethod
    def load(path: str) -> str | None:
        Database.__safety_check()

        with open(mapping_path, "r") as f:
            mapping: dict = json.load(f)

        if not path in mapping.keys():
            return None
        
        file_path = os.path.join(db_path, mapping[path])
        with open(file_path, "r") as f:
            text = f.read()

        del mapping[path]
        with open(mapping_path, "w") as f:
            json.dump(mapping, f)
        os.remove(file_path)

        return text
