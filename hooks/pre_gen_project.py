import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.app_name }}"

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: %s app_name must follow the convention of Python module names!" % module_name)
    sys.exit(1)
