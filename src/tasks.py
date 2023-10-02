from sqlalchemy import func, select

from database.db import session
from database.models import Student, Teacher, Group, Grade, Discipline


def task_01():
    print("TASK 01")


def task_02():
    print("TASK 02")


def get_tasks(obj = None):
    if obj is None:
        obj = globals()
    tasks = [
        globals().get(task_str)
        for task_str in filter(lambda x: x.startswith("task_"), obj)
    ]
    return tasks


if __name__ == "__main__":
    # print(globals())
    # print(dir())
    tasks = get_tasks(dir())
    [task() for task in tasks]
    # func = getattr(globals, tasks[0])
    # func = globals().get(tasks[0])
    # func()
