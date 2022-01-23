#!/usr/bin/env python3
import argparse
import gendiff.engine as engine


def main():
    args = parser.parse_args()
    old, new = engine.files_to_data(args.first_file, args.second_file)
    print(engine.generate_diff(old, new))


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

if __name__ == '__main__':
    main()
