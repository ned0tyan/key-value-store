import json
import os

class KeyValueStore:
    def __init__(self, db_file: str = 'db.json'):
        self.db_file = db_file
        self.storage = self._load_db()

    def _load_db(self) -> dict:
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r', encoding='UTF-8') as db:
                return json.load(db)
        return {}

    def _save_db(self) -> None:
        with open(self.db_file, 'w', encoding='UTF-8') as db:
            json.dump(self.storage, db, indent=4)

    def set(self, key: str, value: str) -> None:
        # TODO: Добавь ключ и значение в self.storage и вызови self._save_db()
        self.storage[key] = value
        self._save_db()

    def get(self, key: str) -> str:
        # TODO: Верни значение по ключу или 'Key not found'
        return self.storage.get(key, 'Key not found')

    def delete(self, key: str) -> bool:
        # TODO: Удали ключ из self.storage, вызови self._save_db() и верни True.
        # Если ключа нет — верни False.
        if key not in self.storage:
            return False
        del self.storage[key]
        self._save_db()
        return True

    def exists(self, key: str) -> bool:
        # TODO: Верни True или False
        return key in self.storage

    def get_all(self) -> dict:
        # TODO: Верни self.storage
        return self.storage



def main():
    db = KeyValueStore()

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
            db.set(key, value)
            print('OK')

        elif command == 'get':
            if len(parts) < 2:
                print('Invalid command. Use "get <key>".')
                continue

            key = parts[1]
            print(db.get(key))

        elif command == 'del':
            if len(parts) < 2:
                print('Invalid command. Use "del <key>".')
                continue

            key = parts[1]
            print('OK' if db.delete(key) else 'Key not found')

        elif command == 'exists':
            if len(parts) < 2:
                print('Invalid command. Use "exists <key>".')
                continue

            key = parts[1]
            print(int(db.exists(key)))

        elif command == 'all':
            if len(parts) > 1:
                print('Invalid command. Use "all"')
                continue

            if not db.get_all():
                print("(empty)")
            else:
                for key, value in db.get_all().items():
                    print(f'{key}: {value}')
        
        else:
            print('Invalid command. Use "set", "get", "all", "del", "exists"')

if __name__ == '__main__':
    main()
