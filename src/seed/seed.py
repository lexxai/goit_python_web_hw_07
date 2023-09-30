from seed.teachers import create_teachers
from seed.groups import create_groups
from seed.students import create_students

def create_data():
    create_teachers()
    create_groups()
    create_students()