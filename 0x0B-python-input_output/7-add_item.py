#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file.
"""


import sys
from os.path import exists
from json import dump, load

filename = "add_item.json"

if exists(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        my_list = load(file)
else:
    my_list = []

my_list.extend(sys.argv[1:])

with open(filename, mode='w', encoding='utf-8') as file:
    dump(my_list, file)
