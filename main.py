def main():
    storage = {}

    while True:
        user_input = input('> ')

        if user_input.lower() == 'exit':
            break
        elif user_input.split()[0].lower() == 'set':
            if len(user_input.split()) < 3:
                print('Invalid command. Use "set <key> <value>".')
                continue
            
            key, value = user_input.split()[1], user_input.split()[2]
            storage[key] = value
        elif user_input.split()[0].lower() == 'get':
            if len(user_input.split()) < 2:
                print('Invalid command. Use "get <key>".')
                continue

            key = user_input.split()[1]
            print(storage.get(key, 'Key not found'))
        else:
            print('Invalid command. Use "set <key> <value>" or "get <key>".')

if __name__ == '__main__':
    main()
