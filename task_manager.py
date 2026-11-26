from task import Task

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title):
        task1 = Task(task_id, title)
        self.tasks.append(task1)

    def get_tasks(self):
        return self.tasks

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        task = self.find_task(task_id)

        if task is not None:
            task.complete()
            return True
        else:
            return False

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is not None:
            self.tasks.remove(task)
            return True
        else:
            return False

manager = TaskManager()
manager.add_task(3, "Купить удаление")
manager.add_task(1, "удаление")
manager.add_task(2, "Купить")
for task in manager.get_tasks():
    print(task.get_info())

manager.complete_task(2)
manager.delete_task(1)

for task in manager.get_tasks():
    print(task.get_info())

