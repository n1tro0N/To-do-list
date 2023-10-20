class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return "Добавлено"
        else:
            return "Задача уже существует"

    def edit_task(self, index, new_task):
        if index >= len(self.tasks) or index < 0:
            return "Недопустимый индекс"

        old_task = self.tasks[index]
        self.tasks[index] = new_task
        return f"Задача в индексе {index} была обновлена с {old_task} до {new_task}"

    def delete_task(self, index):
        if index >= len(self.tasks) or index < 0:
            return "Недопустимый индекс"

        task = self.tasks.pop(index)
        return f"Удаленная задача по индексу {index}: {task}"
    def show_tasks(self):
        return self.tasks

    def txt_file(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            file.write(str(self.tasks))

todo_list = TodoList()

while True:
    print("\nДобро пожаловать в список дел!")
    print(f"Ваши задачи: {todo_list.show_tasks()}")

    print("""
1) Добавить задачу
2) Редактировать задачу 
3) Удалить задачу 
4) Сохранение задач в файл
5) Остановить действие
    """)

    action = input("Действие: ")


    if action == "1":
        print("Введите задачу:")
        todo_list.add_task(input())

    elif action == "2":
        index = int(input("Введите индекс: ")) - 1
        new_task = input("Введите новую задачу: ")
        result = todo_list.edit_task(index, new_task)
        print(result)

    elif action == "3":
        index = int(input("Введите индекс: ")) - 1
        result = todo_list.delete_task(index)
        print(result)

    elif action == "4":
        todo_list.txt_file()

    elif action == "5":
        break
    else:
        print('Invalid input')
