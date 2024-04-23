#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.etc.imports import subprocess


def execute_command(chosen_command, shell_type='cmd'):
    """
    Execute a command in the specified shell.

    Parameters:
    - chosen_command (str): The command to be executed.
    - shell_type (str, optional): The type of shell to be used. Default is 'cmd'.
        - 'cmd' for Command Prompt on Windows.
        - 'powershell' for PowerShell on Windows.
        - 'bash' for Bash on Linux.

    Returns:
    - str: The decoded output of the command if successful.
          Error message if there is an issue during execution.
    """
    try:
        # Define the shell to be used based on the shell_type parameter
        shell = True if shell_type == 'cmd' else False
        if shell_type == 'powershell':
            command = ["powershell.exe", chosen_command]
        else:
            command = chosen_command
            shell = shell_type

        # Execute the command and capture the output as bytes
        result = subprocess.run(command, shell=shell, capture_output=True)

        # Decode the output using utf-8
        decoded_result = result.stdout.decode('utf-8', errors='replace')

        if decoded_result:
            # Return the decoded output
            return decoded_result
        elif result.stderr:
            # Return the decoded error output
            return (f"\n❌ Oops! Something went wrong while executing the chosen command.\n"
                    "Please check your command line and try again. If the issue persists, contact support for "
                    "assistance.\n\n"
                    f"Error output:\n→  {result.stderr.decode('utf-8', errors='replace')}\n")

    except subprocess.CalledProcessError as e:
        # Return error message
        return f"Error executing the command: {e}"


def run(active_frame, chosen_command=None, shell_type=None):
    """
        Execute a command based on the active frame.

        Parameters:
        - active_frame (str): The active frame identifier ("first", "second", or "third").
        - chosen_command (str): The command to be executed.
        - shell_type (str): The type of shell to be used.
            - 'cmd' for Command Prompt on Windows.
            - 'powershell' for PowerShell on Windows.
            - 'bash' for Bash on Linux.

        Returns:
        - None: The result or error message is printed within the function.
    """

    if active_frame == "first":
        # Call the function to execute the command + desired shell (cmd, powershell or bash)
        result = execute_command(chosen_command, shell_type=shell_type)

        # Display the result or error message
        print(result)

    return
