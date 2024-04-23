#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

# 📱 App Configurations
# noinspection PyUnresolvedReferences
from src.app.info import *
# noinspection PyUnresolvedReferences
from src.app.settings import *

# 🚀 Initial setup
# noinspection PyUnresolvedReferences
from src.etc.fonts import *
# noinspection PyUnresolvedReferences
from src.etc.imports import *
# noinspection PyUnresolvedReferences
from src.etc.variables import *
# noinspection PyUnresolvedReferences
from src.etc.color_palette import *

# 🔧 Custom application functions
# noinspection PyUnresolvedReferences
from src.functions.menu.command_line import run
# noinspection PyUnresolvedReferences
from src.functions.contact import open_profile
# noinspection PyUnresolvedReferences
from src.functions.checker import (check_python_version,
                                   operational_system,
                                   user_type,
                                   check_list_of_command_names,
                                   check_list_of_command_line_and_description,
                                   command_line_interface)
# noinspection PyUnresolvedReferences
from src.functions.system.host import get_ipv4

# 📦 JSON
# noinspection PyUnresolvedReferences
from src.json.handlers.update_commands import (add_command,
                                               update_command,
                                               delete_command)

# UTIL
# noinspection PyUnresolvedReferences
from src.json.handlers.util import load_json, save_json

# CVE Groups
# noinspection PyUnresolvedReferences
from src.functions.menu.cve.cve_handler import (identify_and_execute_correct_cve_function,
                                                get_cve_vulnerability_codes_from_json_by_category,
                                                get_cve_vulnerability_categories,
                                                get_all_cve_vulnerability_codes,
                                                get_cve_description_by_cve_code)
# noinspection PyUnresolvedReferences
from src.functions.menu.cve.cve_modifiers import (create_new_cve_category,
                                                  create_new_cve_code_and_description,
                                                  update_cve_description_by_code,
                                                  delete_cve_record_by_code,
                                                  delete_cve_category)

# 🧰 Tools
# noinspection PyUnresolvedReferences
from src.functions.menu.port_scan import port_scan
# noinspection PyUnresolvedReferences
