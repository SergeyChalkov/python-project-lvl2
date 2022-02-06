import argparse
import json
import yaml
from pathlib import Path


def _files_to_data(first_file, second_file):
    decoders = {'.j': json.load, '.y': yaml.safe_load}
    first_file_decoder = decoders[first_file.suffix[:2]]
    second_file_decoder = decoders[second_file.suffix[:2]]
    with first_file.open('r') as file1, second_file.open('r') as file2:
        return first_file_decoder(file1), second_file_decoder(file2)


def parse_files():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return _files_to_data(Path(args.first_file), Path(args.second_file))
