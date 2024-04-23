#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

# region Text of Titles
# (Name Variations)
configure_tab_choose_an_item_english_options = ['Command-Line', 'CVE Vulnerability']
configure_tab_choose_an_item_portuguese_options = ['Linha de Comando', 'Vulnerabilidade CVE']
configure_tab_choose_an_item_spanish_options = ['Línea de Comando', 'Vulnerabilidad CVE']

command_line_name_variations = ['Command-Line', 'Linha de Comando', 'Línea de Comando']
cve_vulnerabilities_name_variations = ['CVE Vulnerability', 'Vulnerabilidade CVE', 'Vulnerabilidad CVE']
# endregion

# region Dropdown Values
# (Options)
appearance_mode_english_options = ["Dark", "Light"]
appearance_mode_portuguese_options = ["Escuro", "Claro"]
appearance_mode_spanish_options = ["Oscuro", "Claro"]

language_options = ['en', 'pt', 'es']

command_line_category_english_options = ['basic', 'advanced']
command_line_category_portuguese_options = ['básico', 'avançado']
command_line_category_spanish_options = ['básico', 'avanzado']

operation_type_english_options = ['Create', 'Update', 'Delete']
operation_type_portuguese_options = ['Criar', 'Atualizar', 'Excluir']
operation_type_spanish_options = ['Crear', 'Actualizar', 'Borrar']

cve_type_english_options = ['CVE Code', 'List']
cve_type_portuguese_options = ['Código CVE', 'Lista']

user_type_on_windows_options = ['user', 'admin']
user_type_on_linux_options = ['usr', 'root']

operational_system_options = ['Windows', 'Linux']

# (Name Variations)
dark_name_variations = ['Dark', 'Escuro', 'Oscuro']
light_name_variations = ['Light', 'Claro']

basic_name_variations = ['basic', 'básico']
advanced_name_variations = ['advanced', 'avançado', 'avanzado']

create_name_variations = ['Create', 'Criar', 'Crear']
update_name_variations = ['Update', 'Atualizar', 'Actualizar']
delete_name_variations = ['Delete', 'Excluir', 'Borrar']

cve_code_name_variations = ['CVE Code', 'Código CVE']
# endregion

# region Slider Values
# (Name Variations)
single_name_variations = ['SINGLE', 'ÚNICO']
list_name_variations = ['LIST', 'LISTA']
all_name_variations = ['ALL', 'TODOS']
# endregion

# region Switch Values
mapping_switch_values = {
        1: ['SINGLE', 'ÚNICO'],
        2: ['LIST', 'LISTA'],
        3: ['ALL', 'TODOS']
    }
# endregion

# Specifies the function to be triggered on program startup. Options: "first", "second", "third".
home_tab_active_container = "first"
configure_tab_active_container = "first"

cve_json_path = 'src/json/cve_list.json'
