import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from database.db import session
from database.models import Teacher


from faker import Faker
import random

TOTAL_TEACHERS = 10

def erase_teachers():
    deleted_teachers = session.query(Teacher).delete()
    print(f"{deleted_teachers=}")


def create_teachers(total: int = TOTAL_TEACHERS):
    erase_teachers()
    fake: Faker = Faker("uk-UA")
    for _ in range(total):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        session.add(teacher)
    session.commit()


if __name__ == "__main__":
    create_teachers()
