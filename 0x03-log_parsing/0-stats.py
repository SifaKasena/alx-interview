#!/usr/bin/python3
import sys
import re


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

line_count = 0
pattern = re.compile(
    r'^\S+\s*-\s*\[\S+ \S+\] "GET /projects/260 HTTP/1.1" '
    r'(\S+) (\d+)$'
)

try:
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)
