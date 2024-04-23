#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.manager import *

all_cve_categories = get_cve_vulnerability_categories(cve_json_path)
all_cve_codes = get_all_cve_vulnerability_codes(cve_json_path)


def change_app_language(new_language):
    home_tab_menu_appearance_dropdown_option = ctk.get_appearance_mode()

    # Define active scrollable frame (in "Configure" tab)
    configure_tab_first_container_first_scrollable_frame.pack(fill=ctk.BOTH,
                                                              expand=True,
                                                              padx=10, pady=10)
    configure_tab_first_container_second_scrollable_frame.pack_forget()

    match new_language:

        case 'en':
            # region 🔵 "Home" Tab

            # region Container "Menu"
            home_tab_menu_title.configure(text=f' {APP_NAME} Menu')
            home_tab_menu_first_button.configure(text="Command-Line")
            home_tab_menu_second_button.configure(text="Port Scanner")
            home_tab_menu_third_button.configure(text="CVE Vulnerabilities")
            home_tab_menu_appearance_dropdown.configure(
                values=appearance_mode_english_options)
            if home_tab_menu_appearance_dropdown_option == "Dark":
                home_tab_menu_appearance_dropdown.set("Dark")
            if home_tab_menu_appearance_dropdown_option == "Light":
                home_tab_menu_appearance_dropdown.set("Light")
            # endregion

            # region 1️⃣ Home > "First" Container
            home_tab_first_container_title.configure(
                text="Command-Line Operations")
            home_tab_first_container_scrollable_frame_first_frame_text_description.configure(
                text='USER TYPE')
            home_tab_first_container_scrollable_frame_first_frame_second_subframe_text_description.configure(
                text='CATEGORY')
            home_tab_first_container_scrollable_frame_first_frame_third_subframe_text_description.configure(
                text='SYSTEM')
            home_tab_first_container_scrollable_frame_second_frame_text_description.configure(
                text='CHOOSE A COMMAND*')
            home_tab_first_container_scrollable_frame_third_frame_group_text_description.configure(
                text='COMMAND LINE')
            home_tab_first_container_scrollable_frame_fourth_frame_group_text_description.configure(
                text='COMMAND DESCRIPTION')
            # endregion

            # region 2️⃣ Home > "Second" Container
            home_tab_second_container_title.configure(text="Port Scanner")
            # Description texts
            home_tab_second_container_first_frame_group_text_description.configure(
                text='IPV4 ADDRESS *')
            home_tab_second_container_first_frame_group_first_entry.configure(
                placeholder_text='e.g. 192.168.79.1')
            home_tab_second_container_first_frame_group_second_subframe_text_description.configure(
                text='USE MY IP')
            home_tab_second_container_second_frame_group_first_subframe_text_description.configure(
                text='THREADS')
            home_tab_second_container_second_frame_group_first_subframe_first_entry.configure(
                placeholder_text='e.g. 100')
            home_tab_second_container_second_frame_group_second_subframe_text_description.configure(
                text='START PORT *')
            home_tab_second_container_second_frame_group_second_subframe_first_entry.configure(
                placeholder_text='e.g. 1')
            home_tab_second_container_second_frame_group_third_subframe_text_description.configure(
                text='END PORT *')
            home_tab_second_container_second_frame_group_third_subframe_first_entry.configure(
                placeholder_text='e.g. 1024')

            # endregion

            # region 3️⃣ Home > "Third" Container
            home_tab_third_container_title.configure(
                text="CVE Vulnerabilities")

            home_tab_third_container_first_frame_group_text_description.configure(
                text='TARGET URL *')
            home_tab_third_container_first_frame_group_first_entry.configure(
                placeholder_text='e.g. https://www.google.com/')

            # Slider description
            home_tab_third_container_second_frame_group_second_subframe_text_description.configure(
                text='LIST')
            home_tab_third_container_second_frame_group_second_subframe_first_slider.set(
                2)
            home_tab_third_container_second_frame_group_text_description.configure(
                text='LIST CVE CHECK')

            home_tab_third_container_third_frame_group_text_description.configure(
                text='VULNERABILITY DESCRIPTION')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '1.0',
                'end')
            home_tab_third_container_third_frame_group_first_textbox.insert(
                '0.0',
                'Checks for all vulnerabilities in a category')
            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='disabled')

            # endregion

            # region ▶️ "Run" Button

            home_tab_footer_description_text.configure(
                text='Pre-Programmed Security Tool')
            home_tab_footer_run_button.configure(text="Run")

            # endregion

            # endregion

            # region 🔴 "Configure" Tab
            # First Container (main)
            configure_tab_first_container_first_frame_first_subframe_text_description.configure(
                text="CHOOSE OPERATION TYPE")
            configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.configure(
                values=operation_type_english_options)
            configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.set(
                'Create')
            configure_tab_first_container_title.configure(
                text_color=LIGHT_BLUE_COLOR)

            configure_tab_first_container_first_frame_second_subframe_text_description.configure(
                text="CHOOSE AN ITEM")
            configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.configure(
                values=configure_tab_choose_an_item_english_options)
            configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.set(
                'Command-Line')

            # Configure Tab Title
            configure_tab_first_container_title.configure(
                text=f'{configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()} '
                     f'{configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.get()}')

            # First Scrollable Frame
            configure_tab_first_container_first_scrollable_frame_first_subframe_text_description.configure(
                text="CHOOSE OPERATING SYSTEM")

            configure_tab_first_container_first_scrollable_frame_second_subframe_text_description.configure(
                text="CHOOSE CATEGORY")
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.configure(
                values=command_line_category_english_options)
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.set(
                'básico')

            configure_tab_first_container_first_scrollable_frame_third_subframe_text_description.configure(
                text="CHOOSE USER TYPE")

            configure_tab_first_container_first_scrollable_frame_second_frame_text_description.configure(
                text="WRITE THE COMMAND NAME *")
            configure_tab_first_container_first_scrollable_frame_third_frame_group_text_description.configure(
                text="WRITE THE COMMAND. USE SIMICOLON (;) TO SKIP A LINE. *")
            configure_tab_first_container_first_scrollable_frame_fourth_frame_group_text_description.configure(
                text="WRITE A DESCRIPTION FOR THE COMMAND (optional)")

            configure_tab_footer_run_button.configure(
                text=f'{configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()}',
                fg_color=LIGHT_BLUE_COLOR,
                hover_color=DARK_BLUE_COLOR)

            # Second Scrollable Frame
            configure_tab_first_container_second_scrollable_frame_first_subframe_text_description.configure(
                text='TYPE'
            )
            configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.configure(
                values=cve_type_english_options
            )
            configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.set(
                value='CVE Code'
            )

            configure_tab_first_container_second_scrollable_frame_second_subframe_text_description.configure(
                text='ASSOCIATE TO LIST'
            )

            configure_tab_first_container_second_scrollable_frame_third_subframe_text_description.configure(
                text='IDENTIFICATION *'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                placeholder_text='e.g. CVE-2024-1234'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_text_description.configure(
                text='WRITE A DESCRIPTION FOR THE COMMAND'
            )

            # Footer
            configure_tab_footer_description_text.configure(
                text="Pre-Programmed Security Tool")

            # endregion

            # region 🟡 "Info" Tab

            # region Container "Info APP"
            info_tab_first_frame_group_first_info_text.configure(
                text="DEVELOPER")
            info_tab_second_frame_group_first_info_text.configure(
                text="APP NAME")
            info_tab_second_frame_group_first_info_text_space.configure(
                text="   ")
            info_tab_third_frame_group_first_info_text.configure(
                text="VERSION")
            info_tab_third_frame_group_first_info_text_space.configure(
                text="      ")
            # endregion

            # region Frame "Text + Button: Contact Developer"

            info_tab_footer_info_text.configure(
                text="Automations, Upgrades, or Support?")
            info_tab_footer_button.configure(text="Contact the developer")

            # endregion

            # endregion

        case 'pt':
            # region 🔵 "Home" Tab

            # region Container "Menu"
            home_tab_menu_title.configure(text=f' Menu {APP_NAME}')
            home_tab_menu_first_button.configure(text="Linha de Comando")
            home_tab_menu_second_button.configure(text="Scanner de Portas")
            home_tab_menu_third_button.configure(text="Vulnerabilidades CVE")
            home_tab_menu_appearance_dropdown.configure(
                values=appearance_mode_portuguese_options)
            if home_tab_menu_appearance_dropdown_option == "Dark":
                home_tab_menu_appearance_dropdown.set("Escuro")
            if home_tab_menu_appearance_dropdown_option == "Light":
                home_tab_menu_appearance_dropdown.set("Claro")
            # endregion

            # region 1️⃣ Home > "First" Container
            home_tab_first_container_title.configure(
                text='Operações de Linha de Comando')
            home_tab_first_container_scrollable_frame_first_frame_text_description.configure(
                text='TIPO DE USUÁRIO')
            home_tab_first_container_scrollable_frame_first_frame_second_subframe_text_description.configure(
                text='CATEGORIA')
            home_tab_first_container_scrollable_frame_first_frame_third_subframe_text_description.configure(
                text='SISTEMA')
            home_tab_first_container_scrollable_frame_second_frame_text_description.configure(
                text='ESCOLHA UM '
                     'COMANDO*')
            home_tab_first_container_scrollable_frame_third_frame_group_text_description.configure(
                text='LINHA DE COMANDO')
            home_tab_first_container_scrollable_frame_fourth_frame_group_text_description.configure(
                text='DESCRIÇÃO DO COMANDO')
            # endregion

            # region 2️⃣ Home > "Second" Container
            home_tab_second_container_title.configure(text="Scanner de Porta")
            # Description texts
            home_tab_second_container_first_frame_group_text_description.configure(
                text='ENDEREÇO IPV4 *')
            home_tab_second_container_first_frame_group_first_entry.configure(
                placeholder_text='Ex: 192.168.79.1')
            home_tab_second_container_first_frame_group_second_subframe_text_description.configure(
                text='USAR MEU IP')
            home_tab_second_container_second_frame_group_first_subframe_text_description.configure(
                text='PROCESSOS')
            home_tab_second_container_second_frame_group_first_subframe_first_entry.configure(
                placeholder_text='Ex: 100')
            home_tab_second_container_second_frame_group_second_subframe_text_description.configure(
                text='PORTA INICIAL *')
            home_tab_second_container_second_frame_group_second_subframe_first_entry.configure(
                placeholder_text='Ex: 1')
            home_tab_second_container_second_frame_group_third_subframe_text_description.configure(
                text='PORTA FINAL *')
            home_tab_second_container_second_frame_group_third_subframe_first_entry.configure(
                placeholder_text='Ex: 1024')
            # endregion

            # region 3️⃣ Home > "Third" Container
            home_tab_third_container_title.configure(
                text="Vulnerabilidades CVE")

            home_tab_third_container_first_frame_group_text_description.configure(
                text='URL ALVO')
            home_tab_third_container_first_frame_group_first_entry.configure(
                placeholder_text='Ex: https://www.google.com/')

            # Slider description
            home_tab_third_container_second_frame_group_second_subframe_text_description.configure(
                text='LISTA')
            home_tab_third_container_second_frame_group_second_subframe_first_slider.set(
                2)
            home_tab_third_container_second_frame_group_text_description.configure(
                text='LISTA CVE CHECK')

            home_tab_third_container_third_frame_group_text_description.configure(
                text='DESCRIÇÃO DA VULNERABILIDADE')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '0.0',
                'end')
            home_tab_third_container_third_frame_group_first_textbox.insert(
                '0.0',
                'Verifica todas as vulnerabilidades em uma categoria')
            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='disabled')

            # endregion

            # region ▶️ "Run" Button
            home_tab_footer_description_text.configure(
                text='Ferramenta de Segurança Pré-Programada')
            home_tab_footer_run_button.configure(text="Iniciar")

            # endregion

            # endregion

            # region 🔴 "Configure" Tab
            # First Container (main)
            configure_tab_first_container_first_frame_first_subframe_text_description.configure(
                text="ESCOLHA O TIPO DE OPERAÇÃO")
            configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.configure(
                values=operation_type_portuguese_options)
            configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.set(
                'Criar')
            configure_tab_first_container_title.configure(
                text_color=LIGHT_BLUE_COLOR)

            configure_tab_first_container_first_frame_second_subframe_text_description.configure(
                text="ESCOLHA UM ITEM")
            configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.configure(
                values=configure_tab_choose_an_item_portuguese_options)
            configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.set(
                'Linha de Comando')

            # Configure Tab Title
            configure_tab_first_container_title.configure(
                text=f'{configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()} '
                     f'{configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.get()}')

            # First Scrollable Frame
            configure_tab_first_container_first_scrollable_frame_first_subframe_text_description.configure(
                text="ESCOLHA O SISTEMA OPERACIONAL")

            configure_tab_first_container_first_scrollable_frame_second_subframe_text_description.configure(
                text="ESCOLHA A CATEGORIA")
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.configure(
                values=command_line_category_portuguese_options)
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.set(
                'básico')

            configure_tab_first_container_first_scrollable_frame_third_subframe_text_description.configure(
                text="ESCOLHA O TIPO DE USUÁRIO")

            configure_tab_first_container_first_scrollable_frame_second_frame_text_description.configure(
                text="ESCREVA O NOME DO COMANDO *")
            configure_tab_first_container_first_scrollable_frame_third_frame_group_text_description.configure(
                text="ESCREVA O COMANDO. USE PONTO E VÍRGULA (;) PARA PULAR UMA LINHA. *")
            configure_tab_first_container_first_scrollable_frame_fourth_frame_group_text_description.configure(
                text="ESCREVA UMA DESCRIÇÃO PARA O COMANDO (opcional)")

            configure_tab_footer_run_button.configure(
                text=f'{configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()}',
                fg_color=LIGHT_BLUE_COLOR,
                hover_color=DARK_BLUE_COLOR)

            # Second Scrollable Frame
            configure_tab_first_container_second_scrollable_frame_first_subframe_text_description.configure(
                text='TIPO'
            )
            configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.configure(
                values=cve_type_portuguese_options
            )
            configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.set(
                value='Código CVE'
            )

            configure_tab_first_container_second_scrollable_frame_second_subframe_text_description.configure(
                text='ASSOCIAR À LISTA'
            )

            configure_tab_first_container_second_scrollable_frame_third_subframe_text_description.configure(
                text='IDENTIFICAÇÃO *'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                placeholder_text='Ex: CVE-2024-1234'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_text_description.configure(
                text='ESCREVA UMA DESCRIÇÃO PARA O COMANDO'
            )

            # Footer
            configure_tab_footer_description_text.configure(
                text="Ferramenta de Segurança Pré-Programada")

            # endregion

            # region 🟡 "Info" Tab

            # region Container "Info App"
            info_tab_first_frame_group_first_info_text.configure(
                text="DESENVOLVEDOR")
            info_tab_second_frame_group_first_info_text.configure(
                text="NOME DO APP")
            info_tab_second_frame_group_first_info_text_space.configure(
                text="      ")
            info_tab_third_frame_group_first_info_text.configure(text="VERSÃO")
            info_tab_third_frame_group_first_info_text_space.configure(
                text="                ")
            # endregion

            # region Frame (Text + Button): "Contact Developer"
            info_tab_footer_info_text.configure(
                text="Automações, Upgrades ou Suporte?")
            info_tab_footer_button.configure(text="Contate o Desenvolvedor")
            # endregion

            # endregion

        case 'es':
            # region 🔵 "Home" Tab

            # region Container "Menu"
            home_tab_menu_title.configure(text=f' {APP_NAME} Ménu')
            home_tab_menu_first_button.configure(text="Línea de Comando")
            home_tab_menu_second_button.configure(text="Escáner de Puertos")
            home_tab_menu_third_button.configure(text="Vulnerabilidades CVE")
            home_tab_menu_appearance_dropdown.configure(
                values=appearance_mode_spanish_options)
            if home_tab_menu_appearance_dropdown_option == "Dark":
                home_tab_menu_appearance_dropdown.set("Oscuro")
            if home_tab_menu_appearance_dropdown_option == "Light":
                home_tab_menu_appearance_dropdown.set("Claro")
            # endregion

            # region 1️⃣ Home > "First" Container (Empty!)
            home_tab_first_container_title.configure(
                text="Operaciones de Línea de Comando")
            home_tab_first_container_scrollable_frame_first_frame_text_description.configure(
                text='TIPO DE USUARIO')
            home_tab_first_container_scrollable_frame_first_frame_second_subframe_text_description.configure(
                text='CATEGORÍA')
            home_tab_first_container_scrollable_frame_second_frame_text_description.configure(
                text='ELIJA UN COMANDO*')
            home_tab_first_container_scrollable_frame_third_frame_group_text_description.configure(
                text='LÍNEA DE COMANDO')
            home_tab_first_container_scrollable_frame_fourth_frame_group_text_description.configure(
                text='DESCRIPCIÓN DEL COMANDO')
            # endregion

            # region 2️⃣ Home > "Second" Container
            home_tab_second_container_title.configure(
                text="Escáner de Puertos")
            # Description texts
            home_tab_second_container_first_frame_group_text_description.configure(
                text='DIRECCIÓN IPV4 *')
            home_tab_second_container_first_frame_group_first_entry.configure(
                placeholder_text='Ej: 192.168.79.1')
            home_tab_second_container_first_frame_group_second_subframe_text_description.configure(
                text='USAR MI IP')
            home_tab_second_container_second_frame_group_first_subframe_text_description.configure(
                text='HILOS')
            home_tab_second_container_second_frame_group_first_subframe_first_entry.configure(
                placeholder_text='Ej: 100')
            home_tab_second_container_second_frame_group_second_subframe_text_description.configure(
                text='PUERTO DE INICIO *')
            home_tab_second_container_second_frame_group_second_subframe_first_entry.configure(
                placeholder_text='Ej: 1')
            home_tab_second_container_second_frame_group_third_subframe_text_description.configure(
                text='PUERTO DE FIN *')
            home_tab_second_container_second_frame_group_third_subframe_first_entry.configure(
                placeholder_text='Ej: 1024')

            # endregion

            # region 3️⃣ Home > "Third" Container
            home_tab_third_container_title.configure(
                text="Vulnerabilidades CVE")

            home_tab_third_container_first_frame_group_text_description.configure(
                text='URL OBJETIVO')
            home_tab_third_container_first_frame_group_first_entry.configure(
                placeholder_text='Ej: https://www.google.com/')

            # Slider description
            home_tab_third_container_second_frame_group_second_subframe_text_description.configure(
                text='LISTA')
            home_tab_third_container_second_frame_group_second_subframe_first_slider.set(
                2)
            home_tab_third_container_second_frame_group_text_description.configure(
                text='LISTA CVE CHECK')

            home_tab_third_container_third_frame_group_text_description.configure(
                text='DESCRIPCIÓN DE LA VULNERABILIDAD')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '0.0',
                'end')
            home_tab_third_container_third_frame_group_first_textbox.insert(
                '0.0',
                'Verifica todas las vulnerabilidades en una categoría')
            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='disabled')
            # endregion

            # region ▶️ "Run" Button

            home_tab_footer_description_text.configure(
                text='Herramienta de Seguridad Preprogramada')
            home_tab_footer_run_button.configure(text="Ejecutar")

            # endregion

            # endregion

            # region 🔴 "Configure" Tab
            # First Container (main)
            configure_tab_first_container_first_frame_first_subframe_text_description.configure(
                text="ELIJA EL TIPO DE OPERACIÓN")
            configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.configure(
                values=operation_type_spanish_options)
            configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.set(
                'Crear')
            configure_tab_first_container_title.configure(
                text_color=LIGHT_BLUE_COLOR)

            configure_tab_first_container_first_frame_second_subframe_text_description.configure(
                text="ELIJA UN ELEMENTO")
            configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.configure(
                values=configure_tab_choose_an_item_spanish_options)
            configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.set(
                'Línea de Comando')

            # Configure Tab Title
            configure_tab_first_container_title.configure(
                text=f'{configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()} '
                     f'{configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.get()}')

            # First Scrollable Frame
            configure_tab_first_container_first_scrollable_frame_first_subframe_text_description.configure(
                text="ELIJA EL SISTEMA OPERATIVO")

            configure_tab_first_container_first_scrollable_frame_second_subframe_text_description.configure(
                text="ELIJA LA CATEGORÍA")
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.configure(
                values=command_line_category_spanish_options)
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.set(
                'básico')

            configure_tab_first_container_first_scrollable_frame_third_subframe_text_description.configure(
                text="ELIJA EL TIPO DE USUARIO")

            configure_tab_first_container_first_scrollable_frame_second_frame_text_description.configure(
                text="ESCRIBA EL NOMBRE DEL COMANDO *")
            configure_tab_first_container_first_scrollable_frame_third_frame_group_text_description.configure(
                text="ESCRIBE EL COMANDO. UTILICE PUNTO Y COMA (;) PARA SALTAR UNA LÍNEA *")
            configure_tab_first_container_first_scrollable_frame_fourth_frame_group_text_description.configure(
                text="ESCRIBA UNA DESCRIPCIÓN PARA EL COMANDO (opcional)")

            configure_tab_footer_run_button.configure(
                text=f'{configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()}',
                fg_color=LIGHT_BLUE_COLOR,
                hover_color=DARK_BLUE_COLOR)

            configure_tab_first_container_second_scrollable_frame_first_subframe_text_description.configure(
                text='TIPO'
            )
            configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.configure(
                values=cve_type_portuguese_options,
            )
            configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.set(
                value='Código CVE'
            )

            configure_tab_first_container_second_scrollable_frame_second_subframe_text_description.configure(
                text='ASOCIAR A LA LISTA'
            )

            configure_tab_first_container_second_scrollable_frame_third_subframe_text_description.configure(
                text='IDENTIFICACIÓN *'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                placeholder_text='Ej: CVE-2024-1234'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_text_description.configure(
                text='ESCRIBA UNA DESCRIPCIÓN PARA EL COMANDO'
            )

            # Footer
            configure_tab_footer_description_text.configure(
                text="Herramienta de Seguridad Preprogramada")

            # endregion

            # region 🟡 "Info" Tab

            # region Container "Info App"
            info_tab_first_frame_group_first_info_text.configure(
                text="DESARROLLADOR")
            info_tab_second_frame_group_first_info_text.configure(
                text="NOMBRE APP")
            info_tab_second_frame_group_first_info_text_space.configure(
                text="       ")
            info_tab_third_frame_group_first_info_text.configure(
                text="VERSIÓN")
            info_tab_third_frame_group_first_info_text_space.configure(
                text="               ")
            # endregion

            # region Frame (Text + Button): "Contate o Desenvolvedor"

            info_tab_footer_info_text.configure(
                text="Automatizaciones, Actualizaciones o Soporte?")
            info_tab_footer_button.configure(text="Contacta al desarrollador")

            # endregion

            # endregion


def change_appearance_mode(appearance_mode):
    new_appearance_mode = None

    if appearance_mode in dark_name_variations:
        new_appearance_mode = "Dark"

        # region ⚫ "Dark Mode"

        APP.configure(fg_color=GRAY_90_COLOR)
        tab.configure(fg_color=GRAY_90_COLOR, bg_color=GRAY_90_COLOR)
        first_tab.configure(fg_color=GRAY_90_COLOR, bg_color=GRAY_90_COLOR)
        second_tab.configure(fg_color=GRAY_90_COLOR, bg_color=GRAY_90_COLOR)
        third_tab.configure(fg_color=GRAY_90_COLOR, bg_color=GRAY_90_COLOR)

        # region 🔵 "Home" Tab

        # region Container "Menu"
        home_tab_menu_container.configure(border_color=LIGHT_BLUE_COLOR)

        home_tab_menu_title.configure(text_color=WHITE_COLOR)

        # Mapeia e define as cores (fg e hover) dos botões do "App Menu", de acordo com o frame ativo.
        button_mapping = {
            "first": home_tab_menu_first_button,
            "second": home_tab_menu_second_button,
            "third": home_tab_menu_third_button,
        }

        for button_name, button in button_mapping.items():
            fg_color = GRAY_70_COLOR if button_name == home_tab_active_container else TRANSPARENT_COLOR
            text_color = LIGHT_RED_COLOR if button_name == "third" else GRAY_10_COLOR
            button.configure(fg_color=fg_color, text_color=text_color,
                             hover_color=GRAY_70_COLOR)

        # Appearance + Language
        home_tab_menu_appearance_dropdown.configure(
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)
        home_tab_menu_language_dropdown.configure(
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)

        # endregion

        # region 1️⃣ Home > "First" Container
        home_tab_first_container.configure(border_color=GRAY_50_COLOR)
        home_tab_first_container_horizontal_line.configure(bg=GRAY_70_COLOR)

        home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.configure(
            border_color=GRAY_45_COLOR,
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)
        home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
            fg_color=GRAY_60_COLOR,
            border_color=GRAY_45_COLOR)
        home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
            fg_color=GRAY_60_COLOR,
            border_color=GRAY_45_COLOR)
        # endregion

        # region 2️⃣ Home > "Second" Container
        home_tab_second_container.configure(border_color=GRAY_50_COLOR)
        home_tab_second_container_horizontal_line.configure(bg=GRAY_70_COLOR)
        # Entry fields
        home_tab_second_container_first_frame_group_first_entry.configure(
            border_color=GRAY_45_COLOR,
            fg_color=GRAY_60_COLOR)
        home_tab_second_container_second_frame_group_first_subframe_first_entry.configure(
            border_color=GRAY_45_COLOR,
            fg_color=GRAY_60_COLOR)
        home_tab_second_container_first_frame_group_second_subframe_first_switch.configure(
            border_color=GRAY_45_COLOR,
            fg_color=GRAY_60_COLOR,
            button_color=GRAY_20_COLOR,
            button_hover_color=WHITE_COLOR)
        home_tab_second_container_second_frame_group_second_subframe_first_entry.configure(
            border_color=GRAY_45_COLOR,
            fg_color=GRAY_60_COLOR)
        home_tab_second_container_second_frame_group_third_subframe_first_entry.configure(
            border_color=GRAY_45_COLOR,
            fg_color=GRAY_60_COLOR)
        # endregion

        # region 3️⃣ Home > "Third" Container
        home_tab_third_container.configure(border_color=GRAY_50_COLOR)
        home_tab_third_container_horizontal_line.configure(bg=GRAY_70_COLOR)
        # endregion

        # region Fields
        # Target URL (Entry)
        home_tab_third_container_first_frame_group_first_entry.configure(
            fg_color=GRAY_60_COLOR,
            border_color=GRAY_45_COLOR)
        # CVE Category (Dropdown)
        home_tab_third_container_second_frame_group_first_dropdown.configure(
            fg_color=GRAY_60_COLOR,
            border_color=GRAY_45_COLOR)
        # Type (Switch)
        home_tab_third_container_second_frame_group_second_subframe_first_slider.configure(
            fg_color=GRAY_60_COLOR,
            border_color=GRAY_45_COLOR,
            button_color=GRAY_20_COLOR,
            button_hover_color=WHITE_COLOR)
        # Combobox
        home_tab_third_container_third_frame_group_first_textbox.configure(
            fg_color=GRAY_60_COLOR,
            border_color=GRAY_45_COLOR)
        # endregion

        # ▶️ "Run" Button Container
        home_tab_footer_container.configure(border_color=GRAY_50_COLOR)

        # endregion

        # region 🔴 "Configure" Tab
        configure_tab_first_container.configure(border_color=GRAY_50_COLOR)

        # region 1️⃣ "First" Scrollable Frame
        configure_tab_first_container_first_scrollable_frame.configure(
            fg_color=GRAY_70_COLOR)
        configure_tab_first_container_second_scrollable_frame.configure(
            fg_color=GRAY_70_COLOR)
        # Second Frame | Dropdown
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry.configure(
            fg_color=GRAY_70_COLOR,
            border_color=GRAY_45_COLOR)
        # Third Frame | Dropdown
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry.configure(
            fg_color=GRAY_70_COLOR,
            border_color=GRAY_45_COLOR)
        # Fourth Frame | Dropdown
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox.configure(
            fg_color=GRAY_70_COLOR,
            border_color=GRAY_45_COLOR)
        # endregion

        # region 2️⃣ "Second" Scrollable Frame
        configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
            border_color=GRAY_45_COLOR,
            fg_color=GRAY_70_COLOR)
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_45_COLOR
        )
        # endregion

        configure_tab_footer_container.configure(border_color=GRAY_50_COLOR)

        # endregion

        # region 🟡 "Info" Tab
        info_tab_container.configure(border_color=GRAY_50_COLOR)
        # endregion

        home_tab_menu_first_button.configure(hover_color=GRAY_70_COLOR)

        # endregion

    elif appearance_mode in light_name_variations:
        new_appearance_mode = "Light"

        # region ⚪ "LIGHT MODE"

        APP.configure(fg_color=GRAY_20_COLOR)
        tab.configure(fg_color=GRAY_20_COLOR, bg_color=GRAY_20_COLOR)
        first_tab.configure(fg_color=GRAY_20_COLOR, bg_color=GRAY_20_COLOR)
        second_tab.configure(fg_color=GRAY_20_COLOR, bg_color=GRAY_20_COLOR)
        third_tab.configure(fg_color=GRAY_20_COLOR, bg_color=GRAY_20_COLOR)

        # region 🔵 "Home" Tab

        # region Container "Menu"
        home_tab_menu_container.configure(border_color=LIGHT_BLUE_COLOR)

        home_tab_menu_title.configure(text_color=GRAY_50_COLOR)

        # Maps and defines the colors (fg and hover) of the "App Menu" buttons, according to the active frame.
        button_mapping = {
            "first": home_tab_menu_first_button,
            "second": home_tab_menu_second_button,
            "third": home_tab_menu_third_button,
        }

        for button_name, button in button_mapping.items():
            fg_color = GRAY_40_COLOR if button_name == home_tab_active_container else TRANSPARENT_COLOR
            text_color = LIGHT_RED_COLOR if button_name == "third" else GRAY_55_COLOR
            button.configure(fg_color=fg_color, text_color=text_color,
                             hover_color=GRAY_40_COLOR)

        home_tab_menu_appearance_dropdown.configure(
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)
        home_tab_menu_language_dropdown.configure(
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)

        # endregion

        # region 1️⃣ Home > "First" Container
        home_tab_first_container.configure(border_color=GRAY_40_COLOR)
        home_tab_first_container_horizontal_line.configure(bg=GRAY_30_COLOR)

        home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.configure(
            border_color=GRAY_35_COLOR,
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)
        home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # endregion

        # region 2️⃣ Home > "Second" Container
        home_tab_second_container.configure(border_color=GRAY_40_COLOR)
        home_tab_second_container_horizontal_line.configure(bg=GRAY_30_COLOR)

        # Entry fields
        home_tab_second_container_first_frame_group_first_entry.configure(
            border_color=GRAY_35_COLOR,
            fg_color=WHITE_COLOR)
        home_tab_second_container_second_frame_group_first_subframe_first_entry.configure(
            border_color=GRAY_35_COLOR,
            fg_color=WHITE_COLOR)
        home_tab_second_container_first_frame_group_second_subframe_first_switch.configure(
            border_color=GRAY_35_COLOR,
            fg_color=WHITE_COLOR,
            button_color=GRAY_45_COLOR,
            button_hover_color=GRAY_55_COLOR)
        home_tab_second_container_second_frame_group_second_subframe_first_entry.configure(
            border_color=GRAY_35_COLOR,
            fg_color=WHITE_COLOR)
        home_tab_second_container_second_frame_group_third_subframe_first_entry.configure(
            border_color=GRAY_35_COLOR,
            fg_color=WHITE_COLOR)

        # endregion

        # region 3️⃣ Home > "Third" Container
        home_tab_third_container.configure(border_color=GRAY_40_COLOR)
        home_tab_third_container_horizontal_line.configure(bg=GRAY_30_COLOR)

        # Target URL (Entry)
        home_tab_third_container_first_frame_group_first_entry.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # CVE Category (Dropdown)
        home_tab_third_container_second_frame_group_first_dropdown.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # Type (Slider)
        home_tab_third_container_second_frame_group_second_subframe_first_slider.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR,
            button_color=GRAY_45_COLOR,
            button_hover_color=GRAY_55_COLOR)
        # Combobox
        home_tab_third_container_third_frame_group_first_textbox.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # endregion

        # region ▶️ Frame "Run" Button"
        home_tab_footer_container.configure(border_color=GRAY_40_COLOR)
        # endregion

        # endregion

        # region 🔴 "Configure" Tab
        configure_tab_first_container.configure(border_color=GRAY_30_COLOR)

        # region 1️⃣ "First" Scrollable Frame
        configure_tab_first_container_first_scrollable_frame.configure(
            fg_color=GRAY_30_COLOR)
        configure_tab_first_container_second_scrollable_frame.configure(
            fg_color=GRAY_30_COLOR)
        # Second Frame | Dropdown
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # Third Frame | Dropdown
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # Fourth Frame | Dropdown
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox.configure(
            fg_color=WHITE_COLOR,
            border_color=GRAY_35_COLOR)
        # endregion

        # region 2️⃣ "Second" Scrollable Frame
        configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
            border_color=GRAY_35_COLOR,
            fg_color=WHITE_COLOR)
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_35_COLOR
        )
        # endregion

        configure_tab_footer_container.configure(border_color=GRAY_30_COLOR)

        # endregion

        # region 🟡 "Info" Tab

        info_tab_container.configure(border_color=GRAY_40_COLOR)

        # endregion

        # endregion

    ctk.set_appearance_mode(new_appearance_mode)


