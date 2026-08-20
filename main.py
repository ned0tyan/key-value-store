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
        parts = user_input.split(maxsplit=2)
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

        elif command == 'del':
            if len(parts) < 2:
                print('Invalid command. Use "del <key>".')
                continue

            key = parts[1]
            if key in storage:
                del storage[key]
                save_db(storage)
                print('OK')
            else:
                print('Key not found')

        elif command == 'exists':
            if len(parts) < 2:
                print('Invalid command. Use "exists <key>"')
                continue

            key = parts[1]
            print(int(key in storage))

        elif command == 'all':
            if len(parts) > 1:
                print('Invalid command. Use "all"')
                continue

            if not storage:
                print("(empty)")
            else:
                for key, value in storage.items():
                    print(f'{key}: {value}')
        
        else:
            print('Invalid command. Use "set", "get", "all", "del", "exists"')

if __name__ == '__main__':
    main()
