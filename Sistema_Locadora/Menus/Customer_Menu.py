from Sistema_Locadora.Getters_Setters.Customers_Getters_Setters import CustomersGetSet
from Sistema_Locadora.Operations_CRUD.Actions_Customer import Customer
from Sistema_Locadora.Menus.Validates_Menu import Validate


class CustomerMenu(Customer):

    global validate
    validate = Validate()

    def customer_menu(self, user_id):
        print("_"*80)
        choice_option = input("\n \t \t \t Menu Clientes\n" + "_"*80 +
                              "\n 1º Verificar Clientes Cadastrados\n 2º Pesquisar por Cliente\n"
                              " 3º Cadastrar Cliente\n 4º Alterar Cliente\n 5º Exlcuir Cliente\n 6º Sair\n "
                              "Escolha a sua opção --> ")
        while choice_option not in("1", "2", "3", "4", "5", "6"):
            validate.validate_text_while()
            choice_option = input("\t \t \t Menu Clientes\n" + "_" * 80 +
                                  "\n 1º Verificar Clientes Cadastrados\n 2º Pesquisar por Cliente\n"
                                  " 3º Cadastrar Cliente\n 4º Alterar Cliente\n 5º Exlcuir Cliente\n 6º Sair\n "
                                  "Escolha a sua opção --> ")

        if choice_option == "1":
            self.select_all_customers()

        elif choice_option == "2":
            self.search_customer_name()

        elif choice_option == "3":
            self.register_customer(user_id)

        elif choice_option == "4":
            self.update_customer(user_id)

        elif choice_option == "5":
            self.delete_customer()

        elif choice_option == "6":
            print("_"*80)
            print("Saindo do Sistema.")
            exit()

    def register_customer(self, user_id):
        datas = []

        print("_" * 80)
        name = input("Digite o Nome do Cliente: ")
        while name.isdigit() or name is "":
            print("_"*80)
            print("Por favor digite o seu nome corretamente.")
            name = input("Digite o Nome do Cliente: ")

        age = input("Digite a Idade do Cliente: ")
        while age.isdigit() is False or age is "" or len(age) > 3:
            print("_"*80)
            print("Por favor digite a sua idade corretamente.")
            age = input("Digite a Idade do Cliente: ")

        street = input("Digite o Nome da Rua do Cliente: ")
        if street is "":
            street = None

        number = input("Digite o Número: ")
        if number is not "":
            while number.isdigit() is False:
                print("_"*80)
                print("Por favor digite o Número corretamente.")
                number = input("Digite o Número: ")

        elif number is "":
            number = None

        complement = input("Digite o Complemento do Endereço do Cliente: ")
        if complement is "":
            complement = None

        cep = input("Digite o CEP do Cliente: ")
        cep = cep.replace(".", "")
        cep = cep.replace("-", "")
        while cep.isdigit() is False or len(cep) != 8:
            print("_"*80)
            print("Por favor digite o CEP do Cliente de Maneira correta.")
            cep = input("Digite o CEP do Cliente: ")
            cep = cep.replace(".", "")
            cep = cep.replace("-", "")

        telephone = input("Digite o número de Telefone do Cliente:")
        telephone = telephone.replace("-", "")
        telephone = telephone.replace(".", "")
        if telephone is not "":
            while telephone.isdigit() is False:
                print("_"*80)
                print("Por favor digite o Número do Telefone corretamente.")
                telephone = input("Digite o número de Telefone do Cliente:")
                telephone = telephone.replace("-", "")
                telephone = telephone.replace(".", "")

        elif telephone is "":
            telephone = None

        cellphone = input("Digite o Número do Celular do Cliente com o DD: ")
        cellphone = cellphone.replace("-", "")
        cellphone = cellphone.replace(".", "")
        while cellphone.isdigit() is False or cellphone is "":
            print("_"*80)
            print("Por favor digite o Número do Celular Do Cliente corretamente.")
            cellphone = input("Digite o Número do Celular do Cliente com o DD: ")
            cellphone = cellphone.replace("-", "")
            cellphone = cellphone.replace(".", "")

        rg = input("Digite o Número do RG do Cliente: ")
        rg = rg.replace(".", "")
        rg = rg.replace("-", "")
        check_rg = self.check_rg(rg)
        while rg.isdigit() is False or len(rg) != 9 or check_rg is not None:
            print("_"*80)
            print("Por favor digite o Número do RG do Cliente corretamente ou\nEste RG já está sendo usado no Sistema.")
            rg = input("Digite o Número do RG do Cliente: ")
            rg = rg.replace(".", "")
            rg = rg.replace("-", "")
            check_rg = self.check_rg(rg)

        cpf = input("Digite o Número do CPF do Cliente: ")
        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")
        cpf_validate = self.return_id(cpf)
        analsying_cpf = validate.validate_number_cpf_employee(cpf)
        while cpf.isdigit() is False or len(cpf) != 11 or cpf_validate is not None or analsying_cpf == 0:
            print("_"*80)
            print("Por favor digite o Número do CPF do Cliente corretamente ou\n"
                  "Este CPF já está sendo usado no Sistema.")
            cpf = input("Digite o Número do CPF do Cliente: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            cpf_validate = self.return_id(cpf)
            analsying_cpf = validate.validate_number_cpf_employee(cpf)

        customer_get_set = CustomersGetSet(name, int(age), street, number, complement, cep, telephone, cellphone,
                                           rg, cpf, user_id)
        datas.append(customer_get_set.name)
        datas.append(customer_get_set.age)
        datas.append(customer_get_set.street)
        datas.append(customer_get_set.number)
        datas.append(customer_get_set.complement)
        datas.append(customer_get_set.cep)
        datas.append(customer_get_set.telephone)
        datas.append(customer_get_set.cellphone)
        datas.append(customer_get_set.rg)
        datas.append(customer_get_set.cpf)
        datas.append(customer_get_set.user_id)

        self.insert(datas)

    def update_customer(self, user_id):
        print("_" * 80)
        choice = input("\t \t \t Menu de Alteração de Dados de Cliente\n" + "_"*80 +
                       "\n \nEscolha o Índice referente ao campo que você quer alterar\n\n 1º Nome\n 2º Idade\n "
                       "3º Rua\n 4º Número\n 5º Complemento\n 6º CEP\n 7º Telefone\n 8º Celular\n 9º RG\n 10º CPF\n"
                       " Escolha a Opção desejada --> ")

        if choice in("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
            print("_"*80)
            cpf = validate.validate_customer_cpf()

            if choice == "1":
                name = input("Digite o Novo Nome do Cliente: ")
                while name.isdigit() or name is "":
                    print("_" * 80)
                    print("Por favor digite o nome corretamente.")
                    name = input("Digite o Novo Nome do Cliente: ")

                self.update_name(cpf, name, user_id)

            elif choice == "2":
                age = input("Digite a Nova Idade do Cliente: ")
                while age.isdigit() is False or age is "" or len(age) > 3:
                    print("_" * 80)
                    print("Por favor digite a sua idade corretamente.")
                    age = input("Digite a Nova Idade do Cliente: ")

                self.update_age(cpf, age, user_id)

            elif choice == "3":
                street = input("Digite o Novo Nome da Rua do Cliente: ")
                if street is "":
                    street = None

                self.update_street(cpf, street, user_id)

            elif choice == "4":
                number = input("Digite o Novo Número: ")
                if number is not "":
                    while number.isdigit() is False:
                        print("_" * 80)
                        print("Por favor digite o Número corretamente.")
                        number = input("Digite o Número: ")

                elif number is "":
                    number = None

                self.update_number(cpf, number, user_id)

            elif choice == "5":
                complement = input("Digite o Novo Complemento do Endereço do Cliente: ")
                if complement is "":
                    complement = None

                self.update_complement(cpf, complement, user_id)

            elif choice == "6":
                cep = input("Digite o Novo CEP do Cliente: ")
                cep = cep.replace(".", "")
                cep = cep.replace("-", "")
                while cep.isdigit() is False or len(cep) != 8:
                    print("_" * 80)
                    print("Por favor digite o Novo CEP do Cliente de Maneira correta.")
                    cep = input("Digite o Novo CEP do Cliente: ")
                    cep = cep.replace(".", "")
                    cep = cep.replace("-", "")

                self.update_cep(cpf, cep, user_id)

            elif choice == "7":
                telephone = input("Digite o Novo número de Telefone do Cliente:")
                telephone = telephone.replace(".", "")
                telephone = telephone.replace("-", "")
                if telephone is not "":
                    while telephone.isdigit() is False:
                        print("_" * 80)
                        print("Por favor digite o Novo Número do Telefone corretamente.")
                        telephone = input("Digite o Novo número de Telefone do Cliente:")
                        telephone = telephone.replace(".", "")
                        telephone = telephone.replace("-", "")

                self.update_telephone(cpf, telephone, user_id)

            elif choice == "8":
                cellphone = input("Digite o Novo Número do Celular do Cliente com o DD: ")
                cellphone = cellphone.replace(".", "")
                cellphone = cellphone.replace("-", "")
                while cellphone.isdigit() is False or cellphone is "":
                    print("_" * 80)
                    print("Por favor digite o Novo Número do Celular Do Cliente corretamente.")
                    cellphone = input("Digite o Novo Número do Celular do Cliente com o DD: ")
                    cellphone = cellphone.replace(".", "")
                    cellphone = cellphone.replace("-", "")

                self.update_cellphone(cpf, cellphone, user_id)

            elif choice == "9":
                rg = input("Digite o Novo Número do RG do Cliente: ")
                rg = rg.replace(".", "")
                rg = rg.replace("-", "")
                check_rg = self.check_rg(rg)

                while rg.isdigit() is False or len(rg) != 9 or check_rg is not None:
                    print("_"*80)
                    print("Por favor digite o Novo Número do RG do Cliente corretamente ou\n"
                          "Este RG já está sendo usado.")
                    rg = input("Digite o Novo Número do RG do Cliente: ")
                    rg = rg.replace(".", "")
                    rg = rg.replace("-", "")
                    check_rg = self.check_rg(rg)

                self.update_rg(cpf, rg, user_id)

            elif choice == "10":
                print("_"*80)
                print("Você Deseja Alterar o Número do CPF do Cliente.")
                cpf_changed = input("Digite o Novo Número do CPF do Cliente: ")
                cpf_changed = cpf_changed.replace(".", "")
                cpf_changed = cpf_changed.replace("-", "")
                cpf_validate = self.return_id(cpf_changed)
                analsying_cpf = validate.validate_number_cpf_employee(cpf_changed)

                while cpf_changed.isdigit() is False or len(cpf_changed) != 11 or \
                        cpf_validate is not None or analsying_cpf == 0:
                    print("_" * 80)
                    print("Por favor digite o Novo Número do CPF do Cliente corretamente ou\n "
                          "Este CPF já está cadastrado no Sistema.")
                    cpf_changed = input("Digite o Novo Número do CPF do Cliente: ")
                    cpf_changed = cpf_changed.replace(".", "")
                    cpf_changed = cpf_changed.replace("-", "")
                    cpf_validate = self.return_id(cpf_changed)
                    analsying_cpf = validate.validate_number_cpf_employee(cpf_changed)

                self.update_cpf(cpf, cpf_changed, user_id)

        else:
            print("_"*80)
            print("Opção inválida.")

    def delete_customer(self):
        print("_"*80)
        cpf = validate.validate_customer_cpf()
        confirm = input("Deseja realmente excluir este Registro: (S -Sim / N - Não):")
        confirm = confirm.upper()
        if confirm == 'S':
            self.delete(cpf)

        else:
            print("_"*80)
            print("O registro não foi deletado.")
            print("Saindo do Sistema até próxima.")

    def select_all_customers(self):
        print("_" * 80)
        self.select_all()

    def search_customer_name(self):
        print("_" * 80)
        name = input("Digite o Nome do Cliente que deseja procurar: ")
        while name is "" or name.isalpha() is False:
            print("_"*80)
            print("Por favor digite o Nome do Cliente. ")
            name = input("Digite o Nome do Cliente que deseja procurar: ")

        self.search_customer(name)


"""customer = CustomerMenu()
customer.customer_menu()"""
