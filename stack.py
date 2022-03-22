def fifth():
    stack = []
    end = False
    valid_commands = ['END']
    while not end:
        print(f"stack is {stack}")
        cmd = input("")
        if cmd not in valid_commands:
            print('ERROR')
        if cmd == "END":
            end = True


if __name__ == '__main__':
    fifth()