def toggle_container_visibility(container, all_containers, chosen_container,
                                button, all_buttons):
    global home_tab_active_container

    # Checks if the target container (widget) is currently visible on the screen
    is_target_container_visible = container.winfo_ismapped()

    # Hide all containers except the target container
    for other_container in all_containers:
        if other_container != container:
            other_container.pack_forget()

    # Manage the "hover" color of the button that triggered the function
    for other_button in all_buttons:
        if other_button != button:
            other_button.configure(fg_color=TRANSPARENT_COLOR)

    # Show or hide the target container unless it is already visible
    if not is_target_container_visible:
        container.pack(side=ctk.RIGHT, padx=5, pady=0, fill=ctk.BOTH,
                       expand=True, anchor="ne")

        appearance_mode = ctk.get_appearance_mode()

        if appearance_mode == "Escuro" or appearance_mode == "Oscuro" or appearance_mode == "Dark":
            button.configure(fg_color=GRAY_70_COLOR)

        elif appearance_mode == "Claro" or appearance_mode == "Light":
            button.configure(fg_color=GRAY_40_COLOR)

        home_tab_active_container = chosen_container


def create_user_preferences():
    # 🔑 USER SETTINGS - Initial Values (Default)
    default_preferences = {
        "preference_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value": "",
        "preference_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value": "",
    }

    # Save the dictionary to the JSON file
    with open("./src/json/preferences.json", "w") as preferences_file:
        json.dump(default_preferences, preferences_file)


