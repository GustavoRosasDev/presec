#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.json.handlers.util import load_json
from .cve_identifier import check_vulnerability
from src.etc.imports import tqdm


def get_cve_vulnerability_categories(json_path):

    #  Obter TODOS OS CÓDIGOS da CVE, de todas as categorias:
    json_dict = load_json(json_path)

    # Inicialize uma lista vazia para armazenar todos os valores
    all_cve_categories = []

    # Itere sobre cada chave e adicione os valores à lista
    for valores in json_dict:
        all_cve_categories.append(valores)

    return all_cve_categories


def get_cve_vulnerability_codes_from_json_by_category(json_path, category):
    """
    Retrieves a list of Common Vulnerabilities and Exposures (CVE) codes for a given category from a JSON file.

    Args:
        json_path (str): The path of cve_list.json
        category (str): The category of vulnerabilities to retrieve codes for.

    Returns:
        list: A list of CVE codes belonging to the specified category.
    """
    data = load_json(json_path)

    if category in data:
        return [entry['code'] for entry in data[category]]
    else:
        return []


def get_all_cve_vulnerability_codes(json_path):
    """
    Retrieves all Common Vulnerabilities and Exposures (CVE) codes from a JSON file.

    Returns:
        list: A list of all CVE codes from all categories.
    """
    data = load_json(json_path)

    all_codes = []
    for category in data:
        all_codes.extend([entry['code'] for entry in data[category]])

    return all_codes


def identify_and_execute_correct_cve_function(json_path, target_url, cve_dropdown_value, slider):
    match slider:
        case 1:  # Single
            result = check_vulnerability(target_url, cve_dropdown_value)
            if result:
                print(f'\n🚨 Vulnerability detected!\n{result}')
            else:
                print(f'\n🛡️ This site is protected against: {cve_dropdown_value}')
            return

        case 2:  # List
            code_by_list = get_cve_vulnerability_codes_from_json_by_category(json_path, cve_dropdown_value)

            list_of_vulnerabilities_found = []

            for code in tqdm(code_by_list, desc='Verifying Vulnerabilities', unit=' iterations'):
                result = check_vulnerability(target_url, code)
                if result:
                    list_of_vulnerabilities_found.append(result)

            if list_of_vulnerabilities_found:
                print(f'\n🚨 Vulnerabilities detected!\n{list_of_vulnerabilities_found}')
            else:
                print('\n🛡️ This site is protected. No vulnerabilities from this list were detected!')

            return

        case 3:  # All
            all_codes = get_all_cve_vulnerability_codes(json_path)

            list_of_vulnerabilities_found = []

            for code in tqdm(all_codes, desc='Verifying Vulnerabilities', unit='code'):
                result = check_vulnerability(target_url, code)
                if result:
                    list_of_vulnerabilities_found.append(result)

            if list_of_vulnerabilities_found:
                print(f'\n🚨 Vulnerabilities detected!\n{list_of_vulnerabilities_found}')
            else:
                print(f'\n🛡️ This site is protected. No vulnerabilities out of the {len(all_codes)} were detected on '
                      f'this site!')

            return


# Use to fill description in interface
def get_cve_description_by_cve_code(json_path, cve_code):
    data = load_json(json_path)

    for categoria, itens in data.items():
        for item in itens:
            if item["code"] == cve_code:
                return item["description"]

    return "Código CVE não encontrado."
