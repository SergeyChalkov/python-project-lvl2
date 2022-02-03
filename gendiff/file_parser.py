import argparse
import json
import yaml


def _files_to_data(file_one, file_two, format):
    with open(file_one) as f1, open(file_two) as f2:
        return yaml.safe_load(f1), yaml.safe_load(f2)
        # return json.load(f1), json.load(f2)


def parse_files():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return _files_to_data(args.first_file, args.second_file)