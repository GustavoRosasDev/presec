#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.json.handlers.util import load_json, save_json


def add_command(json_command_path,
                command_line_interface,
                user_type,
                level,
                command_name,
                command_line,
                description):
    """
        Add a new command to the specified JSON file, associating it with the given command-line interface, user type,
        and access level.

        Parameters:
        - json_command_path (str): The file path of the JSON file containing command data.
        - command_line_interface (str): The command-line interface for which the command is intended.
        - user_type (str): The type of user for whom the command is applicable.
        - level (str): The access level required to use the command.
        - command_name (str): The name of the command to be added.
        - command_line (str): The command-line string associated with the command.
        - description (str): A brief description of the command.

        Returns:
        None
        """

    json_data = load_json(json_command_path)

    for entry in json_data["type"]:
        if command_line_interface in entry and user_type in entry[command_line_interface][0]:
            user_entry = entry[command_line_interface][0][user_type][0]
            if level in user_entry:
                new_command = {
                    "command": command_line,
                    "description": description
                }
                user_entry[level][command_name] = new_command

    save_json(json_command_path, json_data)


def update_command(json_command_path,
                   command_line_interface,
                   user_type,
                   level,
                   command_name,
                   new_command,
                   new_description):
    """
        Update an existing command in the specified JSON file with new command-line and description values.

        Parameters:
        - json_command_path (str): The file path of the JSON file containing command data.
        - command_line_interface (str): The command-line interface for which the command is intended.
        - user_type (str): The type of user for whom the command is applicable.
        - level (str): The access level required to use the command.
        - command_name (str): The name of the command to be updated.
        - new_command (str): The new command-line string associated with the command.
        - new_description (str): The new description for the command.

        Returns:
        None
        """

    json_data = load_json(json_command_path)

    for entry in json_data["type"]:
        if command_line_interface in entry and user_type in entry[command_line_interface][0]:
            user_entry = entry[command_line_interface][0][user_type][0]
            if level in user_entry and command_name in user_entry[level]:
                user_entry[level][command_name]["command"] = new_command
                user_entry[level][command_name]["description"] = new_description

    save_json(json_command_path, json_data)


def delete_command(json_command_path,
                   command_line_interface,
                   user_type,
                   level,
                   command_name):
    """
        Delete an existing command from the specified JSON file based on the provided parameters.

        Parameters:
        - json_command_path (str): The file path of the JSON file containing command data.
        - command_line_interface (str): The command-line interface for which the command is intended.
        - user_type (str): The type of user for whom the command is applicable.
        - level (str): The access level required to use the command.
        - command_name (str): The name of the command to be deleted.

        Returns:
        None
        """

    json_data = load_json(json_command_path)

    for entry in json_data["type"]:
        if command_line_interface in entry and user_type in entry[command_line_interface][0]:
            user_entry = entry[command_line_interface][0][user_type][0]
            if level in user_entry and command_name in user_entry[level]:
                del user_entry[level][command_name]

    save_json(json_command_path, json_data)
