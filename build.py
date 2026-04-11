''' A shortcut for building the app '''
import os
import shutil


# split into lines for readability
BUILD_GUI_CMD = """py -m nuitka --mode=standalone
               --main=gui.py
               --include-data-dir=./src=src 
               --include-data-dir=./uix=uix 
               --include-data-files=./vadimsclicker.kv=vadimsclicker.kv
               --output-dir=./dist
               --windows-console-mode=disable 
               --windows-icon-from-ico=./design/logo.png
"""

BUILD_TUI_CMD = """py -m nuitka --mode=standalone
               --main=tui.py
               --include-data-files=./src/ascii.txt=src/ascii 
               --output-dir=./dist
               --windows-console-mode=force
               --windows-icon-from-ico=./design/logo.png
"""


def exc(cmd):
    '''
    Crossplatform multiline command execution.
    
    Compiles a multiline command into one line and executes it.
    '''
    return os.system(' '.join(cmd.split()))


def build():
    ''' Execute the command for building the app '''
    print('------------ building GUI ------------')
    exc(BUILD_GUI_CMD)
    print('------------ GUI done ------------')
    print('------------ building TUI ------------')
    exc(BUILD_TUI_CMD)
    print('------------ TUI done ------------')
    print('------------ compiling dist ------------')
    if 'vadim-clicker.dist' in os.listdir('./dist'):
        shutil.rmtree('./dist/vadim-clicker.dist')
    os.replace('./dist/gui.dist', './dist/vadim-clicker.dist')
    os.replace('./dist/tui.dist/tui.exe', './dist/vadim-clicker.dist/tui.exe')
    print('------------ dist done ------------')
    

if __name__ == "__main__":
    build()
