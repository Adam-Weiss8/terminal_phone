# Terminal Phone
# Terminal phone
# Terminal Phone



def phone_tasks(current_tasks):
    current_prompt = input("What would you like to do with your tasks? Create, update, delete, or read? When done type exit\n")
    command = ''
    while(command != 'exit'):
        command = input()
        if command == 'create':
            print('You wish you could create')
            task = input('Name your precious task\n')
            current_tasks.append(task)
            print(f'{task} is a terrible name')
        elif command == 'update':
            print('Update who?')
            task_name = input('At least tell me the name\n')
            if task_name in current_tasks:
                new_task = input('What should the new terrible name be?\n')
                index = current_tasks.index(task_name)
                current_tasks[index] = new_task
            else:
                print ('nothing that terrible exist, sorry')
        elif command == 'delete':
            print('Hasta la vista, Baby')
            task_name = input('What garbage will we be deleting?\n')
            if task_name in current_tasks:
                current_tasks.remove(task_name)
                print(f'Finally, {task_name} is out of my life')
            else:
                print('That poopy is long gone my friend')
        elif command == 'read':
            print('Brandon loves to read')
            print(current_tasks)
        elif command == 'exit':
            print('Finally I can go about my day')
        else:
            'Enter something that works like creat or update or something idk'
        