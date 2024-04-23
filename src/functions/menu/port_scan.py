#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.etc.imports import (ThreadPoolExecutor,
                             tqdm,
                             socket,
                             AF_INET,
                             SOCK_STREAM,
                             error,
                             timeout)


def scan_single_port(target_ip, port):
    """
        Scans a specific port on the target IP.

        Parameters:
        - target_ip (str): The target IP address.
        - port (int): The port to scan.

        Returns:
        - int or None: The open port if successful, None otherwise.
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((target_ip, port))
        return port
    except (timeout, error):
        return None
    finally:
        sock.close()


def port_scan(target_ip, num_threads, start_port, end_port):
    """
        Elevates user permissions and scans a range of ports on the target IP using multiple threads.

        Parameters:
        - target_ip (str): The target IP address.
        - start_port (int): The starting port of the scan range.
        - end_port (int): The ending port of the scan range.
        - num_threads (int): The number of threads to use for parallel scanning.

        Returns:
        - list: List of open ports found during the scan.
    """

    if not num_threads:
        num_threads = 1

    open_ports = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(scan_single_port, target_ip, port) for port in range(start_port, end_port + 1)]

        for future in tqdm(futures, desc="Progress", unit=" Iterations"):
            result = future.result()
            if result is not None:
                open_ports.append(result)

    print(f'\nOpen Ports in {target_ip}   →   {open_ports}\n')
