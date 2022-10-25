#!/usr/bin/python3

"""7-add_item module"""
from sys import argv
from os.path import exists

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

f = 'add_item.json'

if not exists(f):
    json_list = []
else:
    json_list = load_from_json_file(f)

if len(argv) > 1:
    for i in range(1, len(argv)):
        json_list.append(argv[i])
    save_to_json_file(json_list, f)
