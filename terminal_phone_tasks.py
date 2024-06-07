# Terminal Phone
current_tasks = []
def phone_tasks(current_tasks):
    command = ''
    while(command != 'exit'):
        command = input()
        if command == 'create':
            print('You wish you could create')
        elif command == 'update':
            print('Update who?')
        elif command == 'delete':
            print('Hasta la vista, Baby')
        elif command == 'read':
            'Brandon loves to read'
        else:
            'Enter something that works'
