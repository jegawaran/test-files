def todoList():
    todo_list =[]
    finished = False
    while not finished:
        task = input("Enter a task for your todo list. Press <enter> Once done: ")
        if len(task) == 0:
            finished = True
        else:
            todo_list.append(task)
            print("TaSK aDDed")

    print()
    print("your todo list: ")
    print('-' * 16)
    print(todo_list)
    for task in todo_list:
        print(task)

todoList()
