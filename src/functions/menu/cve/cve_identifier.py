#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""
import sys
from src.etc.imports import subprocess

# 🛠️ UTIL
from src.json.handlers.util import load_json


def identify_vulnerability_on_windows(target_url, cve_vulnerability_code):
    try:
        # Construa o comando PowerShell
        powershell_command = (f"$url = \"{target_url}\"; $vulnerability = \"{cve_vulnerability_code}\"; $result = "
                              f"Invoke-WebRequest -Uri $url -Method Head; if ($result.Headers -match $vulnerability)"
                              f" {{ Write-Host 'Vulnerability found' }} else {{ Write-Host 'Secure website' }}")

        # Execute o comando e capture a saída como bytes
        result = subprocess.run(["powershell", powershell_command], capture_output=True)

        # Decode a saída usando utf-8
        decoded_result = result.stdout.decode('utf-8', errors='replace')

        if decoded_result:
            # Retorne a saída decodificada
            return decoded_result
        elif result.stderr:
            # Retorne a saída de erro decodificada
            return (f"\n❌ Oops! Something went wrong while executing the chosen command.\n"
                    "Please check your command line and try again. If the issue persists, contact support for "
                    "assistance.\n\n"
                    f"Error output:\n→  {result.stderr.decode('utf-8', errors='replace')}\n")

    except subprocess.CalledProcessError as e:
        # Retorne a mensagem de erro
        return f"Error executing the command: {e}"


def identify_vulnerability_on_linux(target_url, cve_vulnerability_code):
    try:
        # Construa o comando cURL para Linux
        curl_command = f"curl -sI {target_url} | grep {cve_vulnerability_code}"

        # Execute o comando e capture a saída como bytes
        result = subprocess.run(["bash", "-c", curl_command], capture_output=True)

        # Decode a saída usando utf-8
        decoded_result = result.stdout.decode('utf-8', errors='replace')

        if decoded_result:
            # Retorne a saída decodificada
            return decoded_result
        elif result.stderr:
            # Retorne a saída de erro decodificada
            return (f"\n❌ Oops! Something went wrong while executing the chosen command.\n"
                    "Please check your command line and try again. If the issue persists, contact support for "
                    "assistance.\n\n"
                    f"Error output:\n→  {result.stderr.decode('utf-8', errors='replace')}\n")

    except subprocess.CalledProcessError as e:
        # Retorne a mensagem de erro
        return f"Error executing the command: {e}"


def check_vulnerability(target_url, cve_vulnerability_code):
    if sys.platform == 'win32':
        result = identify_vulnerability_on_windows(target_url, cve_vulnerability_code)
    else:
        result = identify_vulnerability_on_linux(target_url, cve_vulnerability_code)

    # Armazenar resultados em uma lista
    if result == 'Vulnerability found':
        message = f'{result}: CVE Code "{cve_vulnerability_code}" detected in the URL "{target_url}"'
        return message
    else:
        return None


if __name__ == "__main__":

    # region (GET) Values from interface
    single_verification = False
    url = 'https://www.google.com/'
    # endregion

    # region (GET) Values from JSON
    json_path = '../../../json/cve_list.json'
    json_data = load_json(json_path)
    print(json_data)
    # endregion

    # region (CONVERT) Key to CVE-CODE
    # endregion

    if single_verification:
        specific_vulnerability = 'CVE-2023-44483'
        check_vulnerability(url, specific_vulnerability)

    else:
        vulnerability_to_cve = load_json(json_path)
        for vulnerability, cve_list in vulnerability_to_cve.items():
            print(f"Vulnerability: {vulnerability}")
            for cve_code in cve_list:
                print(f"  CVE Code: {cve_code['code']}")
                print(f"  CVE Description: {cve_code['description']}")
                check_vulnerability(url, cve_code)
