import os
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m" # To change the terminal color
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if not re.match(MODULE_REGEX, project_slug):
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")