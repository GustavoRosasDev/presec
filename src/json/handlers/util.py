#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.etc.imports import json


def load_json(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file)


def save_json(path, json_data):
    with open(path, "w", encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)
