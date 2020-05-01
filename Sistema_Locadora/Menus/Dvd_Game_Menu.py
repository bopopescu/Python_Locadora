from Sistema_Locadora.Operations_CRUD.Actions_DVD_Game import DvdGame
from Sistema_Locadora.Getters_Setters.DVD_Games_Getters_Setters import DvdGamesGetSet
from Sistema_Locadora.Menus.Validates_Menu import Validate
from Sistema_Locadora.Menus.Data_Load.Data_Load_DVD_Game import DataLoad


class DvdGameMenu(DvdGame):

    global validate
    validate = Validate()

    def dvd_game_menu(self, user_id):
        print("_"*80)
        choice_options = input("\n \t \t \t Menu de Dvd 's e Jogos\n\n " + "_"*80 + "\n " +
                               "1º Consultar Dvd ou Jogos\n 2º Pesquisar por Dvd ou Jogo\n 3º Inserir Novo Dvd ou Jogo"
                               "\n 4º Alterar Dvd ou Jogo\n 5º Excluir Jogo ou Dvd\n 6º Carga em CSV\n "
                               "7º Sair\n Escolha a sua Opcação --> ")
        while choice_options not in("1", "2", "3", "4", "5", "6", "7"):
            validate.validate_text_while()
            choice_options = input("\n \t \t \t Menu de Dvd 's e Jogos\n\n " + "_" * 80 + "\n" +
                                   "\n 1º Consultar Dvd ou Jogos\n 2º Pesquisar por Dvd ou Jogo\n "
                                   "3º Inserir Novo Dvd ou Jogo \n 4º Alterar Dvd ou Jogo\n "
                                   "5º Excluir Jogo ou Dvd\n 6º Carga em CSV\n 7º Sair\n Escolha a sua Opcação --> ")
        if choice_options == "1":
            self.select_all_dvd_game()

        elif choice_options == "2":
            self.search_for_dvd_game()

        elif choice_options == "3":
            self.register_dvd_game(user_id)

        elif choice_options == "4":
            self.update_dvd_game(user_id)

        elif choice_options == "5":
            self.delete_dvd_game()

        elif choice_options == "6":
            print("_"*80)
            self.import_lines_csv(user_id)

        elif choice_options == "7":
            print("_" * 80)
            print("Saindo do Sistema.")
            exit()

    def register_dvd_game(self, user_id):
        price_format = 0

        print("_"*80)
        name = input("Digite o Nome do Novo Dvd ou Jogo: ")
        while name is "":
            print("_"*80)
            print("Por favor digite corretamente o Nome do Dvd ou do Jogo.")
            name = input("Digite o Nome do Novo Dvd ou Jogo: ")

        genare = input("Digite o Genêro do Dvd ou do Jogo: ")
        while genare is "" or genare.isdigit():
            print("_"*80)
            print("Por favor digite corretamente o Genêro do Dvd ou do Jogo. ")
            genare = input("Digite o Genêro: ")

        classification_age = input("Digite a Classificação de Idade: ")
        while classification_age is "" or classification_age.isdigit() is False or int(classification_age) < 0:
            print("_"*80)
            print("Por favor digite corretamente a Classificação de Idade.")
            classification_age = input("Digite a Classificação de Idade:")

        type_dvd_game = input("Digite o Tipo (Dvd ou Jogo): ")
        type_dvd_game = type_dvd_game.title()
        while type_dvd_game not in("Dvd", "Jogo"):
            print("_"*80)
            print("Por favor digite corretamente o Tipo da Mídia que você está cadastrando.")
            type_dvd_game = input("Digite o Tipo (Dvd ou Jogo): ")
            type_dvd_game = type_dvd_game.title()

        try:
            price = input("Digite o Preço da Mídia: ")
            price = price.replace(",", ".")
            price_format = float(price)

            while price_format <= 0:
                print("_" * 80)
                print("Por favor digite o Valor do Preço corretamente.")
                price = input("Digite o Preço da Mídia: ")
                price = price.replace(",", ".")
                price_format = float(price)

        except ValueError:
            print("_"*80)
            print("Por favor digite apenas valores numéricos.")
            exit()

        date_fabrication = input("Digite a Data de Fabricação do Dvd ou Jogo: ")
        date_format = validate.validation_date_insert(date_fabrication)

        while date_format is None:
            print("_"*80)
            print("Por favor digite a Data de Fabricação corretamente.")
            date_fabrication = input("Digite a Data de Fabricação do Dvd ou Jogo: ")
            date_format = validate.validation_date_insert(date_fabrication)

        qty = input("Digite a Quantidade de Dvd ou Jogos: ")
        while qty is "" or qty.isnumeric() is False or int(qty) <= 0:
            print("_"*80)
            print("Por favor digite corretamente a Quantidade de Dvd ou Jogo: ")
            qty = input("Digite a Quantidade de Dvd ou Jogos: ")

        datas_dvd_game = []
        dvd_game_set_get = DvdGamesGetSet(name, genare, int(classification_age), type_dvd_game, price_format,
                                          date_format, int(qty), user_id)

        datas_dvd_game.append(dvd_game_set_get.name_game)
        datas_dvd_game.append(dvd_game_set_get.genare)
        datas_dvd_game.append(dvd_game_set_get.classific_age)
        datas_dvd_game.append(dvd_game_set_get.type_dvd_game)
        datas_dvd_game.append(dvd_game_set_get.price)
        datas_dvd_game.append(dvd_game_set_get.date_fabrication)
        datas_dvd_game.append(dvd_game_set_get.quantity)
        datas_dvd_game.append(dvd_game_set_get.user_id)

        self.insert(datas_dvd_game)

    def update_dvd_game(self, user_id):
        print("_" * 80)
        options_updates = input("\t \t \t Menu de Alteração de Dados de DVD's e Jogos \n" + "_"*80 +
                                "\n Escolha o Índice do Campo que Você Quer Alterar\n\n"
                                " 1º Nome\n 2º Gênero\n 3º Classificação de Idade\n 4º Tipo (Dvd ou Jogo)\n"
                                " 5º Preço\n 6º Data de Fabricação\n 7º Quantidade\n Escolha a sua opção --> ")

        if options_updates in("1", "2", "3", "4", "5", "6", "7"):
            print("_"*80)
            name = validate.validate_name_dvd_game()

            if options_updates == "1":
                new_name = input("Digite o Nome do Novo Dvd ou Jogo : ")
                while new_name is "":
                    print("_" * 80)
                    print("Por favor digite corretamente o Nome do Dvd ou do Jogo.")
                    new_name = input("Digite o Nome do Novo Dvd ou Jogo : ")
                self.update_name(name, new_name, user_id)

            elif options_updates == "2":
                genare = input("Digite o Genêro do Dvd ou do Jogo: ")
                while genare is "" or genare.isdigit():
                    print("_"*80)
                    print("Por favor digite corretamente o Genêro do Dvd ou do Jogo. ")
                    genare = input("Digite o Genêro: ")
                self.update_genare(name, genare, user_id)

            elif options_updates == "3":
                classification_age = input("Digite a Classificação de Idade: ")
                while classification_age is "" or classification_age.isdigit() is False or int(classification_age) < 0:
                    print("_" * 80)
                    print("Por favor digite corretamente a Classificação de Idade.")
                    classification_age = input("Digite a Classificação de Idade:")
                self.update_classification_age(name, int(classification_age), user_id)

            elif options_updates == "4":
                type_dvd_game = input("Digite o Tipo (Dvd ou Jogo): ")
                type_dvd_game = type_dvd_game.title()
                while type_dvd_game not in ("Dvd", "Jogo"):
                    print("_" * 80)
                    print("Por favor digite corretamente o Tipo da Mídia que você está cadastrando.")
                    type_dvd_game = input("Digite o Tipo (Dvd ou Jogo): ")
                    type_dvd_game = type_dvd_game.title()
                self.update_type_dvd_game(name, type_dvd_game, user_id)

            elif options_updates == "5":
                try:
                    price = input("Digite o Preço da Mídia: ")
                    price = price.replace(",", ".")
                    while price.isalpha() or float(price) <= 0:
                        print("_" * 80)
                        print("Por favor digite o Valor do Preço corretamente.")
                        price = input("Digite o Preço da Mídia: ")
                        price = price.replace(",", ".")
                    self.update_price(name, float(price), user_id)

                except ValueError:
                    print("_"*80)
                    print("Por favor digite um valor válido.")

            elif options_updates == "6":
                date_fabrication = input("Digite a Data de Fabricação do Dvd ou Jogo: ")
                date_fabrication_format = validate.validation_date_insert(date_fabrication)

                while date_fabrication_format is None:
                    print("_" * 80)
                    print("Por favor digite a Data de Fabricação corretamente.")
                    date_fabrication = input("Digite a Data de Fabricação do Dvd ou Jogo: ")
                    date_fabrication_format = validate.validation_date_insert(date_fabrication)

                self.update_fabrication_date(name, date_fabrication_format, user_id)

            elif options_updates == "7":
                qty = input("Digite a Quantidade de Dvd ou Jogos: ")
                while qty is "" or qty.isnumeric() is False or int(qty) <= 0:
                    print("_" * 80)
                    print("Por favor digite corretamente a Quantidade de Dvd ou Jogo: ")
                    qty = input("Digite a Quantidade de Dvd ou Jogos: ")

                self.update_quantity(name, int(qty), user_id)

        else:
            print("_"*80)
            print("Opção Inválida.")

    def delete_dvd_game(self):
        print("_"*80)
        name_dvd_game = validate.validate_name_dvd_game()
        confirm_delete = input("Você realmente deseja deletar este Registro (S - Sim/ N - Não): ")
        confirm_delete = confirm_delete.upper()
        if confirm_delete == "S":
            self.delete(name_dvd_game)

        else:
            print("_" * 80)
            print("O registro não foi excluído.")

    def select_all_dvd_game(self):
        print("_"*80)
        self.select_all()

    def search_for_dvd_game(self):
        print("_"*80)
        name_dvd_game = input("Digite o Nome do Dvd ou Jogo: ")
        while name_dvd_game is "":
            print("_"*80)
            print("Por favor Digite o Nome do Dvd ou Jogo corretamente.")
            name_dvd_game = input("Digite o Nome do Dvd ou Jogo: ")

        self.search_dvd_game(name_dvd_game)

    @staticmethod
    def import_lines_csv(user_id):
        insert_dvd_game_csv = DataLoad()
        insert_dvd_game_csv.data_load_csv(user_id)


"""dvd_game = DvdGameMenu()
dvd_game.dvd_game_menu()"""
