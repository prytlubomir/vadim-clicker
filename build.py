''' A shortcut for building the app '''
import os


# split into lines for readability
BUILD_CMD = """py -m nuitka main.py --mode=standalone 
               --include-data-dir=./src=src 
               --include-data-dir=./uix=uix 
               --include-data-files=./vadimsclicker.kv=vadimsclicker.kv
"""
BUILD_CMD = ' '.join(BUILD_CMD.split()) # joined into a sigle line for cross platform support

def scan_dir(path):
    lst = os.listdir(path)
    visible = list(filter(lambda x: x[0] is not '.', lst))
    dirs = list(filter(lambda x: os.path.isdir(f'{path}/{x}'), visible))
    files = list(filter(lambda x: os.path.isfile(f'{path}/{x}'), visible))
    kvs = list(filter(lambda f: '.kv' in f, files))
    
    for dir in dirs:
        dc = scan_dir(os.path.join(path, dir))
        kvs += list(map(lambda f: dir+'/'+f, dc))

    return kvs


def generate_args(kvs):
    gcmd = lambda p: f"--include-data-files=./{p}={p}"
    cmds = [gcmd(f'uix/{kv}') for kv in kvs]
    return cmds


def build():
    ''' Execute the command for building the app '''
    kvs = scan_dir('uix')
    cmd = BUILD_CMD+' '+' '.join(generate_args(kvs))
    os.system(BUILD_CMD)


if __name__ == "__main__":
    build()
