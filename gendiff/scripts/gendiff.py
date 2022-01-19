#!/usr/bin/env python3
import argparse


def main():
    return parser.parse_args()


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

if __name__ == '__main__':
    args = main()