#!/usr/bin/env python3

import sys
import argparse
import guess_language
import json

def main(lang, hints, file, debug):
    rejected = {}
    count = 0

    for line in file:
        line = line.strip()
        guessed_lang = guess_language.guess_language(text=line, hints=hints)
        if guessed_lang != lang:
            if not guessed_lang in rejected.keys():
                rejected[guessed_lang] = []
            rejected[guessed_lang].append(line)

            if debug:
                print('reject', guessed_lang, line)

        count += 1

        if not debug:
            sys.stderr.write('Treated: ' + str(count) + '\r')

    sys.stdout.write(json.dumps(rejected))

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Checking per-line language of a text file')
    PARSER.add_argument('--lang',
                        required=True,
                        type=str,
                        help='Language code supported by guess_language-spirit')
    PARSER.add_argument('--hints',
                        default='',
                        required=False,
                        type=str,
                        help='Comma-separated language codes hints')
    PARSER.add_argument('--file',
                        required=True,
                        type=argparse.FileType('r'),
                        help='Text file to check')
    PARSER.add_argument('--debug',
                        default=False,
                        required=False,
                        type=bool,
                        help='Show progress per line, instead of global ')
    PARAMS = PARSER.parse_args()

    main(lang=PARAMS.lang, hints=PARAMS.hints.split(','), file=PARAMS.file, debug=PARAMS.debug)
