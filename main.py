from store import KeyValueStore

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
