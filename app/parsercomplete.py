#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import argcomplete
import os
from pathlib import Path
from typing import Any, Dict, List
import yaml

root_path = Path(os.path.dirname(os.path.abspath(__file__)))


class MaKim:
    global_data: Dict[str, Any]
    target_commands: Dict[str, Any]

    def get_target_commands(self, target_file: str, target_scope: str, target_name: str) -> List[str]:
        """
        Get the list of target commands from the specified target file and target name.

        Args:
            target_file: Path to the target file.
            target_name: Name of the target.

        Returns:
            List of target commands.
        """
        with open(target_file, 'r') as file:
            self.target_commands = yaml.safe_load(file)
            k_commands = self.target_commands[target_name]
            return list(k_commands[target_scope].get('targets').keys())

    def get_group(self) -> List[str]:
        """
        Get the list of available groups.

        Returns:
            List of groups.
        """
        return ["default", "upstream"]


def targets_list(**kwargs) -> List[str]:
    """
    Get the list of available targets.

    Returns:
        List of targets.
    """
    mkm_obj = MaKim()

    available_targets = []
    for file in os.listdir(root_path):
        if file.endswith('.yaml'):
            fname = os.path.join(root_path, file)
            target_scope = 'upstream'
            available_targets.extend(mkm_obj.get_target_commands(fname, target_scope, 'groups'))
    print(available_targets)

    return available_targets


def targets_group(**kwargs) -> List[str]:
    """
    Get the list of available groups.

    Returns:
        List of groups.
    """
    mkm_obj = MaKim()

    return mkm_obj.get_group()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", help="Group list").completer = targets_group
    parser.add_argument("--targets", help="Targets list").completer = targets_list

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