def get_user_preferences():
    # 🔑 Check if the JSON file exists; if not, create it
    if not os.path.exists("src/json/preferences.json"):
        create_user_preferences()

    # Try to retrieve user preferences from the JSON
    try:
        with (open("src/json/preferences.json", "r") as preferences_file):
            player_preferences = json.load(preferences_file)

            # region (GET) Values From | 1️⃣ Home > "First" Container
            home_tab_first_container_scrollable_frame_first_frame_group_first_entry = (
                player_preferences[
                    'preference_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value'])
            home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown = (
                player_preferences[
                    'preference_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value'])

            # endregion

    except FileNotFoundError:
        player_preferences = {}

    return (
        home_tab_first_container_scrollable_frame_first_frame_group_first_entry,
        home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown)


def define_command_options_in_dropdown_on_start(_=None):
    global command_type

    command_type = home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown.get()
    chosen_user_type = home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown.get()

    list_of_available_commands = check_list_of_command_names(chosen_user_type,
                                                             command_type)

    # Update the dropdown menu options
    home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.configure(
        values=list_of_available_commands)
    return list_of_available_commands


def home_tab_first_container_scrollable_frame_third_frame_group_first_textbox_reset():
    # Temporarily enables the widget for editing its value
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
        state='normal')
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
        state='normal')

    # Clears the current content of the Textbox
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.delete(
        "1.0", "end")
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.delete(
        "1.0", "end")

    # Inserts the new value into the Textbox
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.insert(
        "1.0", '')
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.insert(
        "1.0", '')

    # Disables the widget again for viewing only
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
        state='disabled')
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
        state='disabled')


def change_command_options_in_dropdown(_=None):
    global home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown_value
    # (GET) category
    home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown_value = (
        home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown.get())

    # Obtains the list of commands, sets it in the dropdown, but keeps it without any selected option.
    list_of_commands = define_command_options_in_dropdown_on_start(
        home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown_value)
    home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.configure(
        values=list_of_commands)
    home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.set(
        '')

    # clear dropdown values
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox_reset()


def change_command_line_and_description(_=None):
    new_border_color = None

    # (GET) values from the selected fields ("user type" and "choose a command") in the interface
    chosen_user_type = home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown.get()
    command_name = home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.get()

    # Adjust dropdown colors
    new_border_color = GRAY_45_COLOR if (
            home_tab_menu_appearance_dropdown.get() in
            dark_name_variations) else GRAY_35_COLOR

    home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.configure(
        border_color=new_border_color,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)

    # Retrieve the command line and description based on user_type, command_type, and command_name
    command_line, command_description = check_list_of_command_line_and_description(
        chosen_user_type, command_type, command_name)

    # Temporarily enable the widget to edit its value
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
        state='normal')
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
        state='normal')

    # Clear the current content of the Textbox
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.delete(
        "1.0", "end")
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.delete(
        "1.0", "end")

    # Insert the new value into the Textbox
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.insert(
        "1.0", command_line)
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.insert(
        "1.0", command_description)

    # Disable the widget again for viewing only
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
        state='disabled')
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
        state='disabled')


# region "Configure" Tab Functions
def change_visibility_configure_tab_first_container_scrollable_frames(_=None):
    global configure_tab_active_container

    chosen_item = configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.get()
    operation_type = configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()
    configure_tab_first_container_title.configure(
        text=f'{operation_type} {chosen_item}')

    if chosen_item in command_line_name_variations:
        configure_tab_active_container = "first"
        configure_tab_first_container_second_scrollable_frame.pack_forget()
        configure_tab_first_container_first_scrollable_frame.pack(
            fill=ctk.BOTH, expand=True, padx=10, pady=10)
    elif chosen_item in cve_vulnerabilities_name_variations:
        configure_tab_active_container = "second"
        configure_tab_first_container_first_scrollable_frame.pack_forget()
        configure_tab_first_container_second_scrollable_frame.pack(
            fill=ctk.BOTH, expand=True, padx=10, pady=10)


# endregion


def configure_tab_first_container_change_tab_title_and_button_color(
        chosen_dropdown_option, item):
    # Change Value
    configure_tab_footer_run_button.configure(
        text=f'{chosen_dropdown_option}')
    # Change Color
    if chosen_dropdown_option in delete_name_variations:
        configure_tab_footer_run_button.configure(fg_color=LIGHT_RED_COLOR,
                                                  hover_color=DARK_RED_COLOR)
    elif chosen_dropdown_option in update_name_variations:
        configure_tab_footer_run_button.configure(fg_color=LIGHT_YELLOW_COLOR,
                                                  hover_color=DARK_YELLOW_COLOR)
    else:
        configure_tab_footer_run_button.configure(fg_color=LIGHT_BLUE_COLOR,
                                                  hover_color=DARK_BLUE_COLOR)

    # Update Configure Tab "Title" and "Color"
    configure_tab_first_container_title.configure(
        text=f'{chosen_dropdown_option} '
             f'{item}')
    # Change Color
    if chosen_dropdown_option in delete_name_variations:
        configure_tab_first_container_title.configure(
            text_color=LIGHT_RED_COLOR)
    elif chosen_dropdown_option in update_name_variations:
        configure_tab_first_container_title.configure(
            text_color=LIGHT_YELLOW_COLOR)
    else:
        configure_tab_first_container_title.configure(
            text_color=LIGHT_BLUE_COLOR)


def configure_tab_footer_container_update_tab_title_and_first_button(_=None):
    # (GET) value from "operation type" Dropdown
    chosen_operation_type = configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()
    chosen_an_item = configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.get()
    chosen_type = configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.get()

    # (CREATE)
    if chosen_operation_type in create_name_variations:
        if chosen_type in cve_code_name_variations:  # CVE
            configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                state='normal'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                state='normal'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                state='normal'
            )
        elif chosen_type.upper() in list_name_variations:  # LIST
            configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                state='disabled'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                state='normal'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                state='disabled'
            )
    # (UPDATE)
    elif chosen_operation_type in update_name_variations:
        if chosen_type in cve_code_name_variations:  # CVE
            configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                state='disabled'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                state='normal'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                state='normal'
            )
        elif chosen_type.upper() in list_name_variations:  # LIST
            configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                state='disabled'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                state='disabled'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                state='disabled'
            )
    # (DELETE)
    elif chosen_operation_type in delete_name_variations:
        if chosen_type in cve_code_name_variations:  # CVE
            configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                state='disabled'
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                state='normal'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                state='disabled'
            )
        elif chosen_type.upper() in list_name_variations:  # LIST
            all_cve_categories = get_cve_vulnerability_categories(
                cve_json_path)
            configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                state='normal',
                values=all_cve_categories
            )
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                state='disabled'
            )
            configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                state='disabled'
            )

    # (UPDATE) colors (Tab Title + Button)
    configure_tab_first_container_change_tab_title_and_button_color(
        chosen_operation_type,
        chosen_an_item)


def configure_tab_change_user_type_dropdown_values(_=None):
    chosen_configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value = (
        configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown.get())

    match chosen_configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value:
        case 'Windows':
            configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown.configure(
                values=user_type_on_windows_options)
            configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown.set(
                value='user')
        case 'Linux':
            configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown.configure(
                values=user_type_on_linux_options)
            configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown.set(
                value='usr')


def home_tab_second_container_first_frame_group_get_ipv4_and_update_first_entry():
    value = home_tab_second_container_first_frame_group_second_subframe_first_switch.get()

    match value:
        case 'on':
            home_tab_second_container_first_frame_group_second_subframe_first_switch.configure(
                text='✔',
                text_color=LIGHT_GREEN_COLOR)

            home_tab_second_container_first_frame_group_first_entry.insert(0,
                                                                           string=get_ipv4())
            home_tab_second_container_first_frame_group_first_entry.configure(
                state='disabled')
        case 'off':
            home_tab_second_container_first_frame_group_second_subframe_first_switch.configure(
                text='❌',
                text_color=LIGHT_RED_COLOR)

            home_tab_second_container_first_frame_group_first_entry.configure(
                state='normal')
            home_tab_second_container_first_frame_group_first_entry.delete(0,
                                                                           "end")


def check_language():
    language = home_tab_menu_language_dropdown.get()
    return language


def get_cve_vulnerability_description_in_json():
    cve_code = home_tab_third_container_second_frame_group_first_dropdown.get()
    description = get_cve_description_by_cve_code(cve_json_path, cve_code)
    return description


def change_cve_description_on_interface(description):
    home_tab_third_container_third_frame_group_first_textbox.configure(
        state='normal')
    home_tab_third_container_third_frame_group_first_textbox.delete('0.0',
                                                                    'end')
    home_tab_third_container_third_frame_group_first_textbox.insert(
        '0.0',
        description)
    home_tab_third_container_third_frame_group_first_textbox.configure(
        state='disabled')


def get_cve_description_and_change_description_on_interface(_=None):
    slider_value = int(
        home_tab_third_container_second_frame_group_second_subframe_first_slider.get())
    language = check_language()

    match slider_value:
        case 1:  # SINGLE
            description = get_cve_vulnerability_description_in_json()
            change_cve_description_on_interface(description)

        case 2:  # LIST
            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '0.0',
                'end')

            match language:
                case 'en':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Checks for all vulnerabilities in a category')
                case 'pt':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas as vulnerabilidades em uma categoria')
                case 'es':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas las vulnerabilidades en una categoría')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='disabled')

        case 3:  # ALL

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '0.0',
                'end')

            match language:
                case 'en':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Checks all registered CVE vulnerabilities')
                case 'pt':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas as vulnerabilidades CVE cadastradas')
                case 'es':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas las vulnerabilidades CVE registradas')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='disabled')


def home_tab_third_container_second_frame_group_first_dropdown_change_vulnerability_description_to_list(
        language,
        switch_value):
    match switch_value:
        case 1:
            get_cve_description_and_change_description_on_interface()

        case 2:
            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '0.0', 'end')

            match language:
                case 'en':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Checks for all vulnerabilities in a category')

                case 'pt':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas as vulnerabilidades em uma categoria')
                case 'es':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas las vulnerabilidades en una categoría')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state="disabled")

        case 3:
            home_tab_third_container_third_frame_group_first_textbox.configure(
                state='normal')
            home_tab_third_container_third_frame_group_first_textbox.delete(
                '0.0', 'end')

            match language:
                case 'en':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Checks all registered CVE vulnerabilities')

                case 'pt':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas as vulnerabilidades CVE cadastradas')
                case 'es':
                    home_tab_third_container_third_frame_group_first_textbox.insert(
                        '0.0',
                        'Verifica todas las vulnerabilidades CVE registradas')

            home_tab_third_container_third_frame_group_first_textbox.configure(
                state="disabled")


