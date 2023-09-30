import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from src.db import session
from src.models import Teacher


from faker import Faker
import random

TOTAL_TEACHERS = 10


def create_Teachers(total: int = TOTAL_TEACHERS):
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
    create_Teachers()
