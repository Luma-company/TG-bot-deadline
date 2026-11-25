from task import Task

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title):
        task1 = Task(task_id, title)
        self.tasks.append(task1)

    def get_tasks(self):
        return self.tasks

    def dinf_task(self, task_id):
        for id in self.tasks:
            if id == task_id:
                return self.tasks
            else:
                return None