def home_tab_third_container_second_frame_group_first_dropdown_change_vulnerability_description_to_all(
        _=None):
    language = check_language()

    home_tab_third_container_third_frame_group_first_textbox.configure(
        state="normal")
    home_tab_third_container_third_frame_group_first_textbox.delete("1.0",
                                                                    "end")

    match language:
        case 'en':
            home_tab_third_container_third_frame_group_first_textbox.insert(
                "0.0",
                'Checks all registered CVE vulnerabilities')
        case 'pt':
            home_tab_third_container_third_frame_group_first_textbox.insert(
                "0.0",
                'Verifica todas as vulnerabilidades CVE registradas')
        case 'es':
            home_tab_third_container_third_frame_group_first_textbox.insert(
                "0.0",
                'Verifica todas las vulnerabilidades CVE registradas')

    home_tab_third_container_third_frame_group_first_textbox.configure(
        state="disabled")


def home_tab_third_container_second_frame_group_first_dropdown_change_value_and_text_description(
        slider_description):
    if slider_description in single_name_variations:
        home_tab_third_container_second_frame_group_first_dropdown.configure(
            state='normal',
            values=all_cve_codes)
        home_tab_third_container_second_frame_group_first_dropdown.set(
            all_cve_codes[0])

    elif slider_description in list_name_variations:
        home_tab_third_container_second_frame_group_first_dropdown.configure(
            state='normal',
            values=all_cve_categories)
        home_tab_third_container_second_frame_group_first_dropdown.set(
            all_cve_categories[0])

        chosen_language = check_language()
        switch_value = int(
            home_tab_third_container_second_frame_group_second_subframe_first_slider.get())

        # change vulnerability description
        home_tab_third_container_second_frame_group_first_dropdown_change_vulnerability_description_to_list(
            chosen_language, switch_value)

    elif slider_description in all_name_variations:
        home_tab_third_container_second_frame_group_first_dropdown.set('')
        home_tab_third_container_second_frame_group_first_dropdown.configure(
            state='disabled')

        # change vulnerability description
        home_tab_third_container_second_frame_group_first_dropdown_change_vulnerability_description_to_all()

    home_tab_third_container_second_frame_group_text_description.configure(
        text=f'{slider_description} CVE CHECK')


def home_tab_third_container_second_frame_group_change_type_mode(_=None):
    switch_description = ''
    chosen_language = check_language()
    switch_value = int(
        home_tab_third_container_second_frame_group_second_subframe_first_slider.get())

    home_tab_third_container_second_frame_group_first_dropdown_change_vulnerability_description_to_list(
        chosen_language, switch_value)

    home_tab_third_container_second_frame_group_second_subframe_first_slider.configure(
        progress_color=LIGHT_BLUE_COLOR
    )

    home_tab_third_container_first_frame_group_first_entry.configure(
        border_color=GRAY_45_COLOR)

    for number, value in mapping_switch_values.items():
        if switch_value == number:
            if chosen_language == 'en':
                switch_description = value[0]
            elif chosen_language in ['pt', 'es']:
                switch_description = value[1]

            home_tab_third_container_second_frame_group_second_subframe_text_description.configure(
                text=switch_description)

            home_tab_third_container_second_frame_group_first_dropdown_change_value_and_text_description(
                switch_description)

            return switch_description


def configure_tab_first_container_second_scrollable_frame_change_state_of_second_subframe_dropdown(
        _=None):
    global all_cve_categories
    type = configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.get()
    chosen_operation_type = configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get()

    match type:
        case 'CVE Code':
            # (CREATE)
            if chosen_operation_type in create_name_variations:
                configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                    state='normal'
                )
                configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                    state='normal'
                )
                configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                    state='normal'
                )
            # (UPDATE)
            elif chosen_operation_type in update_name_variations:
                configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                    state='disabled'
                )
                configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                    state='normal'
                )
                configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                    state='normal'
                )
            # (DELETE)
            elif chosen_operation_type in delete_name_variations:
                configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                    state='disabled'
                )
                configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                    state='normal'
                )
                configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                    state='disabled'
                )

            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                placeholder_text='Ex: CVE-2024-1234'
            )
        case 'List':
            # (CREATE)
            if chosen_operation_type in create_name_variations:
                configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                    state='disabled'
                )
                configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                    state='normal'
                )
                configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                    state='disabled'
                )
            # (UPDATE)
            elif chosen_operation_type in update_name_variations:
                configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                    state='disabled'
                )
                configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                    state='disabled'
                )
            # (DELETE)
            elif chosen_operation_type in delete_name_variations:
                all_cve_categories = get_cve_vulnerability_categories(
                    cve_json_path)
                configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
                    state='normal',
                    values=all_cve_categories
                )
                configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                    state='disabled'
                )
                configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
                    state='disabled'
                )

            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                placeholder_text='Ex: Denial of Service'
            )


