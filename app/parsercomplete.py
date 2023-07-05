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
            target_scope: Scope of the target.
            target_name: Name of the target.

        Returns:
            List of target commands.
        """
        with open(target_file, 'r') as file:
            self.target_commands = yaml.safe_load(file)
            k_commands = self.target_commands[target_name]
            if target_scope == 'all':
                return k_commands
            return list(k_commands[target_scope].get('targets').keys())

    def get_available_items(self, target_scope: str, target_name: str) -> List[str]:
        """
        Get the list of available items (targets or groups).

        Args:
            target_scope: Scope of the target.
            target_name: Name of the target.

        Returns:
            List of available items.
        """
        available_items = []
        for file in os.listdir(root_path):
            if file.endswith('.yaml'):
                fname = os.path.join(root_path, file)
                target_commands = self.get_target_commands(fname, target_scope, target_name)
                available_items.extend(target_commands)
        return available_items

    def get_available_targets(self, prefix: str, parsed_args: argparse.Namespace, **kwargs) -> List[str]:
        """
        Get the list of available targets.

        Args:
            prefix: Current completion prefix.
            parsed_args: Parsed arguments.

        Returns:
            List of targets.
        """
        selected_group = parsed_args.group
        return [t for t in self.get_available_items(selected_group, 'groups') if t.startswith(prefix)]

    def get_available_groups(self, **kwargs) -> List[str]:
        """
        Get the list of available groups.

        Returns:
            List of groups.
        """
        return self.get_available_items('all', 'groups')

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--group", help="Group list").completer = self.get_available_groups
        parser.add_argument("--targets", help="Targets list").completer = self.get_available_targets

        argcomplete.autocomplete(parser)
        args = parser.parse_args()

        return args.group, args.targets


if __name__ == '__main__':
    mkm_obj = MaKim()
    mkm_obj.main()
