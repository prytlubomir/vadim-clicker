''' A shortcut for building the app '''
import os


BUILD_CMD = "py -m nuitka main.py --mode=onefile --include-data-files=./src/ascii.txt=src/ascii.txt"


def build():
    ''' Execute the command for building the app '''
    os.system(BUILD_CMD)


if __name__ == "__main__":
    build()
