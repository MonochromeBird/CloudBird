#!/usr/bin/env python
from subprocess import PIPE, Popen, call, check_output
from os import mkdir, remove, getcwd
from os.path import exists, isfile
from appdirs import user_data_dir

tools_path   = '/'.join(__file__.split('/')[:-1:])
programdir = user_data_dir('CloudBird')
try: mkdir(datadir)

def generate(path: str) -> str:
    return check_output(f'{tools_path}/sha256rec {path}', shell = True).decode()

def save(path: str = getcwd()) -> str:
    sum = generate(path)
    with open(datadir+f'currentsum.{path}', 'w') as sumfile:
        sumfile.write(sum)
    return sum

def compare(path: str = getcwd()) -> bool:
    if exists(datadir+f'currentsum.{path}'):
        with open(datadir+f'currentsum.{path}') as sumfile:
            previous_sum =  sumfile.read()
    else: previous_sum = ""

    sum = generate(path)

    if sum != previous_sum:
        with open(datadir+f'currentsum.{path}', 'w') as sumfile:
            sumfile.write(sum)
        return True
    else: False
