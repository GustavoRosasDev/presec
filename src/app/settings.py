#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.etc.imports import ctk, os, Image, platform
from .info import APP_NAME

# Controls the dimensions of the application.
APP_WIDTH = 650
APP_HEIGHT = 500

# Create instance and set APP name, always on top
APP = ctk.CTk()
APP.title(APP_NAME)
APP.attributes("-topmost", True)

# Initial appearance
ctk.set_appearance_mode("Dark")  # Dark, light, System
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# Load (.png) version of the logo
app_logo_image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "images/")
APP_LOGO = ctk.CTkImage(Image.open(os.path.join(app_logo_image_path, "logo_sec.png")), size=(26, 26))

# Get screen dimensions
SCREEN_WIDTH = APP.winfo_screenwidth()
SCREEN_HEIGHT = APP.winfo_screenheight()

# Calculate central window position
posicao_x = (SCREEN_WIDTH - APP_WIDTH) // 2
posicao_y = (SCREEN_HEIGHT - APP_HEIGHT) // 2

# Set window geometry (centered on screen)
APP.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{posicao_x}+{posicao_y}")

# Set minimum and maximum APP dimensions
APP.minsize(width=APP_WIDTH, height=APP_HEIGHT)  # Altura mínima em pixels
APP.maxsize(width=APP_WIDTH, height=APP_HEIGHT)  # Altura máxima em pixels

# Sets the application icon "only if the platform is Windows", because on Linux the icon may not be displayed in the
# window header.
if platform == 'win32':
    try:
        APP.iconbitmap(r"src\images\logo_sec.ico")
    except FileNotFoundError:
        APP.iconbitmap(r"_internal\resources\images\logo_sec.ico")
