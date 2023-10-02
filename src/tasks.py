from sqlalchemy import func, select

from database.db import session
from database.models import Student, Teacher, Group, Grade, Discipline


def task_01():
    r = session.query()


def task_02():
    r = session.query()


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
    # tasks = get_tasks(dir())
    # [task() for task in tasks]
    # func = getattr(globals, tasks[0])
    # func = globals().get(tasks[0])
    # func()
    for task in get_tasks():
        print("-"*80)
        print(task.__name__)
        result = task()
        print(f"result = {result}")
        


