def fifth():
    stack = []
    end = False
    valid_commands = ['END', 'PUSH']
    while not end:
        print(f"stack is {stack}")
        cmd = input("")
        if cmd.split(' ')[0] not in valid_commands:
            print('ERROR')
        if cmd == "END":
            end = True
        if cmd.split(' ')[0] == 'PUSH':
            if len(cmd.split(' ')) > 2:
                print('ERROR')
            try:
                stack.append(int(cmd.split(' ')[1]))
            except ValueError:
                print('ERROR')


if __name__ == '__main__':
    fifth()
