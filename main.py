import json
import os

DB_FILE = 'db.json'

def load_db() -> dict:
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='UTF-8') as db:
            return json.load(db)
    return {}

def save_db(storage) -> None:
    with open(DB_FILE, 'w', encoding='UTF-8') as db:
        json.dump(storage, db, indent=4)


def main():
    storage = load_db()

    while True:
        user_input = input('> ')
        parts = user_input.split()
        if not parts:
            continue

        command = parts[0].lower()

        if command == 'exit':
            break

        elif command == 'set':
            if len(parts) < 3:
                print('Invalid command. Use "set <key> <value>".')
                continue

            key, value = parts[1], parts[2]
            storage[key] = value
            save_db(storage)

        elif command == 'get':
            if len(parts) < 2:
                print('Invalid command. Use "get <key>".')
                continue

            key = parts[1]
            print(storage.get(key, 'Key not found'))

        else:
            print('Invalid command. Use "set <key> <value>" or "get <key>".')

if __name__ == '__main__':
    main()
