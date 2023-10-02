import logging
from parse_args import app_arg

from seed.seed import create_data
import tasks


package_name="hw"
logger = logging.getLogger(package_name)

if __name__ == "__main__":
    logging.basicConfig()
    logger.setLevel(logging.INFO)
    args = app_arg()
    # create_data()

    # do tasks  
    for task in tasks.get_tasks():
        print("-"*80)
        print(task.__name__)
        result = task()
        print(f"result = {result}")
