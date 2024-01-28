import json
from pathlib import Path
from dataclasses import asdict
from lib.models.user import User

root_dir = Path(__file__).resolve().parent.parent.parent
temp_dir = root_dir / 'temp'

def read_from_file(file_path, data_class):
    try:
        with open(file_path) as file:
            json_data = json.load(file)
            return [data_class(**item) for item in json_data]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from file '{file_path}'.")
        return None


def save_to_file(file_path, data_objects):
    try:
        data_dicts = [asdict(obj) for obj in data_objects]
        with open(file_path, 'w') as file:
            json.dump(data_dicts, file)
        print(f"Data successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error: Unable to write data to file '{file_path}'. {e}")


def generate_user_data():
    user = User.generate_random()
    save_to_file( f"{temp_dir}/user_data.json", [user])
    return user
