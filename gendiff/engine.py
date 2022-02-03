import json
import yaml


_rem = '- '
_add = '+ '
_equal = '  '


def generate_diff(old_file: dict, new_file: dict) -> str:
    diff = []

    def compare_old_values():
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

    compare_old_values()
    for key, value in new_file.items():
        diff.append((_add + str(key), value))
    diff.sort(key=lambda x: x[0][2:])
    diff_dict = {key: value for key, value in diff}
    return json.dumps(diff_dict, indent=2).replace('"', '').replace(',', '')


def files_to_data(file_one, file_two):
    with open(file_one) as f1, open(file_two) as f2:
        return yaml.safe_load(f1), yaml.safe_load(f2)
        # return json.load(f1), json.load(f2)
