#!/usr/bin/python3
"""
Script to add command line arguments to a Python list and save them to a file.
"""


import sys

if __name__ == "__main__":
    # Import necessary functions from previous tasks
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_module = __import__('6-load_from_json_file')
    load_from_json_file = load_module.load_from_json_file

    try:
        # Try to load items from the "add_item.json" file
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        existing_items = []

    # Extend the list with command line arguments (excluding the script name)
    new_items = sys.argv[1:]
    updated_items = existing_items + new_items

    # Save the updated list back to the "add_item.json" file
    save_to_json_file(
        updated_items,
        "add_item.json"
    )