def main():
    if check_python_version():
        exit()

    # region 🌎 Global variables

    # region APP + Tabs
    global APP, \
        tab, \
        first_tab, \
        second_tab, \
        third_tab
    # endregion

    # region Input fields (for saving in JSON)
    global home_tab_footer_description_text, \
        home_tab_first_container_scrollable_frame_first_frame_group_first_entry, \
        home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown, \
        home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown, \
        home_tab_first_container_scrollable_frame_third_frame_group_first_textbox, \
        home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox
    # endregion

    # region 🔵 "Home" Tab

    # region Container "Menu"
    global home_tab_menu_container, \
        home_tab_menu_title, \
        home_tab_menu_first_button, \
        home_tab_menu_second_button, \
        home_tab_menu_third_button, \
        home_tab_menu_appearance_dropdown, \
        home_tab_menu_language_dropdown
    # endregion

    # region 1️⃣ Home > "First" Container
    global home_tab_first_container, \
        home_tab_first_container_title, \
        home_tab_second_container_title, \
        home_tab_third_container_title, \
        home_tab_first_container_horizontal_line, \
        home_tab_first_container_scrollable_frame_first_frame_text_description, \
        home_tab_first_container_scrollable_frame_first_frame_group_first_entry, \
        home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown, \
        home_tab_first_container_scrollable_frame_first_frame_second_subframe_text_description, \
        home_tab_first_container_scrollable_frame_first_frame_third_subframe_text_description, \
        home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown, \
        home_tab_first_container_scrollable_frame_second_frame_text_description, \
        home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown, \
        home_tab_first_container_scrollable_frame_third_frame_group_text_description, \
        home_tab_first_container_scrollable_frame_third_frame_group_first_textbox, \
        home_tab_first_container_scrollable_frame_fourth_frame_group_text_description, \
        home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox
    # endregion

    # region 2️⃣ Home > "Second" Container
    global home_tab_second_container, \
        home_tab_second_container_horizontal_line, \
        home_tab_second_container_first_frame_group_text_description, \
        home_tab_second_container_first_frame_group_first_entry, \
        home_tab_second_container_first_frame_group_second_subframe_text_description, \
        home_tab_second_container_first_frame_group_second_subframe_first_switch, \
        home_tab_second_container_second_frame_group_first_subframe_text_description, \
        home_tab_second_container_second_frame_group_first_subframe_first_entry, \
        home_tab_second_container_second_frame_group_second_subframe_text_description, \
        home_tab_second_container_second_frame_group_second_subframe_first_entry, \
        home_tab_second_container_second_frame_group_third_subframe_text_description, \
        home_tab_second_container_second_frame_group_third_subframe_first_entry
    # endregion

    # region 3️⃣ Home > "Third" Container
    global home_tab_third_container, \
        home_tab_third_container_horizontal_line, \
        home_tab_third_container_first_frame_group_text_description, \
        home_tab_third_container_first_frame_group_first_entry, \
        home_tab_third_container_second_frame_group_text_description, \
        home_tab_third_container_second_frame_group_first_dropdown, \
        home_tab_third_container_second_frame_group_second_subframe_text_description, \
        home_tab_third_container_second_frame_group_second_subframe_first_slider, \
        home_tab_third_container_third_frame_group_text_description, \
        home_tab_third_container_third_frame_group_first_textbox

    # endregion

    # region ▶️ "Run" Button
    global home_tab_footer_container, \
        home_tab_footer_description_text, \
        home_tab_footer_run_button
    # endregion

    # endregion

    # region 🔴 "Configure" Tab
    # Configure Tab > First Container (main)
    global configure_tab_first_container, \
        configure_tab_first_container_title, \
        configure_tab_first_container_first_frame_first_subframe_text_description, \
        configure_tab_first_container_first_frame_first_subframe_group_first_dropdown, \
        configure_tab_first_container_first_frame_second_subframe_text_description, \
        configure_tab_first_container_first_frame_second_subframe_group_second_dropdown
    # Configure Tab > "First" Scrollable Frame
    global configure_tab_first_container_first_scrollable_frame, \
        configure_tab_first_container_first_scrollable_frame_first_subframe_text_description, \
        configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown, \
        configure_tab_first_container_first_scrollable_frame_second_subframe_text_description, \
        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown, \
        configure_tab_first_container_first_scrollable_frame_third_subframe_text_description, \
        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown, \
        configure_tab_first_container_first_scrollable_frame_second_frame_text_description, \
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry, \
        configure_tab_first_container_first_scrollable_frame_third_frame_group_text_description, \
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry, \
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_text_description, \
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox
    # Configure Tab > "Second" Scrollable Frame
    global configure_tab_first_container_second_scrollable_frame, \
        configure_tab_first_container_second_scrollable_frame_first_subframe_text_description, \
        configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown, \
        configure_tab_first_container_second_scrollable_frame_second_subframe_text_description, \
        configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown, \
        configure_tab_first_container_second_scrollable_frame_third_subframe_text_description, \
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry, \
        configure_tab_first_container_second_scrollable_frame_fourth_frame_group_text_description, \
        configure_tab_first_container_second_scrollable_frame_second_frame_first_textbox, \
        configure_tab_first_container_second_scrollable_frame_third_frame_group_first_textbox, \
        configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox
    # Configure Tab > Footer Container
    global configure_tab_footer_container, \
        configure_tab_footer_run_button, \
        configure_tab_footer_description_text

    # endregion

    # region 🟡 "Info" Tab

    # region Container "Info APP"

    global info_tab_container, \
        info_tab_first_frame_group_first_info_text, \
        info_tab_second_frame_group_first_info_text, \
        info_tab_third_frame_group_first_info_text, \
        info_tab_second_frame_group_first_text_value, \
        info_tab_second_frame_group_first_info_text_space, \
        info_tab_third_frame_group_first_info_text_space

    # endregion

    # region Frame (Text + Button): "Contact Developer"
    global info_tab_footer_info_text, \
        info_tab_footer_button

    # endregion

    # endregion

    # endregion

    # 🔑 (GET) Values from User Settings, from the "Home" Tab.
    (
        preference_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value,
        preference_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value) = (

        get_user_preferences()

    )

    # region 🟢 Tabs

    # region 🟩 Initial Setup (margins and borders)

    # Creation of the 'tab' Element
    tab = ctk.CTkTabview(APP,
                         width=APP_WIDTH - 0,
                         height=APP_HEIGHT - 0,
                         fg_color=GRAY_90_COLOR,
                         border_color=LIGHT_GREEN_COLOR,
                         segmented_button_selected_color=LIGHT_BLUE_COLOR,
                         segmented_button_selected_hover_color=DARK_BLUE_COLOR, )  # Bordas laterais = 10px
    tab.pack(padx=0,
             pady=0)

    # endregion

    # region 🟩 Main Tab Names
    # Defining names for the main interface tabs
    tab_1 = 'Home'
    tab_2 = 'Configure'
    tab_3 = "Info"

    # Adding tabs to the interface
    tab.add(tab_1)
    tab.add(tab_2)
    tab.add(tab_3)

    # Variables representing the tabs
    first_tab = tab.tab(tab_1)
    second_tab = tab.tab(tab_2)
    third_tab = tab.tab(tab_3)

    # endregion

    # Define the main tab
    tab.set(tab_1)

    # endregion

    # region 🔵 "Home" Tab

    # region 🚫 "Main" Container
    # Group the Containers: "App Menu" and "Basic Commands"
    home_tab_main_container = ctk.CTkFrame(master=first_tab,
                                           corner_radius=0,
                                           fg_color=TRANSPARENT_COLOR)
    home_tab_main_container.pack(side=ctk.TOP,
                                 padx=0,
                                 pady=5,
                                 fill=ctk.BOTH,
                                 expand=True)
    # endregion

    # region 🟦 "Menu Container"

    # Frame creation
    home_tab_menu_container = ctk.CTkFrame(
        master=home_tab_main_container,
        border_width=1,
        border_color=LIGHT_BLUE_COLOR)
    home_tab_menu_container.pack(side=ctk.LEFT, fill=ctk.BOTH, padx=5, pady=0,
                                 anchor="nw")

    # Menu Title
    home_tab_menu_title = ctk.CTkLabel(master=home_tab_menu_container,
                                       text=f" {APP_NAME} Menu",
                                       text_color=WHITE_COLOR,
                                       font=SMALL_TITLE_FONT,
                                       image=APP_LOGO,
                                       compound="left")
    home_tab_menu_title.pack(pady=25)

    # First Frame
    home_tab_menu_container_first_frame = ctk.CTkFrame(
        master=home_tab_menu_container,
        fg_color=TRANSPARENT_COLOR)
    home_tab_menu_container_first_frame.pack(side=ctk.TOP, fill=ctk.X, padx=2,
                                             pady=0, anchor="nw")

    # "First" Button
    home_tab_menu_first_button = ctk.CTkButton(
        master=home_tab_menu_container_first_frame,
        corner_radius=0,
        height=50,
        border_spacing=10,
        text="Command-Line",
        fg_color=GRAY_70_COLOR,
        text_color=GRAY_10_COLOR,
        hover_color=GRAY_70_COLOR,
        font=HIGHLIGHT_FONT,
        anchor="w",
        command=lambda: toggle_container_visibility(home_tab_first_container,
                                                    [home_tab_second_container,
                                                     home_tab_third_container],
                                                    "first",
                                                    home_tab_menu_first_button,
                                                    [
                                                        home_tab_menu_second_button,
                                                        home_tab_menu_third_button])
    )
    home_tab_menu_first_button.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                    padx=0)

    # "Second" Button
    home_tab_menu_second_button = ctk.CTkButton(
        master=home_tab_menu_container_first_frame,
        corner_radius=0,
        height=50,
        border_spacing=10,
        text="Port Scanner",
        fg_color=TRANSPARENT_COLOR,
        text_color=GRAY_10_COLOR,
        hover_color=GRAY_70_COLOR,
        font=HIGHLIGHT_FONT,
        anchor="w",
        command=lambda: toggle_container_visibility(home_tab_second_container,
                                                    [home_tab_first_container,
                                                     home_tab_third_container],
                                                    "second",
                                                    home_tab_menu_second_button,
                                                    [
                                                        home_tab_menu_first_button,
                                                        home_tab_menu_third_button]
                                                    ))
    home_tab_menu_second_button.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                     padx=0)

    # "Third" Button
    home_tab_menu_third_button = ctk.CTkButton(
        master=home_tab_menu_container_first_frame,
        corner_radius=0,
        height=50,
        border_spacing=10,
        text="CVE Vulnerabilities",
        fg_color=TRANSPARENT_COLOR,
        text_color=LIGHT_RED_COLOR,
        hover_color=GRAY_70_COLOR,
        font=HIGHLIGHT_FONT,
        anchor="w",
        command=lambda: toggle_container_visibility(home_tab_third_container,
                                                    [home_tab_first_container,
                                                     home_tab_second_container],
                                                    "third",
                                                    home_tab_menu_third_button,
                                                    [
                                                        home_tab_menu_first_button,
                                                        home_tab_menu_second_button]
                                                    ))
    home_tab_menu_third_button.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                    padx=0)

    # region Appearance (🎨) + Language (🔊)

    # Frame creation
    home_tab_menu_container_appearance_and_language = ctk.CTkFrame(
        master=home_tab_menu_container,
        fg_color=TRANSPARENT_COLOR)
    home_tab_menu_container_appearance_and_language.pack(side=ctk.BOTTOM,
                                                         padx=5, pady=5,
                                                         expand=True,
                                                         fill=ctk.X,
                                                         anchor="s")

    # 🎨 Appearance Mode
    home_tab_menu_appearance_dropdown = ctk.CTkComboBox(
        master=home_tab_menu_container_appearance_and_language,
        values=appearance_mode_english_options,
        command=change_appearance_mode,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    home_tab_menu_appearance_dropdown.pack(side=ctk.LEFT, padx=5, pady=5,
                                           expand=True, fill=ctk.X, anchor="s")

    # 🌐 Language Mode
    home_tab_menu_language_dropdown = ctk.CTkComboBox(
        master=home_tab_menu_container_appearance_and_language,
        values=language_options,
        command=lambda language: change_app_language(language),
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR,
        width=55)
    home_tab_menu_language_dropdown.pack(side=ctk.LEFT, padx=5, pady=5,
                                         expand=True, fill=ctk.X, anchor="s")

    # endregion

    # endregion

    # region 1️⃣ "First" Container

    # region Frame Creation
    home_tab_first_container = ctk.CTkFrame(master=home_tab_main_container,
                                            border_width=1,
                                            border_color=GRAY_50_COLOR)
    home_tab_first_container.pack(side=ctk.RIGHT, padx=4, pady=0,
                                  fill=ctk.BOTH, expand=True, anchor="ne")

    # "First" Container Title
    home_tab_first_container_title = ctk.CTkLabel(
        master=home_tab_first_container,
        text="Command-Line Operations",
        text_color=LIGHT_BLUE_COLOR,
        font=LARGE_TITLE_FONT)
    home_tab_first_container_title.pack(padx=0, pady=20)

    # Inside the frame, a line (canvas).
    home_tab_first_container_horizontal_line = ctk.CTkCanvas(
        home_tab_first_container,
        bg=GRAY_70_COLOR,
        height=1,
        width=370,
        highlightthickness=0)
    home_tab_first_container_horizontal_line.pack(fill=ctk.X, pady=5, padx=20)
    home_tab_first_container_horizontal_line.place(x=10, y=70)

    # "Scrollable" Frame
    home_tab_first_container_scrollable_frame = ctk.CTkScrollableFrame(
        master=home_tab_first_container,
        scrollbar_button_color=LIGHT_BLUE_COLOR,
        scrollbar_button_hover_color=DARK_BLUE_COLOR)
    home_tab_first_container_scrollable_frame.pack(fill=ctk.BOTH, expand=True,
                                                   padx=11, pady=10)

    # region 🚫 Optional Spacer (below the line)
    home_tab_first_container_start_spacer = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame, text='', height=1)
    home_tab_first_container_start_spacer.pack()
    # endregion

    # endregion

    # region ⭐⭐⭐ Input Fields ⭐⭐⭐

    # region ⭐ First Element

    # Main Frame
    home_tab_first_container_scrollable_frame_first_frame = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_first_frame.pack(side=ctk.TOP,
                                                               padx=5,
                                                               pady=0,
                                                               fill=ctk.X,
                                                               expand=True)

    # First SubFrame
    home_tab_first_container_scrollable_frame_first_subframe = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame_first_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_first_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_first_container_scrollable_frame_first_frame_text_description = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame_first_subframe,
        text="USER TYPE",
        text_color=GRAY_COLOR,
        font=SMALL_FONT,
        anchor="w")
    home_tab_first_container_scrollable_frame_first_frame_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # First Dropdown "User/Root"
    home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown = ctk.CTkComboBox(
        master=home_tab_first_container_scrollable_frame_first_subframe,
        values=user_type,
        command=change_command_options_in_dropdown,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR,
        width=105)
    home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)

    # Second Sub-Frame
    home_tab_first_container_scrollable_frame_first_frame_second_subframe = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame_first_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_first_frame_second_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_first_container_scrollable_frame_first_frame_second_subframe_text_description = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame_first_frame_second_subframe,
        text="CATEGORY",
        text_color=GRAY_COLOR,
        font=SMALL_FONT,
        anchor="w")
    home_tab_first_container_scrollable_frame_first_frame_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # First Dropdown "User/Root"
    home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown = ctk.CTkComboBox(
        master=home_tab_first_container_scrollable_frame_first_frame_second_subframe,
        values=command_line_category_english_options,
        command=change_command_options_in_dropdown,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR,
        width=125)
    home_tab_first_container_scrollable_frame_first_frame_second_subframe_first_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)

    # Third Sub-Frame
    home_tab_first_container_scrollable_frame_first_frame_third_subframe = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame_first_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_first_frame_third_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_first_container_scrollable_frame_first_frame_third_subframe_text_description = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame_first_frame_third_subframe,
        text="SYSTEM",
        text_color=GRAY_COLOR,
        font=SMALL_FONT,
        anchor="w")
    home_tab_first_container_scrollable_frame_first_frame_third_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # First Entry "Operational System"
    home_tab_first_container_scrollable_frame_first_frame_group_first_entry = ctk.CTkEntry(
        master=home_tab_first_container_scrollable_frame_first_frame_third_subframe,
        text_color=GRAY_COLOR)
    home_tab_first_container_scrollable_frame_first_frame_group_first_entry.pack(
        side=ctk.RIGHT,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    home_tab_first_container_scrollable_frame_first_frame_group_first_entry.insert(
        0, operational_system)
    home_tab_first_container_scrollable_frame_first_frame_group_first_entry.configure(
        state='disabled')

    # 🔒 Insert the saved value in JSON
    if preference_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value:
        home_tab_first_container_scrollable_frame_first_frame_group_first_entry.insert(
            0,
            preference_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value)
    if preference_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value:
        home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown.set(
            preference_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value)

    # endregion

    # region ⭐ Second Element

    # Frame
    home_tab_first_container_scrollable_frame_second_frame_group = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_second_frame_group.pack(
        side=ctk.TOP, padx=5, pady=0, fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_first_container_scrollable_frame_second_frame_text_description = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame_second_frame_group,
        text="CHOOSE A COMMAND *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT,
        anchor="w")
    home_tab_first_container_scrollable_frame_second_frame_text_description.pack(
        side=ctk.TOP, fill=ctk.X, padx=5,
        pady=0)

    # First Dropdown
    home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown = ctk.CTkComboBox(
        master=home_tab_first_container_scrollable_frame_second_frame_group,
        values=[''],
        command=change_command_line_and_description,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.pack(
        side=ctk.BOTTOM, fill=ctk.X,
        expand=True, padx=5, pady=0)

    # Call the function to set the options at the beginning
    define_command_options_in_dropdown_on_start()

    # endregion

    # region ⭐ Third Element

    # Frame
    home_tab_first_container_scrollable_frame_third_frame_group = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_third_frame_group.pack(
        side=ctk.TOP, padx=5, pady=0, fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_first_container_scrollable_frame_third_frame_group_text_description = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame_third_frame_group,
        text="COMMAND LINE",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_first_container_scrollable_frame_third_frame_group_text_description.pack(
        side=ctk.TOP, fill=ctk.X, padx=5,
        pady=0)

    # Textbox
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox = ctk.CTkTextbox(
        master=home_tab_first_container_scrollable_frame_third_frame_group,
        font=COMMAND_LINE_FONT,
        text_color=LIGHT_YELLOW_COLOR,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30)
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.pack(
        side=ctk.BOTTOM, fill=ctk.X, expand=True, padx=5, pady=0)
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.insert(
        "0.0", text="")
    home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.configure(
        state="disabled")

    # endregion

    # region ⭐ Fourth Element

    # Frame
    home_tab_first_container_scrollable_frame_fourth_frame_group = ctk.CTkFrame(
        master=home_tab_first_container_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_first_container_scrollable_frame_fourth_frame_group.pack(
        side=ctk.TOP, padx=5, pady=0, fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_first_container_scrollable_frame_fourth_frame_group_text_description = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame_fourth_frame_group,
        text="COMMAND DESCRIPTION",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_first_container_scrollable_frame_fourth_frame_group_text_description.pack(
        side=ctk.TOP, fill=ctk.X, padx=5,
        pady=0)

    # Campo Text Box
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox = ctk.CTkTextbox(
        master=home_tab_first_container_scrollable_frame_fourth_frame_group,
        text_color=GRAY_COLOR,
        fg_color=GRAY_60_COLOR, border_width=2,
        border_color=GRAY_45_COLOR, height=150)
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.pack(
        side=ctk.BOTTOM, fill=ctk.X, expand=True, padx=5, pady=0)
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.insert(
        "0.0", text="")
    home_tab_first_container_scrollable_frame_fourth_frame_group_first_textbox.configure(
        state="disabled")

    # endregion

    # region 🚫 INTERNAL-END spacer (OPTIONAL)
    home_tab_first_container_scrollable_frame_fourth_frame_group_end_spacer = ctk.CTkLabel(
        master=home_tab_first_container_scrollable_frame,
        text='',
        height=1)
    home_tab_first_container_scrollable_frame_fourth_frame_group_end_spacer.pack()
    # endregion

    # endregion

    # endregion

    # region 2️⃣ "Second Container"

    # region Frame Creation
    home_tab_second_container = ctk.CTkFrame(master=home_tab_main_container,
                                             border_width=1,
                                             border_color=GRAY_50_COLOR)
    home_tab_second_container.pack(side=ctk.RIGHT, padx=4, pady=0,
                                   fill=ctk.BOTH, expand=True, anchor="ne")
    home_tab_second_container.pack_forget()  # Hide the frame

    # "Second" Container Title
    home_tab_second_container_title = ctk.CTkLabel(
        master=home_tab_second_container,
        text="Port Scanner",
        text_color=LIGHT_BLUE_COLOR,
        font=LARGE_TITLE_FONT)
    home_tab_second_container_title.pack(padx=0, pady=20)

    # Inside the frame, a line (canvas)
    home_tab_second_container_horizontal_line = ctk.CTkCanvas(
        home_tab_second_container,
        bg=GRAY_70_COLOR,
        height=1,
        width=370,
        highlightthickness=0)
    home_tab_second_container_horizontal_line.pack(fill=ctk.X, pady=5, padx=20)
    home_tab_second_container_horizontal_line.place(x=10, y=70)

    # endregion

    # region ⭐⭐⭐ Input Fields ⭐⭐⭐

    # region 🚫 Optional Spacer (below the line)
    home_tab_second_container_start_spacer = ctk.CTkLabel(
        master=home_tab_second_container,
        text='')
    home_tab_second_container_start_spacer.pack(pady=1)
    # endregion

    # "Main" Frame
    home_tab_second_container_main_frame = ctk.CTkFrame(
        master=home_tab_second_container,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_main_frame.pack(side=ctk.TOP,
                                              padx=2,
                                              pady=0,
                                              fill=ctk.X,
                                              expand=True,
                                              anchor='n')

    # region ⭐ First Element

    # Frame
    home_tab_second_container_first_frame_group = ctk.CTkFrame(
        master=home_tab_second_container_main_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_first_frame_group.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # region "First" SubFrame (IPV4 Address)
    home_tab_second_container_first_frame_group_first_subframe = ctk.CTkFrame(
        master=home_tab_second_container_first_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_first_frame_group_first_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # Text Description
    home_tab_second_container_first_frame_group_text_description = ctk.CTkLabel(
        master=home_tab_second_container_first_frame_group_first_subframe,
        text="IPV4 ADDRESS *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_second_container_first_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Entry
    home_tab_second_container_first_frame_group_first_entry = ctk.CTkEntry(
        master=home_tab_second_container_first_frame_group_first_subframe,
        placeholder_text='e.g. 192.168.79.1',
        font=COMMAND_LINE_FONT,
        text_color=LIGHT_YELLOW_COLOR,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30)
    home_tab_second_container_first_frame_group_first_entry.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)
    # endregion

    # region "Second" SubFrame (Switch: On/Off)
    home_tab_second_container_first_frame_group_second_subframe = ctk.CTkFrame(
        master=home_tab_second_container_first_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_first_frame_group_second_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        expand=False,
        fill=ctk.BOTH,
        anchor='s')

    # Text Description
    home_tab_second_container_first_frame_group_second_subframe_text_description = ctk.CTkLabel(
        master=home_tab_second_container_first_frame_group_second_subframe,
        text="USE MY IP",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_second_container_first_frame_group_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # Switch
    home_tab_second_container_first_frame_group_second_subframe_first_switch = ctk.CTkSwitch(
        master=home_tab_second_container_first_frame_group_second_subframe,
        text='❌',
        text_color=LIGHT_RED_COLOR,
        state='normal',
        onvalue='on',
        offvalue='off',
        command=home_tab_second_container_first_frame_group_get_ipv4_and_update_first_entry,
        border_width=2,
        border_color=GRAY_45_COLOR,
        fg_color=GRAY_60_COLOR,
        progress_color=LIGHT_BLUE_COLOR,
        switch_width=40,
        width=25)
    home_tab_second_container_first_frame_group_second_subframe_first_switch.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    # endregion

    # endregion

    # region ⭐ Second Element

    # Frame
    home_tab_second_container_second_frame_group = ctk.CTkFrame(
        master=home_tab_second_container_main_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_second_frame_group.pack(
        side=ctk.TOP,
        anchor='n',
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # region "First" Sub Frame
    home_tab_second_container_second_frame_group_first_subframe = ctk.CTkFrame(
        master=home_tab_second_container_second_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_second_frame_group_first_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # Text Description
    home_tab_second_container_second_frame_group_first_subframe_text_description = ctk.CTkLabel(
        master=home_tab_second_container_second_frame_group_first_subframe,
        text="THREADS",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_second_container_second_frame_group_first_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # Entry
    home_tab_second_container_second_frame_group_first_subframe_first_entry = ctk.CTkEntry(
        master=home_tab_second_container_second_frame_group_first_subframe,
        placeholder_text='e.g. 100',
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30,
        width=50)
    home_tab_second_container_second_frame_group_first_subframe_first_entry.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    # endregion

    # region "Second" Sub Frame
    home_tab_second_container_second_frame_group_second_subframe = ctk.CTkFrame(
        master=home_tab_second_container_second_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_second_frame_group_second_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # Text Description
    home_tab_second_container_second_frame_group_second_subframe_text_description = ctk.CTkLabel(
        master=home_tab_second_container_second_frame_group_second_subframe,
        text="START PORT *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_second_container_second_frame_group_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # Entry
    home_tab_second_container_second_frame_group_second_subframe_first_entry = ctk.CTkEntry(
        master=home_tab_second_container_second_frame_group_second_subframe,
        placeholder_text='e.g. 1',
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30,
        width=50)
    home_tab_second_container_second_frame_group_second_subframe_first_entry.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    # endregion

    # region "Third" Sub Frame
    home_tab_second_container_second_frame_group_third_subframe = ctk.CTkFrame(
        master=home_tab_second_container_second_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_second_container_second_frame_group_third_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # Text Description
    home_tab_second_container_second_frame_group_third_subframe_text_description = ctk.CTkLabel(
        master=home_tab_second_container_second_frame_group_third_subframe,
        text="END PORT *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_second_container_second_frame_group_third_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # Entry
    home_tab_second_container_second_frame_group_third_subframe_first_entry = ctk.CTkEntry(
        master=home_tab_second_container_second_frame_group_third_subframe,
        placeholder_text='e.g. 1024',
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30,
        width=50)
    home_tab_second_container_second_frame_group_third_subframe_first_entry.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    # endregion

    # endregion

    # region 🚫 Optional Spacer (below the line)
    home_tab_second_container_second_frame_group_end_spacer = ctk.CTkLabel(
        master=home_tab_second_container,
        text='', height=160)
    home_tab_second_container_second_frame_group_end_spacer.pack()
    # endregion

    # endregion

    # endregion

    # region 3️⃣ "Third Container"

    # region Frame Creation
    home_tab_third_container = ctk.CTkFrame(master=home_tab_main_container,
                                            border_width=1,
                                            border_color=GRAY_50_COLOR)
    home_tab_third_container.pack(side=ctk.RIGHT, padx=4, pady=0,
                                  fill=ctk.BOTH, expand=True, anchor="ne")
    home_tab_third_container.pack_forget()  # Oculta o frame

    # "Third" Container Title
    home_tab_third_container_title = ctk.CTkLabel(
        master=home_tab_third_container,
        text="CVE Vulnerabilities",
        text_color=LIGHT_RED_COLOR,
        font=LARGE_TITLE_FONT)
    home_tab_third_container_title.pack(padx=0, pady=20)

    # Inside the frame, a line (canvas)
    home_tab_third_container_horizontal_line = ctk.CTkCanvas(
        home_tab_third_container,
        bg=GRAY_70_COLOR,
        height=1,
        width=370,
        highlightthickness=0)
    home_tab_third_container_horizontal_line.pack(fill=ctk.X, pady=5, padx=20)
    home_tab_third_container_horizontal_line.place(x=10, y=70)

    # endregion

    # region ⭐⭐⭐ Input Fields ⭐⭐⭐

    # region 🚫 Optional Spacer (below the line)
    home_tab_third_container_start_spacer = ctk.CTkLabel(
        master=home_tab_third_container, text='')
    home_tab_third_container_start_spacer.pack(pady=1)
    # endregion

    # "Main" Frame
    home_tab_third_container_main_frame = ctk.CTkFrame(
        master=home_tab_third_container,
        fg_color=TRANSPARENT_COLOR)
    home_tab_third_container_main_frame.pack(side=ctk.TOP,
                                             padx=2,
                                             pady=0,
                                             fill=ctk.X,
                                             expand=True,
                                             anchor='n')

    # region ⭐ First Element

    # Frame
    home_tab_third_container_first_frame_group = ctk.CTkFrame(
        master=home_tab_third_container_main_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_third_container_first_frame_group.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # Text Description
    home_tab_third_container_first_frame_group_text_description = ctk.CTkLabel(
        master=home_tab_third_container_first_frame_group,
        text="TARGET URL *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_third_container_first_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Entry
    home_tab_third_container_first_frame_group_first_entry = ctk.CTkEntry(
        master=home_tab_third_container_first_frame_group,
        placeholder_text='e.g. https://www.google.com/',
        font=COMMAND_LINE_FONT,
        text_color=LIGHT_YELLOW_COLOR,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30)
    home_tab_third_container_first_frame_group_first_entry.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # endregion

    # region ⭐ Second Element

    # Frame
    home_tab_third_container_second_frame_group = ctk.CTkFrame(
        master=home_tab_third_container_main_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_third_container_second_frame_group.pack(
        side=ctk.TOP,
        anchor='n',
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # region "First" SubFrame (Dropdown CVE Category)
    home_tab_third_container_second_frame_group_first_subframe = ctk.CTkFrame(
        master=home_tab_third_container_second_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_third_container_second_frame_group_first_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True,
        anchor='n')

    # Text Description
    home_tab_third_container_second_frame_group_text_description = ctk.CTkLabel(
        master=home_tab_third_container_second_frame_group_first_subframe,
        text="LIST CVE CHECK",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_third_container_second_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # Combobox/ Dropdown
    home_tab_third_container_second_frame_group_first_dropdown = ctk.CTkComboBox(
        master=home_tab_third_container_second_frame_group_first_subframe,
        values=all_cve_categories,
        command=get_cve_description_and_change_description_on_interface,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR,
        height=30)
    home_tab_third_container_second_frame_group_first_dropdown.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    # endregion

    # region "Second" SubFrame (Slider: Single/List/All)
    home_tab_third_container_second_frame_group_second_subframe = ctk.CTkFrame(
        master=home_tab_third_container_second_frame_group,
        fg_color=TRANSPARENT_COLOR)
    home_tab_third_container_second_frame_group_second_subframe.pack(
        side=ctk.LEFT,
        padx=5,
        pady=0,
        expand=False,
        fill=ctk.BOTH,
        anchor='s')

    # Text Description
    home_tab_third_container_second_frame_group_second_subframe_text_description = ctk.CTkLabel(
        master=home_tab_third_container_second_frame_group_second_subframe,
        text="LIST",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    home_tab_third_container_second_frame_group_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=0,
        pady=0)

    # Slider
    home_tab_third_container_second_frame_group_second_subframe_first_slider = ctk.CTkSlider(
        master=home_tab_third_container_second_frame_group_second_subframe,
        from_=1,
        to=3,
        number_of_steps=2,
        command=home_tab_third_container_second_frame_group_change_type_mode,
        border_width=2,
        border_color=GRAY_45_COLOR,
        fg_color=GRAY_60_COLOR,
        progress_color=LIGHT_BLUE_COLOR,
        button_color=GRAY_20_COLOR,
        button_hover_color=WHITE_COLOR,
        width=50,
        height=19)
    home_tab_third_container_second_frame_group_second_subframe_first_slider.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=0,
        pady=0)
    # endregion

    # endregion

    # region ⭐ Third Element

    # Frame
    home_tab_third_container_third_frame_group = ctk.CTkFrame(
        master=home_tab_third_container_main_frame,
        fg_color=TRANSPARENT_COLOR)
    home_tab_third_container_third_frame_group.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    home_tab_third_container_third_frame_group_text_description = ctk.CTkLabel(
        master=home_tab_third_container_third_frame_group,
        text="VULNERABILITY DESCRIPTION",
        text_color=GRAY_COLOR,
        font=SMALL_FONT,
        anchor="w")
    home_tab_third_container_third_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Campo Textbox
    home_tab_third_container_third_frame_group_first_textbox = ctk.CTkTextbox(
        master=home_tab_third_container_third_frame_group,
        text_color=GRAY_COLOR,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=100)
    home_tab_third_container_third_frame_group_first_textbox.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)
    home_tab_third_container_third_frame_group_first_textbox.insert(
        "0.0",
        text="Checks for all vulnerabilities in a category")
    home_tab_third_container_third_frame_group_first_textbox.configure(
        state="disabled")

    # endregion

    # region 🚫 Optional Spacer (below the line)
    home_tab_third_container_second_frame_group_end_spacer = ctk.CTkLabel(
        master=home_tab_third_container,
        text='', height=35)
    home_tab_third_container_second_frame_group_end_spacer.pack()

    # endregion

    # endregion

    # endregion

    # region 🟦 "Footer Container"

    # Container ▶️ "Run" Button
    home_tab_footer_container = ctk.CTkFrame(master=first_tab,
                                             border_width=1,
                                             border_color=GRAY_50_COLOR)
    home_tab_footer_container.pack(side=ctk.BOTTOM,
                                   padx=5,
                                   ipady=4,
                                   pady=5,
                                   fill=ctk.X,
                                   anchor="s")

    # TEXT: Description (footer)
    home_tab_footer_description_text = ctk.CTkLabel(
        master=home_tab_footer_container,
        text='Pre-Programmed Security Tool',
        text_color=GRAY_COLOR)
    home_tab_footer_description_text.pack(side=ctk.LEFT, padx=15, pady=5)

    # "Run" Button
    home_tab_footer_run_button = ctk.CTkButton(
        master=home_tab_footer_container,
        text="Run",
        font=HIGHLIGHT_FONT,
        fg_color=LIGHT_GREEN_COLOR,
        hover_color=DARK_GREEN_COLOR,
        height=35,
        width=70,
        command=home_tab_run_button_handler)
    home_tab_footer_run_button.pack(side=ctk.RIGHT, padx=(5, 10), pady=5)

    # endregion

    # endregion

    # region 🟣 "Configure" Tab

    # region 🚫 "Main" Container
    # Group the Containers: "App Menu" and "Basic Commands"
    configure_tab_main_container = ctk.CTkFrame(master=second_tab,
                                                corner_radius=0,
                                                fg_color=TRANSPARENT_COLOR)
    configure_tab_main_container.pack(side=ctk.TOP, padx=0, pady=0,
                                      fill=ctk.BOTH, expand=True)
    # endregion

    # region 1️⃣ "First" Container

    # region Frame Creation
    configure_tab_first_container = ctk.CTkFrame(
        master=configure_tab_main_container,
        border_width=1,
        border_color=GRAY_50_COLOR)
    configure_tab_first_container.pack(side=ctk.TOP, padx=5, pady=5,
                                       fill=ctk.BOTH, expand=True, anchor="ne")

    # "First" Container Title
    configure_tab_first_container_title = ctk.CTkLabel(
        master=configure_tab_first_container,
        text='Create Command-Line',
        text_color=LIGHT_BLUE_COLOR,
        font=LARGE_TITLE_FONT)
    configure_tab_first_container_title.pack(padx=0, pady=20)

    # region Main Frame Options

    # "Main" Frame
    configure_tab_first_container_main_frame = ctk.CTkFrame(
        master=configure_tab_first_container,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_main_frame.pack(side=ctk.TOP,
                                                  padx=2,
                                                  pady=0,
                                                  fill=ctk.X,
                                                  expand=True,
                                                  anchor='n')

    # "First" Frame
    configure_tab_first_container_first_frame = ctk.CTkFrame(
        master=configure_tab_first_container_main_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_frame.pack(side=ctk.TOP,
                                                   padx=5,
                                                   pady=0,
                                                   fill=ctk.X,
                                                   expand=True,
                                                   anchor='n')

    # "First" SubFrame
    configure_tab_first_container_first_frame_first_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_first_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_frame_first_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_frame_first_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_frame_first_subframe,
        text="CHOOSE OPERATION TYPE",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_frame_first_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # First Dropdown "Operational Type"
    configure_tab_first_container_first_frame_first_subframe_group_first_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_first_frame_first_subframe,
        values=operation_type_english_options,
        command=configure_tab_footer_container_update_tab_title_and_first_button,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # Second SubFrame
    configure_tab_first_container_first_frame_second_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_first_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_frame_second_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_frame_second_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_frame_second_subframe,
        text="CHOOSE AN ITEM",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_frame_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Second Dropdown "Type"
    configure_tab_first_container_first_frame_second_subframe_group_second_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_first_frame_second_subframe,
        values=configure_tab_choose_an_item_english_options,
        command=change_visibility_configure_tab_first_container_scrollable_frames,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    configure_tab_first_container_first_frame_second_subframe_group_second_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)
    # endregion

    # endregion

    # region ⭐⭐⭐ First Scrollable Frame | Input Fields ⭐⭐⭐

    # First "Scrollable" Frame
    configure_tab_first_container_first_scrollable_frame = ctk.CTkScrollableFrame(
        master=configure_tab_first_container_main_frame,
        scrollbar_button_color=LIGHT_BLUE_COLOR,
        scrollbar_button_hover_color=DARK_BLUE_COLOR,
        height=220,
        fg_color=GRAY_70_COLOR)
    configure_tab_first_container_first_scrollable_frame.pack(
        fill=ctk.BOTH,
        expand=True,
        padx=10,
        pady=10)

    # region ⭐ First Element

    # First Master Frame
    configure_tab_first_container_first_scrollable_frame_first_master_frame = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_first_master_frame.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # First SubFrame
    configure_tab_first_container_first_scrollable_frame_first_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame_first_master_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_first_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_scrollable_frame_first_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame_first_subframe,
        text="CHOOSE OPERATING SYSTEM",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_scrollable_frame_first_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # First Dropdown "Operational System" (Windows, Linux)
    configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_first_scrollable_frame_first_subframe,
        values=operational_system_options,
        command=configure_tab_change_user_type_dropdown_values,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # Second SubFrame
    configure_tab_first_container_first_scrollable_frame_second_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame_first_master_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_second_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_scrollable_frame_second_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame_second_subframe,
        text="CHOOSE CATEGORY",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_scrollable_frame_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Second Dropdown "Category" (Basic, Advanced, CVE Vulnerabilities)
    configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_first_scrollable_frame_second_subframe,
        values=command_line_category_english_options,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # Third SubFrame
    configure_tab_first_container_first_scrollable_frame_third_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame_first_master_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_third_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_scrollable_frame_third_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame_third_subframe,
        text="CHOOSE USER TYPE",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_scrollable_frame_third_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Third Dropdown "User Type" (Basic, Advanced, CVE Vulnerabilities)
    configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_first_scrollable_frame_third_subframe,
        values=user_type_on_windows_options,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # endregion

    # region ⭐ Second Element

    # Frame
    configure_tab_first_container_first_scrollable_frame_second_frame_group = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_second_frame_group.pack(
        side=ctk.TOP, padx=5, pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_scrollable_frame_second_frame_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame_second_frame_group,
        text="WRITE THE COMMAND NAME *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT,
        anchor="w")
    configure_tab_first_container_first_scrollable_frame_second_frame_text_description.pack(
        side=ctk.TOP, fill=ctk.X,
        padx=5,
        pady=0)

    # First Entry
    configure_tab_first_container_first_scrollable_frame_second_frame_first_entry = ctk.CTkEntry(
        master=configure_tab_first_container_first_scrollable_frame_second_frame_group,
        placeholder_text='e.g. Network Configuration Information',
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30)
    configure_tab_first_container_first_scrollable_frame_second_frame_first_entry.pack(
        side=ctk.BOTTOM, fill=ctk.X, expand=True, padx=5, pady=0)

    # endregion

    # region ⭐ Third Element

    # Frame
    configure_tab_first_container_first_scrollable_frame_third_frame_group = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_third_frame_group.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_scrollable_frame_third_frame_group_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame_third_frame_group,
        text="WRITE THE COMMAND. USE SIMICOLON (;) TO SKIP A LINE. *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_scrollable_frame_third_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # First Entry
    configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry = ctk.CTkEntry(
        master=configure_tab_first_container_first_scrollable_frame_third_frame_group,
        placeholder_text='e.g. ipconfig',
        font=COMMAND_LINE_FONT,
        text_color=LIGHT_YELLOW_COLOR,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=30)
    configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry.pack(
        side=ctk.BOTTOM, fill=ctk.X, expand=True, padx=5, pady=0)

    # endregion

    # region ⭐ Fourth Element

    # Frame
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group = ctk.CTkFrame(
        master=configure_tab_first_container_first_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame_fourth_frame_group,
        text="WRITE A DESCRIPTION FOR THE COMMAND (optional)",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Campo Text Box
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox = ctk.CTkTextbox(
        master=configure_tab_first_container_first_scrollable_frame_fourth_frame_group,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=150)
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox.insert(
        "0.0",
        text="")

    # endregion

    # region 🚫 INTERNAL-END spacer (OPTIONAL)
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_end_spacer = ctk.CTkLabel(
        master=configure_tab_first_container_first_scrollable_frame,
        text='',
        height=1)
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_end_spacer.pack()
    # endregion

    # endregion

    # region ⭐⭐⭐ Second Scrollable Frame | Input Fields ⭐⭐⭐

    # Second "Scrollable" Frame
    configure_tab_first_container_second_scrollable_frame = ctk.CTkScrollableFrame(
        master=configure_tab_first_container_main_frame,
        scrollbar_button_color=LIGHT_BLUE_COLOR,
        scrollbar_button_hover_color=DARK_BLUE_COLOR,
        height=220,
        fg_color=GRAY_70_COLOR)
    configure_tab_first_container_second_scrollable_frame.pack(fill=ctk.BOTH,
                                                               expand=True,
                                                               padx=10,
                                                               pady=10)
    configure_tab_first_container_second_scrollable_frame.pack_forget()

    # region ⭐ First Element

    # First Master Frame
    configure_tab_first_container_second_scrollable_frame_first_master_frame = ctk.CTkFrame(
        master=configure_tab_first_container_second_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_second_scrollable_frame_first_master_frame.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # First SubFrame
    configure_tab_first_container_second_scrollable_frame_first_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_second_scrollable_frame_first_master_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_second_scrollable_frame_first_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_second_scrollable_frame_first_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_second_scrollable_frame_first_subframe,
        text="TYPE",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_second_scrollable_frame_first_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # First Dropdown "Operational System" (Windows, Linux)
    configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_second_scrollable_frame_first_subframe,
        values=cve_type_english_options,
        command=configure_tab_first_container_second_scrollable_frame_change_state_of_second_subframe_dropdown,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR,
        width=60)
    configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # Second SubFrame
    configure_tab_first_container_second_scrollable_frame_second_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_second_scrollable_frame_first_master_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_second_scrollable_frame_second_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_second_scrollable_frame_second_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_second_scrollable_frame_second_subframe,
        text="ASSOCIATE TO LIST",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_second_scrollable_frame_second_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Second Dropdown "Category" (Basic, Advanced, CVE Vulnerabilities)
    configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown = ctk.CTkComboBox(
        master=configure_tab_first_container_second_scrollable_frame_second_subframe,
        values=all_cve_categories,
        button_color=LIGHT_BLUE_COLOR,
        button_hover_color=DARK_BLUE_COLOR)
    configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.pack(
        side=ctk.RIGHT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # Third SubFrame
    configure_tab_first_container_second_scrollable_frame_third_subframe = ctk.CTkFrame(
        master=configure_tab_first_container_second_scrollable_frame_first_master_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_second_scrollable_frame_third_subframe.pack(
        side=ctk.LEFT,
        padx=0,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_second_scrollable_frame_third_subframe_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_second_scrollable_frame_third_subframe,
        text="IDENTIFICATION *",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_second_scrollable_frame_third_subframe_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Entry
    configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry = ctk.CTkEntry(
        master=configure_tab_first_container_second_scrollable_frame_third_subframe,
        placeholder_text='e.g. CVE-2024-1234')
    configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.pack(
        side=ctk.LEFT,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)

    # endregion

    # region ⭐ Fourth Element

    # Frame
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group = ctk.CTkFrame(
        master=configure_tab_first_container_second_scrollable_frame,
        fg_color=TRANSPARENT_COLOR)
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group.pack(
        side=ctk.TOP,
        padx=5,
        pady=0,
        fill=ctk.X,
        expand=True)

    # Text Description
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_text_description = ctk.CTkLabel(
        master=configure_tab_first_container_second_scrollable_frame_fourth_frame_group,
        text="WRITE A DESCRIPTION FOR THE COMMAND",
        text_color=GRAY_COLOR,
        font=SMALL_FONT, anchor="w")
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_text_description.pack(
        side=ctk.TOP,
        fill=ctk.X,
        padx=5,
        pady=0)

    # Campo Textbox
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox = ctk.CTkTextbox(
        master=configure_tab_first_container_second_scrollable_frame_fourth_frame_group,
        fg_color=GRAY_60_COLOR,
        border_width=2,
        border_color=GRAY_45_COLOR,
        height=150)
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.pack(
        side=ctk.BOTTOM,
        fill=ctk.X,
        expand=True,
        padx=5,
        pady=0)
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.insert(
        "0.0",
        text="")

    # endregion

    # region 🚫 INTERNAL-END spacer (OPTIONAL)
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_end_spacer = ctk.CTkLabel(
        master=configure_tab_first_container_second_scrollable_frame,
        text='',
        height=1)
    configure_tab_first_container_second_scrollable_frame_fourth_frame_group_end_spacer.pack()
    # endregion

    # endregion

    # endregion

    # region 🟦 "Footer Container"

    # Container ▶️ "Create" Button
    configure_tab_footer_container = ctk.CTkFrame(
        master=configure_tab_main_container,
        border_width=1,
        border_color=GRAY_50_COLOR)
    configure_tab_footer_container.pack(side=ctk.BOTTOM,
                                        padx=5,
                                        ipady=4,
                                        pady=5,
                                        fill=ctk.X,
                                        expand=False,
                                        anchor="n")

    # TEXT: Description (footer)
    configure_tab_footer_description_text = ctk.CTkLabel(
        master=configure_tab_footer_container,
        text='Pre-Programmed Security Tool',
        text_color=GRAY_COLOR)
    configure_tab_footer_description_text.pack(side=ctk.LEFT, padx=15, pady=5)

    # "Create" Button
    configure_tab_footer_run_button = ctk.CTkButton(
        master=configure_tab_footer_container,
        text="Create",
        font=HIGHLIGHT_FONT,
        fg_color=LIGHT_BLUE_COLOR,
        hover_color=DARK_BLUE_COLOR,
        height=35,
        width=70,
        command=configure_tab_create_button_handler)
    configure_tab_footer_run_button.pack(side=ctk.RIGHT, padx=(5, 10), pady=5)

    # endregion

    # endregion

    # region  🟡 "Info" Tab

    # region 🟨 Frame of Frames (smaller groups)
    info_tab_container = ctk.CTkFrame(master=third_tab,
                                      border_width=1,
                                      border_color=GRAY_50_COLOR)
    info_tab_container.pack(side=ctk.TOP,
                            padx=5,
                            pady=5,
                            fill=ctk.X,
                            expand=True,
                            anchor="n")
    # endregion

    # region 🟨 First group

    # FRAME: Desenvolvedor

    info_tab_first_frame_group = ctk.CTkFrame(master=info_tab_container,
                                              fg_color=TRANSPARENT_COLOR)
    info_tab_first_frame_group.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                    anchor="n", pady=2, padx=2)

    info_tab_first_frame_group_first_info_text = ctk.CTkLabel(
        master=info_tab_first_frame_group, text="DEVELOPER",
        text_color=GRAY_COLOR, font=SMALL_FONT)
    info_tab_first_frame_group_first_info_text.pack(side=ctk.LEFT, fill=ctk.X,
                                                    anchor='w', expand=False,
                                                    ipadx=20)

    info_tab_first_frame_group_first_text_value = ctk.CTkLabel(
        master=info_tab_first_frame_group, text=DEVELOPER_NAME,
        text_color=LIGHT_BLUE_COLOR,
        font=HIGHLIGHT_FONT)
    info_tab_first_frame_group_first_text_value.pack(side=ctk.RIGHT,
                                                     anchor='w', expand=True,
                                                     ipadx=20)

    # endregion

    # region 🟨 Second group

    # FRAME: App Name

    info_tab_second_frame_group = ctk.CTkFrame(master=info_tab_container,
                                               fg_color=TRANSPARENT_COLOR)
    info_tab_second_frame_group.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                     anchor="n", padx=2)

    info_tab_second_frame_group_first_info_text = ctk.CTkLabel(
        master=info_tab_second_frame_group, text="APP NAME",
        text_color=GRAY_COLOR,
        font=SMALL_FONT)
    info_tab_second_frame_group_first_info_text.pack(side=ctk.LEFT, fill=ctk.X,
                                                     anchor='w', expand=False,
                                                     ipadx=20)

    info_tab_second_frame_group_first_info_text_space = ctk.CTkLabel(
        master=info_tab_second_frame_group, text='   ',
        text_color=GRAY_COLOR, font=SMALL_FONT)
    info_tab_second_frame_group_first_info_text_space.pack(side=ctk.LEFT,
                                                           fill=ctk.X,
                                                           anchor='w',
                                                           expand=False)

    info_tab_second_frame_group_first_text_value = ctk.CTkLabel(
        master=info_tab_second_frame_group, text=APP_NAME,
        text_color=LIGHT_BLUE_COLOR,
        font=HIGHLIGHT_FONT)
    info_tab_second_frame_group_first_text_value.pack(side=ctk.RIGHT,
                                                      anchor='w', expand=True,
                                                      ipadx=20)

    # endregion

    # region 🟨 Third group

    # FRAME: Version

    info_tab_third_frame_group = ctk.CTkFrame(master=info_tab_container,
                                              fg_color=TRANSPARENT_COLOR)
    info_tab_third_frame_group.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                    anchor="n", pady=2, padx=2)

    info_tab_third_frame_group_first_info_text = ctk.CTkLabel(
        master=info_tab_third_frame_group, text="VERSION",
        text_color=GRAY_COLOR,
        font=SMALL_FONT)
    info_tab_third_frame_group_first_info_text.pack(side=ctk.LEFT, fill=ctk.X,
                                                    anchor='w', expand=False,
                                                    ipadx=20)

    info_tab_third_frame_group_first_info_text_space = ctk.CTkLabel(
        master=info_tab_third_frame_group, text='      ',
        text_color=GRAY_COLOR, font=SMALL_FONT)
    info_tab_third_frame_group_first_info_text_space.pack(side=ctk.LEFT,
                                                          fill=ctk.X,
                                                          anchor='w',
                                                          expand=False)

    info_tab_third_frame_group_first_text_value = ctk.CTkLabel(
        master=info_tab_third_frame_group,
        text=APP_VERSION,
        text_color=LIGHT_RED_COLOR,
        font=HIGHLIGHT_FONT)
    info_tab_third_frame_group_first_text_value.pack(side=ctk.RIGHT,
                                                     anchor='w', expand=True,
                                                     ipadx=20)

    # endregion

    # region 🚫 Optional Spacer
    info_tab_third_frame_group_end_spacer = ctk.CTkLabel(master=third_tab,
                                                         text='')
    info_tab_third_frame_group_end_spacer.pack(expand=True, fill=ctk.Y)
    # endregion

    # region 🟨 FOOTER (Text + action button)
    # Info text
    info_tab_footer_info_text = ctk.CTkLabel(master=third_tab,
                                             text="Automations, Upgrades or Support?",
                                             text_color=GRAY_COLOR,
                                             font=MEDIUM_FONT)
    info_tab_footer_info_text.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                   anchor="s")

    # "Contact" Button
    info_tab_footer_button = ctk.CTkButton(master=third_tab,
                                           text="Contact Developer",
                                           command=open_profile,
                                           height=35,
                                           fg_color=LIGHT_BLUE_COLOR,
                                           hover_color=DARK_BLUE_COLOR)
    info_tab_footer_button.pack(side=ctk.BOTTOM, fill=ctk.X, padx=5, pady=5)
    # endregion

    # endregion

    APP.mainloop()


def change_dropdown_border_color(dropdown_name, decision_flag):
    if decision_flag:
        dropdown_name.configure(
            border_color=GRAY_45_COLOR,
            button_color=LIGHT_BLUE_COLOR,
            button_hover_color=DARK_BLUE_COLOR)
    elif not decision_flag:
        dropdown_name.configure(
            border_color=LIGHT_RED_COLOR,
            button_color=LIGHT_RED_COLOR,
            button_hover_color=DARK_RED_COLOR)


def home_tab_first_container_get_values_and_update_json():
    """Goal: (GET) Values in first tab"""
    first_container_chosen_command = None

    if home_tab_active_container == "first":

        # region (GET) Values

        chosen_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value = (
            home_tab_first_container_scrollable_frame_first_frame_group_first_entry.get())
        chosen_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value = (
            home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown.get())

        chosen_home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown_value = (
            home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.get())

        chosen_home_tab_first_container_scrollable_frame_third_frame_group_first_textbox_value = (
            home_tab_first_container_scrollable_frame_third_frame_group_first_textbox.get(
                "1.0", "end-1c"))

        # endregion

        if chosen_home_tab_first_container_scrollable_frame_third_frame_group_first_textbox_value:
            first_container_chosen_command = (
                chosen_home_tab_first_container_scrollable_frame_third_frame_group_first_textbox_value)

        # region (UPDATE) JSON

        try:
            with open("src/json/preferences.json", "r") as preferences_file:
                player_preferences = json.load(preferences_file)
        except FileNotFoundError:
            player_preferences = {}

        player_preferences[
            'preference_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value'] = (
            chosen_home_tab_first_container_scrollable_frame_first_frame_group_first_entry_value)
        player_preferences[
            'preference_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value'] = (
            chosen_home_tab_first_container_scrollable_frame_first_frame_group_first_dropdown_value)

        try:
            with open("./src/json/preferences.json", "w") as preferences_file:
                json.dump(player_preferences, preferences_file)
        except Exception as e:
            print(f"Erro ao escrever no arquivo JSON: {e}")

        # endregion

        return first_container_chosen_command


def home_tab_second_container_get_values():
    # IPv4 adress
    home_tab_second_container_first_frame_group_first_entry_value = (
        home_tab_second_container_first_frame_group_first_entry.get())
    # Threads
    home_tab_second_container_second_frame_group_first_subframe_first_entry_value = (
        home_tab_second_container_second_frame_group_first_subframe_first_entry.get())
    # Start port
    home_tab_second_container_second_frame_group_second_subframe_first_entry_value = (
        home_tab_second_container_second_frame_group_second_subframe_first_entry.get())
    # End port
    home_tab_second_container_second_frame_group_third_subframe_first_entry_value = (
        home_tab_second_container_second_frame_group_third_subframe_first_entry.get())

    return (home_tab_second_container_first_frame_group_first_entry_value,
            home_tab_second_container_second_frame_group_first_subframe_first_entry_value,
            home_tab_second_container_second_frame_group_second_subframe_first_entry_value,
            home_tab_second_container_second_frame_group_third_subframe_first_entry_value)


def home_tab_second_container_check_required_fields_are_filled(first_entry,
                                                               third_entry,
                                                               fourth_entry):
    if first_entry and third_entry and fourth_entry:
        return True


def home_tab_second_container_check_which_required_fields_were_not_filled_in(
        first_entry,
        third_entry,
        fourth_entry):
    # identify which fields were not filled in
    not_filled_entries = []

    if not first_entry:
        not_filled_entries.append('first')
    if not third_entry:
        not_filled_entries.append('third')
    if not fourth_entry:
        not_filled_entries.append('fourth')

    return not_filled_entries


def identifying_appearance_mode():
    appearance_mode = home_tab_menu_appearance_dropdown.get()
    return appearance_mode


def home_tab_second_container_change_color_of_unfilled_required_fields(
        chosen_appearance_mode, unfilled_widget):
    if chosen_appearance_mode in dark_name_variations:
        unfilled_widget.configure(border_color=GRAY_45_COLOR)
    elif chosen_appearance_mode in light_name_variations:
        unfilled_widget.configure(border_color=GRAY_35_COLOR)


def home_tab_run_button_handler():
    dropdown_name = None
    command_executed = False

    if home_tab_active_container == "first":

        # region (GET) Values
        dropdown_name = home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown
        chosen_command = home_tab_first_container_get_values_and_update_json()
        # endregion

        # region (EXECUTE) Function
        if chosen_command:
            # 🚀🚀🚀 Inicialize automation 🚀🚀🚀
            run(home_tab_active_container, chosen_command,
                command_line_interface)
            command_executed = True
        else:
            command_executed = False
            change_dropdown_border_color(
                dropdown_name=dropdown_name,
                decision_flag=command_executed)

        return
        # endregion

    elif home_tab_active_container == "second":

        # region (GET) Values
        (home_tab_second_container_first_frame_group_first_entry_value,
         home_tab_second_container_second_frame_group_first_subframe_first_entry_value,
         home_tab_second_container_second_frame_group_second_subframe_first_entry_value,
         home_tab_second_container_second_frame_group_third_subframe_first_entry_value) = (

            home_tab_second_container_get_values()

        )
        # endregion

        # region (EXECUTE) Function
        result = home_tab_second_container_check_required_fields_are_filled(
            home_tab_second_container_first_frame_group_first_entry_value,
            home_tab_second_container_second_frame_group_second_subframe_first_entry_value,
            home_tab_second_container_second_frame_group_third_subframe_first_entry_value)

        # Map and color
        widget_mapping = {
            'first': home_tab_second_container_first_frame_group_first_entry,
            'second': home_tab_second_container_second_frame_group_first_subframe_first_entry,
            'third': home_tab_second_container_second_frame_group_second_subframe_first_entry,
            'fourth': home_tab_second_container_second_frame_group_third_subframe_first_entry
        }

        # Check if all 3 required fields ('IPv4', 'Start port' and 'End port') have values
        if result:
            # Fix border colors
            for entry in widget_mapping:
                widget = widget_mapping[entry]
                # If it is in the not_filled_entries list, color them red
                widget.configure(border_color=GRAY_45_COLOR)

            # Mapping keys to get widget values and converting to integers
            first_entry_value = widget_mapping['first'].get()  # IPv4
            second_entry_value = int(widget_mapping['second'].get())  # Threads
            third_entry_value = int(
                widget_mapping['third'].get())  # Start port
            fourth_entry_value = int(
                widget_mapping['fourth'].get())  # End port

            # Execute function
            port_scan(first_entry_value, second_entry_value, third_entry_value,
                      fourth_entry_value)

        else:
            # Ops! Some entry are unfilled.
            not_filled_entries = home_tab_second_container_check_which_required_fields_were_not_filled_in(
                home_tab_second_container_first_frame_group_first_entry_value,
                home_tab_second_container_second_frame_group_second_subframe_first_entry_value,
                home_tab_second_container_second_frame_group_third_subframe_first_entry_value)

            for entry in widget_mapping:
                widget = widget_mapping[entry]
                if entry in not_filled_entries:
                    # If it is in the not_filled_entries list, color them red
                    widget.configure(border_color=LIGHT_RED_COLOR)
                else:
                    # If NOT, identify the appearance mode and return the color to normal
                    appeareance_mode = identifying_appearance_mode()
                    home_tab_second_container_change_color_of_unfilled_required_fields(
                        appeareance_mode, widget)

        return

        # endregion

    elif home_tab_active_container == "third":

        # region (GET) Values
        target_url = home_tab_third_container_first_frame_group_first_entry.get()
        cve_dropdown_value = home_tab_third_container_second_frame_group_first_dropdown.get()
        slider = int(
            home_tab_third_container_second_frame_group_second_subframe_first_slider.get())
        # endregion

        # region (EXECUTE) Function
        if target_url:
            home_tab_third_container_first_frame_group_first_entry.configure(
                border_color=GRAY_45_COLOR)
            identify_and_execute_correct_cve_function(cve_json_path,
                                                      target_url,
                                                      cve_dropdown_value,
                                                      slider)
        else:
            home_tab_third_container_first_frame_group_first_entry.configure(
                border_color=LIGHT_RED_COLOR)
        # endregion

        return

    else:
        command_executed = False


def configure_tab_operation_type_handler():
    global chosen_operation_type

    chosen_operation_type = None

    operation_type_first_dropdown_value = (
        configure_tab_first_container_first_frame_first_subframe_group_first_dropdown.get())

    # Filter by Operation Type: "Create" (option_1), "Update" (option_2) or "Delete" (option_3)
    if operation_type_first_dropdown_value in create_name_variations:
        chosen_operation_type = "first"
    elif operation_type_first_dropdown_value in update_name_variations:
        chosen_operation_type = "second"
    elif operation_type_first_dropdown_value in delete_name_variations:
        chosen_operation_type = "third"

    return chosen_operation_type


def configure_tab_first_container_first_scrollable_frame_get_dropdown_values():
    # Windows/Linux
    configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value = (
        configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown.get())
    # Category
    configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value = (
        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown.get())
    # User type
    configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value = (
        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown.get())

    return configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value, \
        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value, \
        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value


def configure_tab_first_container_first_scrollable_frame_get_textboxes_values():
    # NAME OF COMMAND
    configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value = (
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry.get())
    # COMMAND LINE
    configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value = (
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry.get())
    # COMMAND DESCRIPTION
    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value = (
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox.get(
            "1.0", "end-1c"))

    return (
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value)


def configure_tab_first_container_first_scrollable_frame_second_dropdown_value_converter(
        dropdown_value):
    if dropdown_value in basic_name_variations:
        dropdown_value = 'basic'
    elif dropdown_value in advanced_name_variations:
        dropdown_value = 'advanced'

    return dropdown_value


def configure_tab_get_data_from_frame(chosen_active_frame):
    # (GET) Dropdowns Values
    (
        configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value) = (

        configure_tab_first_container_first_scrollable_frame_get_dropdown_values()

    )

    # Execute the function that convert value of category dropdown and capture returns
    configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value = (
        configure_tab_first_container_first_scrollable_frame_second_dropdown_value_converter(
            configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value))

    # (GET) Textboxes Values
    (
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value) = (

        configure_tab_first_container_first_scrollable_frame_get_textboxes_values()

    )

    return (
        configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value)


def configure_tab_first_container_get_values_from_second_scrollable_frame():
    # region (GET) Values from second scrollable frame
    chosen_type = configure_tab_first_container_second_scrollable_frame_first_subframe_group_first_dropdown.get()
    associate_to_list = (
        configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.get())
    identification = configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.get()
    # endregion
    return chosen_type, associate_to_list, identification


def configure_tab_first_container_check_if_all_mandatory_fields_have_been_filled(
        chosen_identification,
        chosen_appearance,
        option_01,
        option_02):
    # region (CHECK) If all mandatory fields have been filled.
    if chosen_identification:
        if chosen_appearance in option_01:
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                border_color=GRAY_45_COLOR
            )
        elif chosen_appearance in option_02:
            configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
                border_color=GRAY_35_COLOR
            )
        return True
    else:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=LIGHT_RED_COLOR
        )
        return False
    # endregion


def create_new_cve_registry_in_json(
        cve_json_path,
        associate_to_list,
        identification,
        description):
    global all_cve_codes

    # (EXECUTE) Function that creates a New CVE Code and Description
    create_new_cve_code_and_description(
        cve_json_path,
        associate_to_list,
        identification,
        description)

    # (UPDATE) Refresh Interface Dropdown with All CVE Codes
    all_cve_codes = get_all_cve_vulnerability_codes(cve_json_path)
    home_tab_third_container_second_frame_group_first_dropdown.configure(
        values=all_cve_codes
    )

    # Adjust border color
    appearance = identifying_appearance_mode()

    if appearance in dark_name_variations:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_45_COLOR
        )
    elif appearance in light_name_variations:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_35_COLOR
        )

    return


def create_new_cve_list_in_json(
        cve_json_path,
        identification):
    global all_cve_categories

    # (EXECUTE) Function that creates a New CVE Category in Data
    create_new_cve_category(
        cve_json_path,
        identification)

    # (UPDATE) Refresh Interface Dropdown with All CVE Categories
    all_cve_categories = get_cve_vulnerability_categories(cve_json_path)
    home_tab_third_container_second_frame_group_first_dropdown.configure(
        values=all_cve_categories
    )

    # Adjust border color
    appearance = identifying_appearance_mode()

    if appearance in dark_name_variations:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_45_COLOR
        )
    elif appearance in light_name_variations:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_35_COLOR
        )

    return


def update_cve_description_in_json(
        cve_json_path,
        identification,
        description):
    if len(description) == 1:
        configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.configure(
            state='normal',
            border_color=LIGHT_RED_COLOR
        )
        return

    # (EXECUTE) Function that updates CVE Description in Data
    update_cve_description_by_code(
        cve_json_path,
        identification,
        description)

    # (UPDATE) Refresh Interface Dropdown with All CVE Codes
    all_cve_codes = get_all_cve_vulnerability_codes(cve_json_path)
    home_tab_third_container_second_frame_group_first_dropdown.configure(
        values=all_cve_codes
    )

    # (GET) Chosen value in dropdown "Single/List/All" CVE Check
    chosen_code = home_tab_third_container_second_frame_group_first_dropdown.get()

    # (GET) Description by cve code
    cve_description = get_cve_description_by_cve_code(cve_json_path,
                                                      chosen_code)

    # (UPDATE) Description by vulnerability
    home_tab_third_container_third_frame_group_first_textbox.configure(
        state='normal')
    home_tab_third_container_third_frame_group_first_textbox.delete('0.0',
                                                                    'end')
    home_tab_third_container_third_frame_group_first_textbox.insert('0.0',
                                                                    cve_description)
    home_tab_third_container_third_frame_group_first_textbox.configure(
        state='disabled')

    # (UPDATE) border color
    appearance = identifying_appearance_mode()

    if appearance in dark_name_variations:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_45_COLOR
        )
    elif appearance in light_name_variations:
        configure_tab_first_container_second_scrollable_frame_first_frame_group_first_entry.configure(
            border_color=GRAY_35_COLOR
        )

    return


def configure_tab_first_container_second_scrollable_frame_filter_and_execute_function(
        operation_type,
        item_type,
        associate_to_list,
        identification):
    description = configure_tab_first_container_second_scrollable_frame_fourth_frame_group_first_textbox.get(
        '0.0',
        'end')

    match operation_type:
        case 'first':  # Create
            match item_type:
                case 'CVE Code':
                    create_new_cve_registry_in_json(
                        cve_json_path,
                        associate_to_list,
                        identification,
                        description)

                case 'List':
                    create_new_cve_list_in_json(
                        cve_json_path,
                        identification)

        case 'second':  # Update
            match item_type:
                case 'CVE Code':
                    update_cve_description_in_json(
                        cve_json_path,
                        identification,
                        description)
                case 'List':
                    return
        case 'third':  # Delete
            match item_type:
                case 'CVE Code':
                    delete_cve_record_by_code(cve_json_path, identification)
                    return
                case 'List':
                    delete_cve_category(cve_json_path, associate_to_list)
                    return


def configure_tab_create_button_handler():
    global all_cve_categories, \
        all_cve_codes

    configure_tab_operation_type_handler()

    # (GET) Retrieve Values from Configure Tab
    (
        configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value,
        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value,

        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value,
        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value) = (

        configure_tab_get_data_from_frame(configure_tab_active_container)

    )

    json_command_path = "src/json/commands.json"

    # Filter by Item (Active Scrollable Frame)
    if configure_tab_active_container == "first":  # Command line

        # region (CHECK) That all mandatory fields have been filled in
        # List of mandatory fields
        mandatory_fields = [
            configure_tab_first_container_first_scrollable_frame_second_frame_first_entry,
            configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry
        ]

        # Iterate over the fields
        for field in mandatory_fields:
            # Get the value of the field
            field_value = field.get()

            # Check if the field is blank and apply the border coloring logic
            if not field_value:
                field.configure(border_color=LIGHT_RED_COLOR)
                return
            else:
                appearance = identifying_appearance_mode()
                if appearance in dark_name_variations:
                    field.configure(border_color=GRAY_45_COLOR)
                elif appearance in light_name_variations:
                    field.configure(border_color=GRAY_45_COLOR)
        # endregion

        chosen_command_line_interface = ""

        match configure_tab_first_container_first_scrollable_frame_first_subframe_group_first_dropdown_value:
            case "Windows":
                chosen_command_line_interface = "shell"
            case "Linux":
                chosen_command_line_interface = "bash"

        match chosen_operation_type:
            case "first":  # create command
                if configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value:
                    add_command(
                        json_command_path,
                        chosen_command_line_interface,
                        configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value,
                        configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value,
                        configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value,
                        configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value,
                        configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value)
            case "second":  # update command
                update_command(
                    json_command_path,
                    chosen_command_line_interface,
                    configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value,
                    configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value,
                    configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value,
                    configure_tab_first_container_first_scrollable_frame_third_frame_group_first_entry_value,
                    configure_tab_first_container_first_scrollable_frame_fourth_frame_group_first_textbox_value)
            case "third":  # delete commmand
                delete_command(
                    json_command_path,
                    chosen_command_line_interface,
                    configure_tab_first_container_first_scrollable_frame_first_frame_group_third_dropdown_value,
                    configure_tab_first_container_first_scrollable_frame_second_subframe_group_second_dropdown_value,
                    configure_tab_first_container_first_scrollable_frame_second_frame_first_entry_value)

        define_command_options_in_dropdown_on_start()

        # Reset values (Dropdown + Textboxes)
        home_tab_first_container_scrollable_frame_third_frame_group_first_textbox_reset()
        home_tab_first_container_scrollable_frame_second_frame_group_first_dropdown.set(
            value='')

    elif configure_tab_active_container == "second":  # CVE Vulnerabilities

        appearance = identifying_appearance_mode()

        # (GET) Retrieve Values
        chosen_type, associate_to_list, identification = (
            configure_tab_first_container_get_values_from_second_scrollable_frame())

        # (CHECK) Verify Mandatory Field Completion
        are_mandatory_fields_filled = configure_tab_first_container_check_if_all_mandatory_fields_have_been_filled(
            identification,
            appearance,
            dark_name_variations,
            light_name_variations)

        if not are_mandatory_fields_filled:
            return

        # (FILTER and EXECUTE) Invoke Filtering and Execution Function
        configure_tab_first_container_second_scrollable_frame_filter_and_execute_function(
            chosen_operation_type,
            chosen_type,
            associate_to_list,
            identification)

        # (UPDATE) Dropdowns in the Configure Tab and Home Tab
        all_cve_categories = get_cve_vulnerability_categories(cve_json_path)
        all_cve_codes = get_all_cve_vulnerability_codes(cve_json_path)
        configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.configure(
            values=all_cve_categories
        )
        configure_tab_first_container_second_scrollable_frame_second_subframe_group_second_dropdown.set(
            '')
        home_tab_third_container_second_frame_group_first_dropdown.configure(
            values=all_cve_codes
        )


if __name__ == '__main__':
    main()
