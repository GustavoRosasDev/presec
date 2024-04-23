#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


import socket
from src.etc.imports import platform, psutil


def get_ipv4():
    try:
        # Verifica se o sistema operacional é Linux
        if platform == 'linux':
            # Obtém informações sobre todas as interfaces de rede
            interfaces = psutil.net_if_addrs()

            # Verifica se a interface 'lo' está presente
            if 'lo' in interfaces:
                # Obtém o endereço IPv4 associado à interface 'lo'
                ipv4_address = interfaces['lo'][0].address
                return ipv4_address

        # Para outros sistemas operacionais ou se a interface 'lo' não estiver presente, usa o comportamento original
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        return ipv4_address

    except socket.error as e:
        # Trata erros ao obter o endereço IPv4
        print(f"Erro ao obter o endereço IPv4: {e}")
        return None
