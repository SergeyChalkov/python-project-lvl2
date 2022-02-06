#!/usr/bin/env python3
import gendiff.engine as engine
from gendiff.file_parser import parse_files


def main():
    old, new = parse_files()
    print(engine.generate_diff(old, new))


if __name__ == '__main__':
    main()
