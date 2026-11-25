class Task():
    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False
    def complete(self):
        self.completed = True
    def get_info(self):
        if self.completed == True:
            status = "Выполнено"
        else:
            status = "Не выполнено"

        return f"Задача №{self.task_id}: {self.title} | {status}"

task1 = Task(1, "Купить лапму")
task2 = Task(2, "Выучить Java")

print(task1.get_info())
print(task2.get_info())

task1.complete()
task2.get_info()

print(task1.get_info())
print(task2.get_info())