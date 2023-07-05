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

    def targets_list(self, prefix: str, parsed_args, **kwargs) -> List[str]:
        """
        Get the list of available targets.

        Args:
            prefix: Current completion prefix.
            parsed_args: Parsed arguments.

        Returns:
            List of targets.
        """
        selected_group = parsed_args.group

        available_targets = []
        for file in os.listdir(root_path):
            if file.endswith('.yaml'):
                fname = os.path.join(root_path, file)
                available_targets.extend(self.get_target_commands(fname, selected_group, "groups"))
        return [t for t in available_targets if t.startswith(prefix)]

    def targets_group(self, **kwargs) -> List[str]:
        """
        Get the list of available groups.

        Returns:
            List of groups.
        """
        return self.get_group()

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--group", help="Group list").completer = self.targets_group
        parser.add_argument("--targets", help="Targets list").completer = self.targets_list

        argcomplete.autocomplete(parser)
        args = parser.parse_args()

        return args.group, args.targets

if __name__ == '__main__':
    mkm_obj = MaKim()
    mkm_obj.main()
