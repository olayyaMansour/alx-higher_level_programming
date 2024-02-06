#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics based on log entries.
"""

import sys


def print_metrics(total_size, status_codes):
    """
    Prints the computed metrics.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes):
        print("{:d}: {:d}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parses a log entry line and returns a tuple of status code and file size.
    """
    parts = line.split()
    return int(parts[-2]), int(parts[-1])
