import logging

from sqlalchemy import func, select, label, desc

from database.db import session
from database.models import Student, Teacher, Group, Grade, Discipline

package_name="hw"
logger = logging.getLogger(package_name)


def get_tasks(obj=None):
    if obj is None:
        obj = globals()
    tasks = [
        globals().get(task_str)
        for task_str in filter(lambda x: x.startswith("task_"), obj)
    ]
    return tasks


def get_query_dict(query):
    return {"column_names": query.statement.columns.keys(), "result": query.all()}


def task_01(*args, **kwargs):
    """
    SELECT s.fullname as student, ROUND(AVG(grade),2) as average_grade
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5
    """
    query = (
        session.query(
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("Average grade"))
        .limit(5)
    )
    return get_query_dict(query)


def task_02(*args, **kwargs):
    """
    SELECT d.name AS discipline, s.fullname as student, ROUND(AVG(grade),2) as average_garde
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id 
    LEFT JOIN disciplines d ON g.disciplines_id = d.id 
    WHERE g.disciplines_id = 2
    GROUP BY s.id
    ORDER BY average_garde DESC
    LIMIT 1
    """
    discipline_id = kwargs.get("discipline_id", 419)
    print(f"{discipline_id=}")
    query = (
        session.query(
            label("Discipline",Discipline.name),
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name)
        .order_by(desc("Average grade"))
        .limit(1)
    )
    return get_query_dict(query)


if __name__ == "__main__":
    # print(globals())
    # print(dir())
    # tasks = get_tasks(dir())
    # [task() for task in tasks]
    # func = getattr(globals, tasks[0])
    # func = globals().get(tasks[0])
    # func()
    for task in get_tasks():
        print("-" * 80)
        print(task.__name__)
        task_result = task()
        if task_result:
            column_names = task_result.get("column_names")
            print(".   " * 20)
            for row in enumerate(task_result.get("result")):
                row_str = []
                for i, col in enumerate(row[1]):
                    row_str.append(f"{column_names[i]}: {col}")
                result = ", ".join(row_str)
                print(result)
