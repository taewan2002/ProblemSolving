#!/usr/bin/env python3

## Basic things
import glob, sys, os, pathlib, shutil
debug_mode, run_after, skip_ex = False, False, False
src_path, is_dir = None, False

## Functions
def usage(exit_code):
    if exit_code == 1:
        scprint('invalid usage.')
    print('usage: sc [options] c_source_files..')
    print('       sc [options] c_source_directory')
    print('       sc [--help/-h]\n')
    print('options:')
    print('   --debug/-d                Include source code to output file.')
    print('   --run-after-compile/-r    Run output executable after successful build.')
    print('   --skip-filetype-check/-s  Try compiling non C/C++ source files too.')
    exit(exit_code)

def scprint(text):
    print('simplec: ' + str(text))
def scexit(code=None):
    if not code or code == 0:
        exit(0)
    else:
        scprint(code)
        exit(1)

def exec(cmd, printcmd=True, exitiferr=True):
    if printcmd:
        print(cmd)
    if os.system(cmd) != 0 and exitiferr:
        scexit('error detected.')

def mktmpdir():
    rmtmpdir()
    os.mkdir('obj')
def rmtmpdir():
    if pathlib.Path('obj').is_dir():
        shutil.rmtree('obj')

def mkrundir():
    if not os.path.exists('pwd'):
        scprint('pwd directory does not exist, making one.')
        os.mkdir('pwd')

def isfile(path):
    return pathlib.Path(path).is_file()
def isdir(path):
    return pathlib.Path(path).is_dir()
def endswithc(name):
    return name.endswith('.c') or name.endswith('.cpp')
def alertnoncfile(name):
    scprint('%s is not a C/C++ source file, ignoring.' % filebasename(name))

def filebasename(name):
    return os.path.basename(pathlib.Path(name).absolute())

def readdir(path):
    result = []
    for file in glob.glob(path+'/**/*', recursive=True):
        if (file.endswith('.c') or file.endswith('.cpp')) or skip_ex:
            result.append(file)
        else:
            alertnoncfile(file)
    return result

def buildobj(path):
    basename = os.path.basename(path)
    debugstr = '-g' if debug_mode else ''
    exec('gcc %s -c -o \"./obj/%s.o\" \"%s\"' % (debugstr, basename, path))
def linkobj(output):
    exec('gcc -o \"%s\" ./obj/*' % output)

def addfiletolist(path, lst):
    if endswithc(path) or skip_ex:
        lst.append(path)
    else:
        alertnoncfile(path)

## Start point
# Read args
args = sys.argv
if len(args) == 1:
    usage(0)

file_args, opt_args = [], []
for idx in range(len(args)):
    if idx == 0:
        continue
    arg = args[idx]
    if arg[0] == '-':
        opt_args.append(arg)
    else:
        file_args.append(arg)

for arg in opt_args:
    opt = arg.lower()
    if arg[0:2] == '--':
            if opt == '--debug':
                opt = '-d'
            elif opt == '--run-after-compile':
                opt = '-r'
            elif opt == '--skip-filetype-check':
                opt = '-s'
            elif opt == '--help':
                opt = '-h'
            else:
                opt = '-%'
            opt.replace('-', '')

    opt = opt[1:]
    for optc in opt:
        if optc == 'd':
            debug_mode = True
        elif optc == 'r':
            run_after = True
        elif optc == 's':
            skip_ex = True
        elif optc == 'h':
            usage(0)
        else:
            usage(1)

for arg in file_args:
    if not src_path:
        if isfile(arg):
            is_dir = False
            src_path = []
            addfiletolist(arg, src_path)
        elif isdir(arg):
            is_dir = True
            src_path = readdir(arg) 
            if len(src_path) == 0:
                scexit('no files detected in %s.' % filebasename(arg))
        else:
            scexit('no such file or directory.')
    elif not is_dir:
        if isfile(arg):
            addfiletolist(arg, src_path)
        elif isdir(arg):
            usage(1)
        else:
            scexit('no such file or directory.')
    else:
        usage(1)

# Validation
if src_path == None:
    scexit('no source files given.')

# Build 
mktmpdir()

filecnt = len(src_path)
if filecnt == 0:
    scexit('no files detected.')
elif is_dir:
    scprint('compiling %d file%s in one directory' % (filecnt, 's' if filecnt != 1 else ''))
else:
    scprint('compiling %d separate file%s' % (filecnt, 's' if filecnt != 1 else ''))
for sc in src_path:
    buildobj(sc)
linkobj('output.bin')

# Check and exit
if not debug_mode:
    rmtmpdir()
if run_after:
    scprint('Executing..')
    mkrundir()
    print('\033[0;32m[Program started]\033[0;0m')
    result = os.system('cd ./pwd; ../output.bin')
    print('\033[0;%dm[Program terminated]\033[0;0m' % (32 if result == 0 else 31))
scexit(0)
