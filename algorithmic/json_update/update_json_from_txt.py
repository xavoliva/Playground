import json
from collections.abc import Mapping


CONFIG_FILE = "config_file.json"
CHANGES_FILE = "changes.txt"


'''
Function that modifies values in the configuration file
on position specified by (.txt) file containing changes.
First parameter: configuration file
Second parameter: txt file containing list of changes to be applied
The resulting json is written into json file called updated_config_file.json
'''


def update_json_file(configFile, changesFile):

    changes_dict = changes_parser(changesFile)

    with open(configFile, "r") as read_config_file:
        config_data = json.load(read_config_file)

    update_dict_iteration(config_data, changes_dict)

    with open("updated_config_file.json", "w") as outfile:
        json.dump(config_data, outfile, indent=" " * 3)

    return 1


# Function allowing to put changes of txt file into a dictionary

def changes_parser(changesFile):
    with open(changesFile, "r") as read_changes_file:
        content = read_changes_file.readlines()

    content = [x.strip() for x in content]

    final_dict = {}
    for line in content:
        temp_dict = current = {}
        left, right = line.split(": ", 1)
        left_list = left.replace("\"", "").split(".")
        for element in left_list[:-1]:
            current[element] = {}
            current = current[element]

        current[left_list[-1]] = json.loads(right)
        current = current[left_list[-1]]

        update_dict_iteration(final_dict, temp_dict)

    return final_dict


def update_dict_iteration(old_dict, changes):
    stack = [(old_dict, changes)]

    while stack:
        old_dict, changes = stack.pop()
        for x, y in changes.items():
            if isinstance(y, Mapping):
                temp_dict = old_dict.setdefault(x, {})

                if isinstance(temp_dict, Mapping):
                    stack.append((temp_dict, y))

                else:
                    old_dict[x] = y

            else:
                old_dict[x] = y


def update_dict_recursive(old_dict, changes):
    for x, y in changes.items():
        if isinstance(y, Mapping):
            old_dict[x] = update_dict_recursive(old_dict.get(x, {}), y)
        else:
            old_dict[x] = y

    return old_dict


if __name__ == "__main__":
    update_json_file(CONFIG_FILE, CHANGES_FILE)
