def fifth():
    stack = []
    end = False
    valid_commands = ['END', 'PUSH', 'POP']
    while not end:
        print(f"stack is {stack}")
        cmd = input("")
        if cmd.split(' ')[0] not in valid_commands:
            print('ERROR')
        elif len(cmd.split(' ')) > 2:
            print('ERROR')
        elif len(cmd.split(' ')) == 2 and cmd.split(' ')[0] != 'PUSH':
            print('ERROR')
        elif cmd == "END":
            end = True
        elif cmd.split(' ')[0] == 'PUSH':
            try:
                stack.append(int(cmd.split(' ')[1]))
            except ValueError:
                print('ERROR')
        elif cmd == 'POP':
            stack.pop()


if __name__ == '__main__':
    fifth()
