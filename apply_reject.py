#!/usr/bin/env python3

import argparse
import json

def main(source, target, jsonf):
    rejected = json.loads(jsonf.read())
    flat_rej = []

    for lang in rejected.keys():
        flat_rej += rejected[lang]

    for line in source:
        try:
            if flat_rej.index(line.strip()) >= 0:
                pass
        except ValueError:
            target.write(line)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Read a JSON file produced by check_lang.py and change source text file')
    PARSER.add_argument('--source-file',
                        required=True,
                        type=argparse.FileType('r'),
                        help='Text file to read')
    PARSER.add_argument('--target-file',
                        required=True,
                        type=argparse.FileType('w'),
                        help='Text file to produce')
    PARSER.add_argument('--reject-file',
                        required=True,
                        type=argparse.FileType('r'),
                        help='JSON file to apply')
    PARAMS = PARSER.parse_args()

    main(source=PARAMS.source_file, target=PARAMS.target_file, jsonf=PARAMS.reject_file)
