def main():
    while True:
        print('> ', end='')
        user_input = input()
        if user_input.lower() == 'exit':
            break
        else:
            print(user_input)

if __name__ == '__main__':
    main()
