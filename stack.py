def fifth():
    stack = []
    end = False
    valid_commands = ['END', 'PUSH', 'POP', 'SWAP', 'DUP']
    while not end:
        print(f"stack is {stack}")
        cmd = input("")
        if cmd.split(' ')[0] not in valid_commands:
            print('ERROR')
            end = True
        elif len(cmd.split(' ')) > 2:
            print('ERROR')
            end = True
        elif len(cmd.split(' ')) == 2 and cmd.split(' ')[0] != 'PUSH':
            print('ERROR')
            end = True
        elif cmd == "END":
            end = True
        elif cmd.split(' ')[0] == 'PUSH':
            try:
                stack.append(int(cmd.split(' ')[1]))
            except ValueError:
                print('ERROR')
                end = True
        elif cmd == 'POP':
            stack.pop()
        elif cmd == 'SWAP':
            second_from_last = stack[-2]
            stack[-2] = stack[-1]
            stack[-1] = second_from_last
        elif cmd == 'DUP':
            stack.append(stack[-1])


if __name__ == '__main__':
    fifth()
