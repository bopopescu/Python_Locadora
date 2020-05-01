from Sistema_Locadora.Operations_CRUD.Actions_Rent_DVD_Game import RentDvdGame
from Sistema_Locadora.Getters_Setters.Rent_DVD_Games_Getters_Setters import RentDvdGameGetSet
from Sistema_Locadora.Menus.Validates_Menu import Validate
from Sistema_Locadora.Operations_Files.Report_File_Txt import Report
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow


class RentDvdGameMenu(RentDvdGame):
    global validate, report_txt
    report_txt = Report()
    validate = Validate()

    def rent_dvd_game_menu(self, user_id):
        print("_"*80)
        choice = input("\n \t \t \t Menu de Empréstimo de DVD's e Jogos\n" + "_"*80 +
                       "\n Escolha uma das Opções abaixo\n\n 1º Empréstimo de DVD's e Filmes\n "
                       "2º Alterar Empréstimo de DVD's ou Jogos\n 3º Excluir um Registro\n "
                       "4º Verificar Todos os Registros\n 5º Pesquisar por um registro.\n "
                       "6º Relatório de Empréstimos\n 7º Sair\n Escolha a sua opção aqui --> ")
        while choice not in("1", "2", "3", "4", "5", "6", "7"):
            validate.validate_text_while()
            choice = input("\n \t \t \t Menu de Empréstimo de DVD's e Jogos\n" + "_" * 80 +
                           "\n Escolha uma das Opções abaixo\n\n 1º Empréstimo de DVD's e Filmes\n "
                           "2º Alterar Empréstimo de DVD's ou Jogos\n 3º Excluir um Registro\n "
                           "4º Verificar Todos os Registros\n 5º Pesquisar por um registro.\n "
                           "6º Relatório de Empréstimos\n 7º Sair\n Escolha a sua opção aqui --> ")

        if choice == "1":
            self.register_rent_dvd_game(user_id)

        elif choice == "2":
            self.update_rent_dvd_game(user_id)

        elif choice == "3":
            self.delete_rent_dvd_game()

        elif choice == "4":
            self.select_all_rent_dvd_game()

        elif choice == "5":
            self.search_for_rent_dvd_game()

        elif choice == "6":
            self.report_txt_history_rent()

        elif choice == "7":
            print("_"*80)
            print("Encerrando o Programa")
            exit()

        else:
            print("_"*80)
            print("Opção inválida.")

    def register_rent_dvd_game(self, user_id):
        try:
            daily_value_format = 0
            print("_"*80)
            cpf_employee = validate.validate_employee_cpf()
            cpf_customer = validate.validate_customer_cpf()
            name_dvd_game = validate.validate_name_dvd_game()

            qty_days_rent = input("Digite a quantidade de dias para empréstimo: ")
            while qty_days_rent.isnumeric() is False:
                print("_"*80)
                print("Por favor digite um valor válido para quantidade de dias.")
                qty_days_rent = input("Digite a quantidade de dias para empréstimo: ")

            if qty_days_rent.isnumeric():
                try:
                    while int(qty_days_rent) <= 0:
                        print("_" * 80)
                        print("Por favor digite um valor maior que zero!")
                        qty_days_rent = int(input("Digite a quantidade de dias para empréstimo: "))

                except ValueError:
                    print("_"*80)
                    print("Por favor digite somente valores numéricos.")
                    exit()

            daily_value = input("Digite o valor da diária: ")
            daily_value = daily_value.replace(",", ".")
            while daily_value is "":
                print("_" * 80)
                print("Por favor digite um valor válido.")
                daily_value = input("Digite o valor da diária: ")
                daily_value.replace(",", ".")

            try:
                daily_value_format = float(daily_value)
                while daily_value_format <= 0:
                    print("_" * 80)
                    print("Por favor digite um valor diário corretamente.")
                    daily_value = input("Digite o valor da diária: ")
                    daily_value.replace(",", ".")
                    daily_value_format = float(daily_value)

            except ValueError:
                print("_" * 80)
                print("Por favor digite somente valores numéricos.")
                exit()

            datas_rent_dvd_game = []
            rent_dvd_game_set_get = RentDvdGameGetSet(int(qty_days_rent), float(daily_value_format), cpf_employee,
                                                      cpf_customer, name_dvd_game, user_id)

            datas_rent_dvd_game.append(rent_dvd_game_set_get.quantity_days_rent)
            datas_rent_dvd_game.append(rent_dvd_game_set_get.daily_value)
            datas_rent_dvd_game.append(rent_dvd_game_set_get.cpf_employee)
            datas_rent_dvd_game.append(rent_dvd_game_set_get.cpf_customer)
            datas_rent_dvd_game.append(rent_dvd_game_set_get.name_dvd_game)
            datas_rent_dvd_game.append(rent_dvd_game_set_get.user_id)
            self.insert(datas_rent_dvd_game)

        except():
            print("_"*80)
            print("Erro em geral ao tentar registrar o Empréstimo deste Dvd ou Jogo.")

    def update_rent_dvd_game(self, user_id):
        print("_"*80)
        options = input("\t \t \t Menu de Alterações\n " + "_"*80 +
                        "\n Escolha uma das opções abaixo\n\n 1º Alterar Cliente"
                        "\n 2º Alterar Dvd ou Jogo\n 3º Alterar funcionário\n"
                        " 4º Alterar a Quantidade de dias alugado\n 5º Alterar Valor da diária\n "
                        "6º Sair\n Escolha a sua opção aqui -->  ")

        if options in("1", "2", "3", "4", "5"):
            validate_cpf_customer = validate.validate_customer_cpf()
            validate_name_dvd_game = validate.validate_name_dvd_game()

            id_customer = self.return_id_cliente(validate_cpf_customer)
            id_dvd_game = self.return_id_dvd_jogo(validate_name_dvd_game)
            id_rent_dvd_game = self.return_id_empr_dvd_jogo(id_customer, id_dvd_game)

            if id_rent_dvd_game is not None:
                if options == "1":
                    print("_"*80)
                    print("CPF do Novo Cliente abaixo.")
                    new_cpf_customer = validate.validate_customer_cpf()
                    self.update_id_customer(validate_cpf_customer, validate_name_dvd_game, new_cpf_customer, user_id)

                elif options == "2":
                    print("_" * 80)
                    print("Nome do Novo DVD ou Jogo abaixo.")
                    new_name_dvd_game = validate.validate_name_dvd_game()
                    self.update_id_dvd_game(validate_cpf_customer, validate_name_dvd_game, new_name_dvd_game, user_id)

                elif options == "3":
                    old_cpf_employee = validate.validate_employee_cpf()
                    if old_cpf_employee is not None:
                        print("_" * 80)
                        print("CPF do Novo Funcionário abaixo.")
                        new_cpf_employee = validate.validate_employee_cpf()
                        self.update_id_employee(validate_cpf_customer, validate_name_dvd_game, new_cpf_employee,
                                                user_id)

                elif options == "4":
                    print("_" * 80)
                    print("Nova Quantidade de dias emprestados abaixo.")
                    qty_days_rent = input("Digite a quantidade de dias para empréstimo: ")
                    while qty_days_rent.isnumeric() is False:
                        print("_" * 80)
                        print("Por favor digite um valor válido para quantidade de dias.")
                        qty_days_rent = input("Digite a quantidade de dias para empréstimo: ")

                    if qty_days_rent.isnumeric():
                        try:
                            while int(qty_days_rent) <= 0:
                                print("_" * 80)
                                print("Por favor digite um valor maior que zero!")
                                qty_days_rent = int(input("Digite a quantidade de dias para empréstimo: "))

                            self.update_qty_days_emp(validate_cpf_customer, validate_name_dvd_game, qty_days_rent,
                                                     user_id)

                        except ValueError:
                            print("_" * 80)
                            print("Por favor digite somente valores numéricos.")
                            exit()

                elif options == "5":
                    print("_" * 80)
                    print("Novo Valor diário do Empréstimo abaixo.")
                    daily_value = input("Digite o valor da diária: ")
                    daily_value = daily_value.replace(",", ".")
                    while daily_value is "":
                        print("_" * 80)
                        print("Por favor digite um valor válido.")
                        daily_value = input("Digite o valor da diária: ")
                        daily_value.replace(",", ".")

                    try:
                        daily_value_format = float(daily_value)
                        while daily_value_format <= 0:
                            print("_" * 80)
                            print("Por favor digite um valor diário corretamente.")
                            daily_value = input("Digite o valor da diária: ")
                            daily_value.replace(",", ".")
                            daily_value_format = float(daily_value)
                        self.update_daily_value(validate_cpf_customer, validate_name_dvd_game, daily_value_format,
                                                user_id)

                    except ValueError:
                        print("_" * 80)
                        print("Por favor digite somente valores numéricos.")
                        exit()

        elif options == "6":
            print("_"*80)
            print("Encerrando o programa...")
            exit()

        else:
            print("_"*80)
            print("Opção inválida")

    def delete_rent_dvd_game(self):
        print("_"*80)
        customer_cpf = validate.validate_customer_cpf()
        name_dvd_game = validate.validate_name_dvd_game()

        confirm_delete = input("Deseja realmente Excluir este registro ? (S - Sim ou  N - Não): ")
        confirm_delete = confirm_delete.upper()

        if confirm_delete == "S":
            self.delete(customer_cpf, name_dvd_game)

    def select_all_rent_dvd_game(self):
        print("_"*80)
        self.select_all()

    def search_for_rent_dvd_game(self):
        print("_"*80)
        customer_name = input("Digite o nome do cliente: ")
        while customer_name is "":
            print("_"*80)
            print("Por favor digite o nome do cliente.")
            customer_name = input("Digite o nome do cliente: ")

        name_dvd_game = input("Digite o nome do Dvd ou Jogo: ")
        self.search_rent_dvd_game(customer_name, name_dvd_game)

    @staticmethod
    def report_txt_history_rent():
        start_date_format = ""
        print("_"*80)
        start_date = input("Digite a Data Inicial: ")
        if start_date is "":
            now = DateHourNow()
            start_date = now.get_just_date()

        start_date_format = validate.validation_date_select(start_date)

        while start_date_format is None:
            print("_" * 80)
            print("Por favor digite a Data Inicial corretamente.")
            start_date = input("Digite a Data Inicial: ")
            start_date_format = validate.validation_date_select(start_date)

        end_date = input("Digite a Data Final: ")
        if end_date is "":
            end_date = start_date_format
        end_date_format = validate.validation_date_select(end_date)

        while end_date_format is None:
            print("_" * 80)
            print("Por favor digite a Data Final corretamente.")
            end_date = input("Digite a Data Final: ")
            end_date_format = validate.validation_date_select(end_date)

        report_txt.report_txt(start_date_format, end_date_format)


"""test = MenuRentDvdGame()
test.rent_dvd_game_menu()"""
