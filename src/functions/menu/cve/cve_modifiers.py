#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.json.handlers.util import load_json, save_json


# (CREATE)
def create_new_cve_category(path, category):
    """
        Creates a new category in the specified JSON file.

        Parameters:
        - path (str): The path of the JSON file.
        - category (str): The category to be created.

        Returns:
        None

        Example of use:
            if __name__ == "__main__":
                # Exemplo de uso:
                json_path = '../../../json/cve_list.json'
                chosen_list = "New List"

                create_new_category(json_path, chosen_list)
    """
    data = load_json(path)

    if category not in data:
        data[category] = []

    save_json(path, data)
    print(f'✅ CVE Category "{category}" was created!')


def create_new_cve_code_and_description(path, category, code, description):
    """
        Adds a new record to the specified JSON file.

        Parameters:
        - path (str): The path of the JSON file.
        - category (str): The category to which the record will be added.
        - code (str): The code of the record.
        - description (str): The description associated with the code.

        Returns:
        None

        Example of use:
            if __name__ == "__main__":
                json_path = '../../../json/cve_list.json'
                chosen_category = "New List"
                chosen_code = "CVE-2023-12345"
                chosen_description = "Nova vulnerabilidade descoberta."

                create_new_cve_code_and_description(json_path, chosen_category, chosen_code, chosen_description)
    """
    data = load_json(path)

    new_registry = {
        "code": code,
        "description": description
    }

    if category not in data:
        data[category] = []

    data[category].append(new_registry)

    save_json(path, data)
    print(f'✅ CVE Vulnerability "{code}" was created with this description "{description}"!')


# (UPDATE)
def update_cve_description_by_code(path, code, nova_descricao):
    """
        Modifies the description of a record based on the CVE code and category.

        Parameters:
        - path (str): The path of the JSON file.
        - category (str): The category of the record.
        - code (str): The code of the record to be modified.
        - new_description (str): The new description to be assigned to the record.

        Returns:
        None

        Example of use:
            if __name__ == "__main__":
                json_path = '../../../json/cve_list.json'
                chosen_category = "New List"
                chosen_code = "CVE-2023-12345"
                new_description = "New description for the discovered vulnerability."

                change_cve_description_by_code(json_path, chosen_category, chosen_code, new_description)
    """
    data = load_json(path)

    for category, entries in data.items():
        for entry in entries:
            if entry['code'] == code:
                entry['description'] = nova_descricao
                break

        save_json(path, data)
        print(f'✅ Description of CVE Vulnerability "{code}" was updated!')
    else:
        print(f"❌ No CVE record with code {code} was found.")


# (DELETE)
def delete_cve_record_by_code(path, code):
    """
    Deletes a record based on the CVE code.

     Parameters:
     - path (str): The path of the JSON file.
     - code (str): The code of the record to be deleted.

    Returns:
    None

    Example of use:
        if __name__ == "__main__":
            json_path = '../../../json/cve_list.json'
            chosen_code_to_delete = "CVE-2023-12345"

            delete_cve_record_by_code(json_path, chosen_code_to_delete)
    """
    data = load_json(path)

    record_found = False

    for category, entries in data.items():
        if any(entry['code'] == code for entry in entries):
            data[category] = [entry for entry in entries if entry['code'] != code]
            record_found = True
            break

    if record_found:
        save_json(path, data)
        print(f'✅ CVE Vulnerability "{code}" was deleted!')
    else:
        print(f'❌ CVE Vulnerability "{code}" not found in any category.')


def delete_cve_category(path, category):
    """
    Deletes an entire category and its records.

     Parameters:
     - path (str): The path of the JSON file.
     - category (str): The category to delete.

    Returns:
    None

    Example of use:
        if __name__ == "__main__":
            json_path = '../../../json/cve_list.json'
            chosen_category_to_delete = "New List"

            delete_cve_category(json_path, chosen_category_to_delete)
    """
    data = load_json(path)

    if category in data:
        del data[category]
        save_json(path, data)
        print(f'✅  CVE Vulnerability category "{category}" was deleted!')
    else:
        print(f'❌  CVE Vulnerability category {category} not found.')
