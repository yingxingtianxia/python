import getpass

userdb = {}

def register():
    username = input('username: ')
    if username in userdb:
        print('\033[31;1m%s already exists.\033[0m' % username)
    else:
        password = input('password: ')
        userdb[username] = password

def login():
    username = input('username: ')
    password = getpass.getpass('password: ')
    # if username not in userdb or userdb['username'] != password:
    if userdb.get(username) != password:
        print('\033[31;1mLogin incorrect\033[0m')
    else:
        print('\033[32;1mLogin successful\033[0m')

def show_menu():
    prompt = """(0) register
(1) login
(2) quit
Please input your choice(0/1/2): """
    cmds = {'0': register, '1': login}

    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print('Invalid choice. Try again.')
            continue

        if choice == '2':
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
