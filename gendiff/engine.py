import json


_rem = '- '
_add = '+ '
_equal = '  '


def generate_diff(old_file: dict, new_file: dict) -> str:
    diff = []
    for key, value in old_file.items():
        new_value = new_file.pop(key, None)
        if new_value:
            if new_value == value:
                diff.append((_equal + str(key), value))
            else:
                diff.extend(
                    [(_rem + str(key), value), (_add + str(key), new_value)]
                )
        else:
            diff.append((_rem + str(key), value))
    for key, value in new_file.items():
        diff.append((_add + str(key), value))
    diff.sort(key=lambda x: x[0][2:])
    diff_dict = {key: value for key, value in diff}
    return json.dumps(diff_dict, indent=2).replace('"', '')


def files_to_data(file_one, file_two):
    with open(file_one) as f1, open(file_two) as f2:
        old_file = json.load(f1)
        new_file = json.load(f2)
    return old_file, new_file