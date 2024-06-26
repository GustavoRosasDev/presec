<!-- Logo -->
<p align="center">
  <img width="90" align="center" src="src/images/logo_sec.png">
</p>

<!-- Title -->
<h1 align="center">
  PreSec
</h1>

<!-- Subtitle -->
<p align="center">
  Pre-Programmed Security Tool
</p>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Cross-Platform-brightgreen" alt="Platform">
  <img src="https://img.shields.io/badge/Open-Source-brightgreen" alt="Source Code">
  <img src="https://img.shields.io/badge/Version-Beta-yellow" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.11-blue" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/CustomTkinter-5.2.2-blue" alt="CustomTkinter">
</p>

## Introduction
<!-- Index -->
<details>
  <summary><strong>📚 Index</strong></summary>

  * [Introduction](#introduction)
  * [About the software](#about-the-software)
      * [Functionalities](#functionalities)
      * [Features](#features)
      * [Extra](#extra)
      * [Other media](#other-media)
  * [Note](#note)
  * [Instructions](#instructions)
  * [Get started](#get-started)
  * [How to run PreSec?](#how-to-run-presec)
      * [Using CMD or PowerShell](#using-cmd-or-powershell)
      * [Using Bash](#using-bash)
  * [Contribution and Licensing](#contribution-and-licensing)
      * [Contribute](#contribute)
      * [Third-Party Software](#third-party-software)
      * [License](#license)


</details>

<!-- Overview -->
<details>
  <summary><strong>📰 Overview</strong></summary>

  **PreSec** is a cybersecurity software that I created to simplify the application of concepts I learned after completing the Leveling module in the <a href="https://hackersdobem.org.br/">Hackers do Bem</a> course.
  
  Entirely built in Python, **PreSec** features a modern and intuitive Graphical User Interface (GUI) created with <a href="http://customtkinter.tomschimansky.com/">Customtkinter</a>, by <a href="https://github.com/TomSchimansky">Tom Schimansky</a>.
  
  It's a comprehensive solution initially designed to simplify non-critical tasks, such as preventive analysis and monitoring. 
  
  The software encompasses three main functionalities, allowing customization of appearance (dark mode and light mode) and language (English, Portuguese, and Spanish), as well as the creation and complete management (CRUD) of your own commands and CVE vulnerabilities.

</details>

## About the software
### Functionalities
<!-- Command-Line -->
<details>
  <summary><strong>💀 Command-line</strong></summary>

Easy execution of command lines: **PreSec** facilitates command execution with a straightforward approach. 
By registering and organizing commands from basic to advanced, this feature simplifies tasks, 
mmaking them accessible to all skill levels.<br />

**Parameters:**<br />

| Field                 | Type/reference                                                                     | Description                                                     |
|-----------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `user_type`           | [Combobox](https://customtkinter.tomschimansky.com/documentation/widgets/combobox) | Allows the user **to filter** commands by privileges.           |
| `category`            | [Combobox](https://customtkinter.tomschimansky.com/documentation/widgets/combobox) | Allows the user **to filter** commands by category.             |
| `system`              | [Entry](https://customtkinter.tomschimansky.com/documentation/widgets/entry)       | **Automatically identifies** the operating system.              |
| `choose_a_command *`  | [Combobox](https://customtkinter.tomschimansky.com/documentation/widgets/combobox) | Required field.<br />Allows the user **to choose** the command. |
| `command_line`        | [Textbox](https://customtkinter.tomschimansky.com/documentation/widgets/textbox)   | Allows the user **to view only** the command line.              |
| `command_description` | [Textbox](https://customtkinter.tomschimansky.com/documentation/widgets/textbox)   | Allows the user **to view only** the command description.       |

<br />**Demonstration:**<br />
![command_line](https://github.com/GustavoRosas-Dev/GUI_PreSec/assets/113495972/26c5d9d2-7162-425e-ad51-d2c4c9c0e8d5)

</details>

<!-- Port Scanner -->
<details>
  <summary><strong>🔎 Port Scanner</strong></summary>

Simplify network exploration with PreSec's active port scanner. Just provide the IP address, adjust your preferences, and allow the tool to perform an efficient scan. Ideal for identifying suspicious activities and maintaining a secure environment.<br />

**Parameters:**<br />

| Field           | Type/reference                                                                 | Description                                                            |
|-----------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `ipv4_adress *` | [Entry](https://customtkinter.tomschimansky.com/documentation/widgets/entry)   | Required field.<br />Allows the user **to set** IPv4 address.          |
| `use_my_ip`     | [Slider](https://customtkinter.tomschimansky.com/documentation/widgets/slider) | Allows the user **to define** an IPv4 or **choose** their own.         |
| `threads`       | [Entry](https://customtkinter.tomschimansky.com/documentation/widgets/entry)   | Allows the user **to define** the number of threads that will be used. |
| `start_port *`  | [Entry](https://customtkinter.tomschimansky.com/documentation/widgets/entry)   | Required field.<br />Allows the user **to choose** the start port.     |
| `end_port *`    | [Entry](https://customtkinter.tomschimansky.com/documentation/widgets/entry)   | Required field.<br />Allows the user **to choose** the end port.       |

<br />**Demonstration:**<br />
![port_scanner](https://github.com/GustavoRosas-Dev/GUI_PreSec/assets/113495972/4fdd8927-eb15-404d-a666-4edc0c8e8a21)

</details>

<!-- CVE Vulnerabilities -->
<details>
  <summary><strong>🛡️ CVE Vulnerability</strong></summary>

- Easily identify known vulnerabilities by CVE on any website (*with proper authorization*) using PreSec. Simply provide the website URL, choose the desired scan type (single, list, or all), and let **PreSec** do the rest.
- Customize vulnerabilities and categories (in the "configure" tab) for a dynamic environment tailored to your needs.<br />

**Parameters:**<br />

| Field                                                    | Type/reference                                                                     | Description                                                                                                                             |
|----------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------| 
| `target_url *`                                           | [Entry](https://customtkinter.tomschimansky.com/documentation/widgets/entry)       | Required field.<br />Allows the user **to define** any target url.                                                                      |
| `single_cve_check`, `list_cve_check` and `all_cve_check` | [Combobox](https://customtkinter.tomschimansky.com/documentation/widgets/combobox) | Allows the user **to choose** between a single CVE code, a list of code (containing a group of CVE codes), or all registered CVE codes. |
| `list`, `single` and `all`                               | [Switch](https://customtkinter.tomschimansky.com/documentation/widgets/textbox)    | Allows the user **to set** the type of check: single, list or all.                                                                      |
| `vulnerability_description`                              | [Textbox](https://customtkinter.tomschimansky.com/documentation/widgets/textbox)   | Allows the user **to view only** the vulnerability description.                                                                         |

**Demonstration:**<br />
![cve_vulnerabilities](https://github.com/GustavoRosas-Dev/GUI_PreSec/assets/113495972/cf2ea450-7685-4d31-bc44-8cfe0815795c)

</details>

... and more are coming!

### Features
<!-- Appearance mode -->
<details>
  <summary><strong>🎨 Appearance mode</strong></summary>

Change between **dark** or **light** mode.

  ![Appearance Mode](https://i.imgur.com/sdOtWvX.png)

</details>

<!-- Language mode -->
<details>
  <summary><strong>🔊 Language mode</strong></summary>

  Change between **english**, **portuguese** or **spanish** version.

![languages](https://github.com/GustavoRosas-Dev/GUI_PreSec/assets/113495972/25d3046b-3cf3-4891-a354-d3a0a8b462e1)

</details>

<!-- User settings -->
<details>
  <summary><strong>⚙️ User settings</strong></summary>

  User type (e.g., `user` or `admin`) and platform system (e.g., `Windows` or `Linux`) are stored as user preferences in JSON format, in this folder: `src/json/preferences.json`.
  
  ![User Settings](https://i.imgur.com/oiGEKKw.png)

Add more as needed.

</details>

### Extra
<!-- Customize it -->
<details>
  <summary><strong>🛠️ Customize it (CRUD)</strong></summary>

Create your own:
- **Command-Line**: Configure (*create, update and delete*) commands for Windows (shell) or Linux (bash) and organize in categories.

  ![Configure Tab > Command Line](https://i.imgur.com/GQ8bfvN.png)

- **CVE Vulnerabilities**: Configure (*create, update and delete*) CVE codes and organize in categories

  ![Configure Tab > CVE Vulnerability](https://i.imgur.com/LWuVw3m.png)

</details>

<!-- Prerequisites -->
<details>
  <summary><strong>🌟 Good practices</strong></summary>

  | Category                                                                                                                               | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                         |
  |----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
  | [Clean Code](https://dev.to/alexomeyer/10-must-know-patterns-for-writing-clean-code-with-python-56bf)                                  | ![Code Verticalization](https://img.shields.io/badge/Verticalization-100%25-brightgreen) ![Code Language](https://img.shields.io/badge/Code_In_English-100%25-brightgreen) ![High Cohesion](https://img.shields.io/badge/High_Cohesion-90%25-lightgreen) ![Low Coupling](https://img.shields.io/badge/Low_Coupling-80%25-yellowgreen) ![SoC](https://img.shields.io/badge/SoC-70%25-lightyellow) ![SRP](https://img.shields.io/badge/SRP-60%25-yellow) ![Modularization](https://img.shields.io/badge/Modularization-60%25-yellow) | Practices for coding to make the code clean and readable.                                           |
  | [PEPs](https://peps.python.org/pep-0000/#introduction)                                                                                 | ![PEP-8](https://img.shields.io/badge/PEP_8-100%25-brightgreen) ![PEP-20](https://img.shields.io/badge/PEP_20-80%25-yellowgreen) ![PEP-257](https://img.shields.io/badge/PEP_257-50%25-orange)                                                                                                                                                                                                                                                                                                                                     | Standards for code style in Python. Zen of Python principles. Conventions for docstrings in Python. |
  | [Pythonic](https://testdriven.io/blog/clean-code-python/#:~:text=PEP%208%20.-,C%C3%B3digo%20Pit%C3%B4nico,-O%20c%C3%B3digo%20Pythonic) | ![Pythonic](https://img.shields.io/badge/Pythonic-50%25-orange)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Writing Python code in the "Pythonic" way.                                                          |

</details>

### Other media
<!-- Start concept -->
<details>
  <summary><strong>✏️ Start concept (basic sketch in Figma)</strong></summary>

  ![Start concept](https://i.imgur.com/MMqGZS1.png)

</details>

<!-- Design mockup (Figma) -->
<details>
  <summary><strong>✨ Design mockup (Figma)</strong></summary>

![Design mockup](https://i.imgur.com/XvQoPag.png)

</details>

<!-- Frame Managment (Screenshot) -->
<details>

<summary><strong>🖼️ Frame management (screenshot)</strong></summary>
All are separated into frames and subframes to facilitate the layout/grid and manipulation of elements.<br />

  ![Frame Managment > Command Line Tab](https://i.imgur.com/ZDx4Rqu.png)<br /> 
  ![Frame Managment > CVE Vulnerabilities Tab](https://i.imgur.com/nIAEElb.png)<br />

</details>

<!-- Project Structure (Screenshot) -->
<details>
<summary><strong>🖼️ Project struture(screenshot)</strong></summary>

  ![Project Structure](https://i.imgur.com/lUxCyI5.png)<br />

</details>

<!-- Dependencies (Screenshot) -->
<details>
<summary><strong>🖼️ Dependencies (screenshot)</strong></summary>
 Dependencies do not have CVE vulnerabilities.

  ![CVE Vulnerabilities Free](https://i.imgur.com/vLjgbAW.png)<br />

> [!IMPORTANT]
> During development, **only one** dependency with a CVE vulnerability was identified, but **it has already been corrected**.

  ![CVE Vulnerabilities Free](https://i.imgur.com/pv5pZ5Q.png)

</details>

<!-- Video Presentation -->
<details>
  <summary><strong>🎥 Video presentation</strong></summary>

Opens on YouTube. 

> [!WARNING]
> Active captions, audio in Portuguese (🇧🇷) only.<br />

[![YouTube Video](https://i.imgur.com/C8pDEtc.png)](https://www.youtube.com/watch?v=Heqp-fZ53xA)
Video url: https://www.youtube.com/watch?v=Heqp-fZ53xA

</details>

## Note
> 👉  `PreSec (beta)` is currently under development in branch `main`.

## Instructions
<!-- Prerequisites -->
<details>
  <summary><strong>📋 Prerequisites</strong></summary>

  1. **Windows 10** or higher and **Ubuntu 22.04** or higher.
  2. [Python 3.11.4](https://www.python.org/downloads/release/python-3114/) or higher
  3. [git 2.40.1](https://git-scm.com/downloads) or higher
  4. [pip 23.1.2](https://pypi.org/project/pip/) or higher

</details>

<!-- Installing prerequisites -->
<details>
  <summary><strong>⬇️ Installing prerequisites</strong></summary>

   <h3><span style="color:#cccc">On Linux (via Bash):</span></h3>

Update system dependencies before proceeding. To do this, copy and paste the command below into your Terminal and press `enter`:
  ```
  sudo apt update
  ```

...and only then, proceed with the tutorial below:

   <!-- Installing Python -->
<details>
  <summary><strong>🐍 Installing Python</strong></summary>

  ```
  sudo apt install python3.11
  ```
</details>

   <!-- Installing Git -->
<details>
  <summary><strong>🐙 Installing git</strong></summary>
    
  ```
  sudo apt install git
  ```
</details>

   <!-- Installing pip -->
<details>
  <summary><strong>📦 Installing pip</strong></summary>
    
  ```
  sudo apt install python3.11-pip
  ```
</details>

</details>

### Get Started
To use this software, follow the steps below:

<!-- 1st - Cloning repository -->
<details>
  <summary><strong>1️⃣ Cloning this repository</strong></summary>

1. Navigate to the folder where you typically install programs or applications on your computer. Any folder you prefer.
2. Opens the Terminal. To do this, **follow any of the instructions below**:
   
    **On Windows**, there are 2 options:
      - Via **CMD** *(Command Prompt)*:
         1. In the address bar located at the top of the window, **click on the folder address field**. If it's not visible, ensure that 'Address Bar' is checked in the 'View' menu.
         2. Type `CMD` in the selected address bar and press `enter`. This opens a **CMD-type** terminal in the current folder.
      - Via **PowerShell**:
         1. In the upper address bar, click to select the folder address. If not visible, ensure 'Address Bar' is checked in the 'View' menu.
         2. Right-click on the selected address bar and choose `Open in Terminal`. This opens a **PowerShell-type** terminal in the current folder.

    **On Linux** (via Bash):<br />
   - Right-click on the folder background and select `Open in Terminal` or navigate to the project root folder using the `cd` command.

3. Next, clone this repository into the folder you chose. To do this, copy and paste the command below into your terminal and press `enter`:
  ```
  git clone https://github.com/GustavoRosas-Dev/GUI_PreSec.git
  ```

Then, **navigate into the project folder**. To do this, copy and paste the command below into your terminal and press `enter`:
  ```
  cd GUI_PreSec
  ```

> [!NOTE]
> The above command will use the git clone module to create an exact copy of this repository in your folder (local repository).

</details>

<!-- 2nd - Create Virtual environment -->
<details>
  <summary><strong>2️⃣ Create virtual environment</strong></summary>

With the Terminal still open, copy and paste the command below and press `enter`:

**On Windows**:
  ```
  python -m venv venv
  ```
**On Linux**:

Begin by installing the package below, which **provides support** for virtual environments (venv), in Python 3.11.
  ```
  sudo apt install python3.11-venv
  ```

The execution of the above command **requires elevated administrative privileges** (indicated by the use of `sudo`). Therefore, you will be prompted for the superuser (`root`) password **to ensure security** and **authorize the package installation** in Python 3.11.

Next, **create your virtual environment** by copying and pasting the code below into your Terminal:
  ```
  python3.11 -m venv venv
  ```

> [!NOTE]
> The above command utilizes the `python` interpreter (via environment variables) with the `-m` (module) parameter to create a virtual environment (`venv`) named the same as `venv`. You could name it whatever you like; however, it is a universal convention (adopted by the Python community) to name it this way.

</details>

<!-- 3rd - Activate Virtual environment -->
<details>
  <summary><strong>3️⃣ Activate virtual environment</strong></summary>

The next step is to **activate the virtual environment**. See how simple it is:

**On Windows**: <br />
1. Navigate to the `Scripts` folder:
    ```shell
    cd venv\Scripts
    ```

2. Then, **activate** the virtual environment:

    ```shell
    activate
    ```
3. And finally, return to the root folder. To do this, type the command below and press `enter`. **Repeat this twice**:

    ```shell
    cd ..
    ```
   
> [!NOTE]
> The `cd` (change directory) command, when used with `..`, allows you to navigate up one level in the directory structure. Executing this combination twice will bring you back to the main project folder, specifically the `GUI_PreSec/` directory.


**On Linux**: <br />
  ```bash
  source venv/bin/activate
  ```

✅ To confirm that the virtual environment **has been activated** correctly , simply look at your Terminal and check if `(venv)` appears on the same line where you would type your next command.<br /><br />See an example in the image below:<br />
![Activating Virtual Environment](https://i.imgur.com/F1bd2el.png)

<!-- Newbie Catcher  -->
<details>
  <summary><strong> (Bonus) If you are a newbie in development (like me 😏), click here.</strong></summary>

Now, you might be wondering, 'Why should I **create** and **activate** a virtual environment, I'm right?'<br />

![Activating Virtual Environment](https://i.imgur.com/Wrjdct6.jpg)

If you're wondering why you should create and activate a virtual environment, it's essential to understand that a virtual environment provides a dedicated space for installing dependencies (libraries) isolated from the rest of your machine. Each project can have its own virtual environment, ensuring that the dependencies required for that specific project are maintained separately.<br />

This practice is crucial for a few reasons:

> [!TIP] **Consistency**: It guarantees a consistent environment for your project, preventing conflicts between different projects that may require different versions of the same library.

> [!TIP] **Isolation**: Dependencies are confined to the virtual environment, avoiding interference with other projects or system-level packages.

> [!TIP] **Collaboration**: When collaborating on projects, sharing the project's virtual environment specifications (usually stored in a requirements.txt file) enables others to recreate the exact environment, ensuring a smooth collaboration experience across different machines.

</details>

</details>

<!-- 4th - Install requirements -->
<details>
  <summary><strong>4️⃣ Install requirements</strong></summary>

With the virtual environment active, simply install the dependencies (libraries) that the project needs to function. To do this, copy and paste the command below into the Terminal and press `enter`:

**On Windows:**
  ```
  pip install -r requirements.txt
  ```
**On Linux:**
  ```
  pip3.11 install -r requirements.txt
  ```

> [!NOTE]
> The above command uses `pip` _(Package Installer for Python)_ to install dependencies specified in the requirements file. The `install` command is a fundamental part of pip, followed by the `-r` _(read)_ parameter, indicating that it should **read and install the requirements**. The `requirements.txt` file, located in the root folder of this project, contains a **list of necessary libraries** for the project to function.

</details>

## How to Run PreSec

Make sure you are in the project's root folder (`GUI_PreSec/`). Then, copy and paste the command below into the Terminal, and press `enter`:

### Using CMD or PowerShell
  ```
  python main.py
  ```

### Using Bash
  ```
  python3.11 main.py
  ```

## Contribution and Licensing
### Contribute

See [CONTRIBUTING](src/docs/CONTRIBUTING.md)

### Third-Party Software

See [ThirdPartyNotices](src/docs/THIRD-PARTY-NOTICES.md)

### License
See [LICENSE](src/docs/LICENSE.md)

## Special Thanks 🥰
**[Hackers Do Bem](https://www.linkedin.com/groups/9579478/)** (1st BR class).

<!-- SVG Typing -->
<p align="center"><br /><br />
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=4285F4&center=true&random=false&width=435&lines=Keep+Learning.+Keep+Hacking!" alt="Typing SVG">
</p><br /><br />