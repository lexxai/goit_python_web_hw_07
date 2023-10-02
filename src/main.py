import logging
from parse_args import app_arg

from seed.seed import create_data
import tasks


package_name="hw"
logger = logging.getLogger(package_name)

if __name__ == "__main__":
    # logging.basicConfig()
    # logger.setLevel(logging.INFO)
    args = app_arg()
    # create_data()

    # do tasks  
    for task in tasks.get_tasks():
        print("-" * 80)
        print(task.__name__)
        task_result = task()
        if task_result:
            column_names = task_result.get("column_names")
            print(".   " * 20)
            for id, row in enumerate(task_result.get("result")):
                row_str = []
                for i, col in enumerate(row):
                    row_str.append(f'{column_names[i]}: "{col}"')
                result = ", ".join(row_str)
                print(f"[{id+1:2}] {result}")