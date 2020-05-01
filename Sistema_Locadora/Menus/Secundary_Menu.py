from Sistema_Locadora.Menus.Customer_Menu import CustomerMenu
from Sistema_Locadora.Menus.Dvd_Game_Menu import DvdGameMenu
from Sistema_Locadora.Menus.Rent_DVD_Game_Menu import RentDvdGameMenu
from Sistema_Locadora.Menus.Validates_Menu import Validate
from Sistema_Locadora.Menus.Employee_Menu import EmployeeMenu


class SecundaryMenu:

    @staticmethod
    def secundary_menu(job_role, user_id):
        try:
            validate = Validate()
            print("_" * 80)

            if job_role not in("GERENTE DE LOJA", "ADMINISTRADOR DE SISTEMA"):
                choose = input("\n \t \t \t Menu Secundário - Operações Locadora\n" + "_"*80 + "\n 1 º Clientes\n "
                               "2 º DVD's e Jogos\n 3 º Empréstimo de Dvd's e Jogos\n 4º Sair\n"
                               " Escolha a sua opção aqui ---> ")
                while choose not in("1", "2", "3", "4"):
                    validate.validate_text_while()
                    choose = input("\n \t \t \t Menu Secundário - Operações Locadora\n" + "_" * 80 +
                                   "\n 1 º Clientes\n 2 º DVD's e Jogos\n 3 º Empréstimo de Dvd's e Jogos\n 4º Sair\n "
                                   "Escolha a sua opção aqui ---> ")

                if choose == "1":
                    customer_menu = CustomerMenu()
                    customer_menu.customer_menu(user_id)

                elif choose == "2":
                    dvd_game_menu = DvdGameMenu()
                    dvd_game_menu.dvd_game_menu(user_id)

                elif choose == "3":
                    rent_dvd_game_menu = RentDvdGameMenu()
                    rent_dvd_game_menu.rent_dvd_game_menu(user_id)

                elif choose == "4":
                    print("_"*80)
                    print("Saindo do Sistema...")
                    exit()

            else:
                choose = input("\n \t \t \t Menu Secundário - Operações Locadora\n" + "_" * 80 + "\n 1 º Clientes\n "
                               "2 º DVD's e Jogos\n 3 º Empréstimo de Dvd's e Jogos\n 4º Funcionários\n 5º Sair\n"
                               " Escolha a sua opção aqui ---> ")
                while choose not in ("1", "2", "3", "4"):
                    validate.validate_text_while()
                    choose = input("\n \t \t \t Menu Secundário - Operações Locadora\n" + "_" * 80 +
                                   "\n 1 º Clientes\n 2 º DVD's e Jogos\n 3 º Empréstimo de Dvd's e Jogos\n"
                                   " 4º Funcionários\n 5º Sair\n "
                                   "Escolha a sua opção aqui ---> ")

                if choose == "1":
                    customer_menu = CustomerMenu()
                    customer_menu.customer_menu(user_id)

                elif choose == "2":
                    dvd_game_menu = DvdGameMenu()
                    dvd_game_menu.dvd_game_menu(user_id)

                elif choose == "3":
                    rent_dvd_game_menu = RentDvdGameMenu()
                    rent_dvd_game_menu.rent_dvd_game_menu(user_id)

                elif choose == "4":
                    employee = EmployeeMenu()
                    employee.employee_menu(user_id)

                elif choose == "5":
                    print("_" * 80)
                    print("Saindo do Sistema...")
                    exit()

        except():
            print("_"*80)
            print("Erro em geral ao tentar executar os processos no Menu Secundário.")


"""secundary_menu = SecundaryMenu()
secundary_menu.secundary_menu()"""
