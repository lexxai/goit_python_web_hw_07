import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from database.db import session
from database.models import Student


from faker import Faker
import random

TOTAL_students = 100

def erase_students():
    deleted_students = session.query(Student).delete()
    print(f"{deleted_students=}")


def create_students(total: int = TOTAL_students):
    erase_students()
    fake: Faker = Faker("uk-UA")
    for _ in range(total):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        session.add(student)
    session.commit()

if __name__ == "__main__":
    create_students()
