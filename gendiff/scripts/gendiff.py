#!/usr/bin/env python3
import argparse
import json


def new_d(a: dict, b: dict):
    new = []
    minus = '- '
    plus = '+ '
    equal = '  '
    for key, value in a.items():
        b_value = b.pop(key, None)
        if b_value:
            if b_value == value:
                new.append((equal + str(key), value))
            else:
                new.extend(
                    [(minus + str(key), value), (plus + str(key), b_value)]
                )
        else:
            new.append((minus + str(key), value))
    for key, value in b.items():
        new.append((plus + str(key), value))
    new.sort(key=lambda x: x[0][2:])
    return {key: value for key, value in new}


def main():
    args = parser.parse_args()
    with open(args.first_file) as old, open(args.second_file) as new:
        diff = new_d(json.load(old), json.load(new))
    print(json.dumps(diff, indent=2).replace('"', ''))


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

if __name__ == '__main__':
    main()
