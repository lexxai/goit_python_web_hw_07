import argparse
from pathlib import Path


def app_arg():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", help="Directory of images for input", type=Path)


    args = vars(ap.parse_args())
    # print(f"{args=}")
    return args
