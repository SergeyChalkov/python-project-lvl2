#!/usr/bin/env python3
import gendiff.engine as engine
from file_parser import parse_files

def main():
    print(engine.generate_diff(parse_files()))


if __name__ == '__main__':
    main()
