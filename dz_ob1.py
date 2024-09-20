# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False
    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
          status = "Выполнено" if self.completed else "Не выполнено"
          return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {status}"

def add_task(tasks, description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].mark_as_completed()
    else:
        print("Неверный индекс задачи.")
def get_pending_tasks(tasks):
    return [task for task in tasks if not task.completed]

def show_tasks(tasks):
    for task in get_pending_tasks(tasks):
        print(task)

tasks = []
add_task(tasks, "Поиграть с котом", "2024-09-25")
add_task(tasks, "Сходить к врачу", "2024-09-20")
add_task(tasks, "Сделать дз по Python", "2024-09-18")
print(f"Текущие задачи: {show_tasks(tasks)}")

mark_task_completed(tasks, 0)
print(f"\nОбновленные задачи: {show_tasks(tasks)}")