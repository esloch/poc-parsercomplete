# Parser Auto Complete

Parser Auto Complete is a tool that reads targets from YAML files and provides auto-completion for the selected targets on the command line.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/parser-auto-complete.git`
2. Navigate to the project directory: `cd parser-auto-complete`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage

1. Run the parser: `./app/parser_auto_complete.py --group <group_name> --targets <target_name>`
   - The `--group` option is used to specify the group. Auto-completion will provide a list of available groups.
   - The `--targets` option is used to specify the target. Auto-completion will provide a list of available targets based on the selected group.

## Configuration

1. Create YAML files for defining your targets. For example, create a file named `targets.yaml`.
2. Define your targets and groups in the YAML file using the following format:

   ```yaml
   <group_name>:
     targets:
       <target_name_1>:
         ...
       <target_name_2>:
         ...

![Screenshot_20230607_145924](https://github.com/esloch/poc-parsercomplete/assets/3450741/6cbc27a1-4729-4059-9030-42e65f03d081)
