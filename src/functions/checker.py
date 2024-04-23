#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.etc.imports import version_info, platform, json, os


def check_python_version():
    """
        Checks the Python version and prints a warning message if it is below 3.11.

        Returns:
            bool: True if the Python version is below 3.11, False otherwise.
    """

    if version_info < (3, 11):
        print("This script requires Python 3.11 or higher")
        return True
    return False


def check_platform():
    """
    Check the operating system and set global variables accordingly.

    Returns:
    Tuple: A tuple containing operational_system (str),
           command_line_interface_index (int),
           user_type (list of str),
           shell (str),
           command_line_interface (str).
    """

    global operational_system, command_line_interface_index, user_type, shell, command_line_interface

    if 'linux' in platform.lower():
        shell = "bash"
        operational_system = "Linux"
        command_line_interface = shell
        command_line_interface_index = 0
        user_type = ["usr", "root"]
    elif 'win' in platform.lower():
        shell = "shell"
        operational_system = "Windows"
        command_line_interface = 'powershell'
        command_line_interface_index = 1
        user_type = ["user", "admin"]

    return operational_system, command_line_interface_index, user_type, shell, command_line_interface


operational_system, command_line_interface_index, user_type, shell, command_line_interface = check_platform()


def check_json_values():
    """
        Check for the existence of a JSON file in specified paths and return its content.

        Returns:
        - dict: The content of the JSON file.

        Raises:
        - FileNotFoundError: If no JSON file is found in the specified paths.
    """

    json_path_options = ['src/json/commands.json', '../src/json/commands.json']

    for json_path in json_path_options:
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as arquivo:
                json_content = json.load(arquivo)
            return json_content

    # Se nenhum arquivo for encontrado, você pode levantar uma exceção ou retornar um valor padrão
    raise FileNotFoundError("Nenhum arquivo JSON encontrado nos caminhos especificados.")


def check_group_of_commands(chosen_command_line_interface, chosen_user_type, level, command_name=None):
    """
    Check and retrieve a group of commands based on specified parameters.

    Parameters:
    - command_line_interface (str): The type of shell to use, e.g., "bash", "powershell", "cmd".
    - user_type (str): The user permission level, e.g., "user", "usr", "admin", "root".
    - level (str): The type of command, e.g., "Basic" or "Advanced".
    - command_name (str, optional): Specific command to retrieve information. Default is None.

    Returns:
    - dict: A group of commands based on the specified parameters.
    """

    if chosen_user_type == "usr" or chosen_user_type == "user":
        user_type_index = 0
        if platform == 'linux':
            chosen_user_type = 'usr'
    else:
        user_type_index = 1
        if platform == 'linux':
            chosen_user_type = 'root'

    json_values = check_json_values()

    if command_name:
        group = (json_values['type'][command_line_interface_index][chosen_command_line_interface][user_type_index][
            chosen_user_type][0][level][command_name])
    else:
        group = json_values['type'][command_line_interface_index][chosen_command_line_interface][user_type_index][
            chosen_user_type][0][level]

    return group


def check_list_of_command_names(chosen_user_type, level):
    """
        Retrieve a list of command names based on user permission and command type.

        Parameters:
        - user_type (str): The user's permission level (e.g., 'user', 'admin').
        - level (str): The type of command (e.g., 'basic', 'advanced').

        Returns:
        - list: A list of command names filtered based on user permission and command type.
    """

    group = check_group_of_commands(shell, chosen_user_type, level)
    list_of_commands = []

    for command in group:
        list_of_commands.append(command)

    return list_of_commands


def check_list_of_command_line_and_description(chosen_user_type, level, command_name):
    """
        Check the list of command lines and descriptions based on user permissions and chosen command type.

        Parameters:
        - user_type (str): User's permission level (e.g., 'user', 'admin').
        - level (str): Type of command (e.g., 'basic', 'advanced').
        - command_name (str): Specific command name chosen by the user.

        Returns:
        - tuple: A tuple containing the command line and its description.
                 The command line is a string representing the actual command.
                 The command description is a string providing details about the command.

        Note: The implementation of the 'check_group_of_commands' function and the 'shell' variable
              needs to be provided for a complete understanding of the functionality.
    """
    group = check_group_of_commands(shell, chosen_user_type, level, command_name)
    command_line = group['command']
    command_description = group['description']

    return command_line, command_description
