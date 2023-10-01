# import sys
# import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

from seed.teachers import create_teachers
from seed.disciplines import create_disciplines
from seed.groups import create_groups
from seed.students import create_students
from seed.grades import create_gardes

def create_data():
    create_teachers()
    create_disciplines()
    create_groups()
    create_students()
    create_gardes()


if __name__ == "__main__":
    create_data()