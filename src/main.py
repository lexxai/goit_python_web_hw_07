from parse_args import app_arg
from seed.seed import create_data
import logging


logger = logging.getLogger()

if __name__ == "__main__":
    args = app_arg()
    create_data()
