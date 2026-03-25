''' A shortcut for building the app '''
import os


# split into lines for readability
BUILD_CMD = """py -m nuitka main.py --mode=standalone 
               --include-data-dir=./src=src 
               --include-data-dir=./uix=uix 
               --include-data-files=./vadimsclicker.kv=vadimsclicker.kv
"""
BUILD_CMD = ' '.join(BUILD_CMD.split()) # joined into a sigle line for cross platform support


def build():
    ''' Execute the command for building the app '''
    os.system(BUILD_CMD)


if __name__ == "__main__":
    build()
