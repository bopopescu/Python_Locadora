from Sistema_Locadora.Operations_CRUD.Actions_Employee import Employee
from Sistema_Locadora.Getters_Setters.Employees_Getters_Setters import EmployeeGetSet
from Sistema_Locadora.Menus.Validates_Menu import Validate
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow


class EmployeeMenu(Employee):

    global validate, date_get
    validate = Validate()
    date_get = DateHourNow()

    def employee_menu(self, user_id):
        print("_"*80)
        choose = input("\t \t \t Menu de Funcionários\n\n " + "_"*80 + "\n "
                       "1º Consultar Todos os Funcionários Cadastrados\n 2º Pesquisar por um Funcionário\n "
                       "3º Cadastrar um Novo Funcionário\n 4º Alterar Dados de um Funcionário\n "
                       "5º Excluir um Funcionário\n 6º Sair do Sistema\n Escolha a sua opção --> ")
        while choose not in("1", "2", "3", "4", "5", "6"):
            validate.validate_text_while()
            choose = input("\t \t \t Menu de Funcionários\n\n " + "_" * 80 + "\n "
                           "1º Consultar Todos os Funcionários Cadastrados\n 2º Pesquisar por um Funcionário\n "
                           "3º Cadastrar um Novo Funcionário\n 4º Alterar Dados de um Funcionário\n "
                           "5º Excluir um Funcionário\n 6º Sair do Sistema\n Escolha a sua opção --> ")

        if choose == "1":
            self.select_all_employee()

        elif choose == "2":
            self.search_for_employee()

        elif choose == "3":
            self.insert_employee(user_id)

        elif choose == "4":
            self.update_datas_employee(user_id)

        elif choose == "5":
            self.delete_employee()

        elif choose == "6":
            print("_"*80)
            print("Saindo do Sistema...")
            exit()

    def insert_employee(self, user_id):
        datas_employee = []
        gross_salary_format = 0
        print("_"*80)
        name_employee = input("Digite o Nome do Novo Funcionário: ")
        while name_employee is "" or name_employee.isdigit():
            print("_"*80)
            print("Por favor Preencha o Nome do Funcionário.")
            name_employee = input("Digite o Nome do Novo Funcionário: ")

        birthday = input("Digite a Data de Nascimento: ")
        birthday_validate = validate.validation_date_insert(birthday)
        while birthday_validate is None:
            print("_"*80)
            print("Por Favor Digite uma Data de Nascimento válida.")
            birthday = input("Digite a Data de Nascimento: ")
            birthday_validate = validate.validation_date_insert(birthday)

        age = input("Digite a Idade do Funcionário: ")
        while age.isdigit() is False:
            print("_"*80)
            print("Por Favor Digite a Idade do Funcionário Corretamente.")
            age = input("Digite a Idade do Funcionário: ")

        sex = input("Digite o Sexo do Funcionário: ")
        sex = sex.title()

        if sex is "":
            sex = "M"
            sex_validate = sex

        else:
            while sex not in("Masculino", "Feminino"):
                print("_"*80)
                print("Por Favor Digite o Sexo do Funcionário Corretamente.")
                sex = input("Digite o Sexo do Funcionário: ")
                sex = sex.title()

            if sex == "Feminino":
                sex_validate = "F"

            else:
                sex_validate = "M"

        rg = input("Digite o Número do RG do Funcionário: ")
        rg = rg.replace(".", "")
        rg = rg.replace("-", "")
        check_rg = self.check_rg(rg)
        while rg.isdigit() is False or len(rg) != 9 or check_rg is not None:
            print("_" * 80)
            print("Por favor digite o Número do RG do Funcionário corretamente ou\n"
                  "Este RG já está sendo usado no Sistema.")
            rg = input("Digite o Número do RG do Cliente: ")
            rg = rg.replace(".", "")
            rg = rg.replace("-", "")
            check_rg = self.check_rg(rg)

        cpf = input("Digite o Número do CPF do Funcionário: ")
        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")
        cpf_validate = self.return_id(cpf)
        analsying_cpf = validate.validate_number_cpf_employee(cpf)
        while cpf.isdigit() is False or len(cpf) != 11 or cpf_validate is not None or analsying_cpf == 0:
            print("_" * 80)
            print("Por favor digite o Número do CPF do Funcionário corretamente ou\n"
                  "Este CPF já está sendo usado no Sistema.")
            cpf = input("Digite o Número do CPF do Cliente: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            cpf_validate = self.return_id(cpf)
            analsying_cpf = validate.validate_number_cpf_employee(cpf)

        telephone = input("Digite o Número do Telefone do Funcionário: ")
        telephone = telephone.replace(".", "")
        telephone = telephone.replace("-", "")
        telephone = telephone.replace("/", "")
        if telephone is "":
            telephone = None

        else:
            while telephone.isdigit() is False:
                print("_"*80)
                print("Por Favor Digite o Número do Telefone corretamente.")
                telephone = input("Digite o Número do Telefone do Funcionário: ")
                telephone = telephone.replace(".", "")
                telephone = telephone.replace("-", "")
                telephone = telephone.replace("/", "")

        cellphone = input("Digite o Número do Celular do Funcionário: ")
        cellphone = cellphone.replace(".", "")
        cellphone = cellphone.replace("-", "")
        cellphone = cellphone.replace("/", "")
        if cellphone is "":
            cellphone = None

        else:
            while cellphone.isdigit() is False or cellphone.count("9") == 0:
                print("_"*80)
                print("Por Favor Digite o Número do Celular corretamente.")
                cellphone = input("Digite o Número do Celular do Funcionário: ")
                cellphone = cellphone.replace(".", "")
                cellphone = cellphone.replace("-", "")
                cellphone = cellphone.replace("/", "")

        street = input("Digite o Nome da Rua do Funcionário: ")
        street = street.title()
        while street is "":
            print("_"*80)
            print("Por Favor Digite o Nome da Rua.")
            street = input("Digite o Nome da Rua do Funcionário: ")
            street = street.title()

        number = input("Digite o Número da Casa do Funcionário: ")
        while number.isdigit() is False:
            print("_"*80)
            print("Por Favor Digite o Número da Casa do Funcionário.")
            number = input("Digite o Número da Casa do Funcionário: ")

        complement = input("Digite o Complemento do Endereço do Funcionário: ")
        if complement is "":
            complement = None

        cep = input("Digite o CEP do Funcionário: ")
        cep = cep.replace(".", "").replace("-", "").replace("/", "").replace("\\", "")
        while cep.isdigit() is False or cep is "" or len(cep) != 8:
            print("_"*80)
            print("Por favor digite o CEP do Funcionário corretamente.")
            cep = input("Digite o CEP do Funcionário: ")
            cep = cep.replace(".", "").replace("-", "").replace("/", "").replace("\\", "")

        qty_days = input("Digite a Quantidade de Dias que o Funcionário Irá Trabalhar: ")
        if qty_days is "":
            qty_days = "6"
        else:
            while qty_days.isdigit() is False or qty_days == "0":
                print("_"*80)
                print("Por Favor Digite Um Valor Válido Para Quantidade de Dias trabalhados.")
                qty_days = input("Digite a Quantidade de Dias que o Funcionário Irá Trabalhar: ")

        entry_time = input("Digite a Horário de Entrada do Funcionário: ")
        entry_time_format = validate.validate_schedule(entry_time)
        if entry_time_format is None:
            entry_time_format = str("09:00:00")

        departure_hour = input("Digite o Horário de Saída do Funcionário: ")
        departure_hour_format = validate.validate_schedule(departure_hour)
        if departure_hour_format is None:
            departure_hour_format = str("18:00:00")

        gross_salary = input("Digite o valor do Salário Bruto do Funcionário: ")
        gross_salary = gross_salary.replace(",", ".")

        if gross_salary is "":
            gross_salary = "500"
            gross_salary_format = gross_salary

        else:
            try:
                gross_salary_format = float(gross_salary)

            except ValueError:
                print("_"*80)
                print("Por Favor Digite Somente Números.")

        job_role = input("Digite o Cargo Do Funcionário: ")
        job_role = job_role.title()
        if job_role is "":
            job_role = "Atendente"

        vt = input("O Funcionário Irá Usar Vale Transporte (S - Sim / N - Não): ")
        vt = vt.upper()
        if vt is "":
            vt = "Y"

        else:
            if vt == "S":
                vt = "Y"

            else:
                while vt not in("Y", "N"):
                    print("_"*80)
                    print("Por Favor Digite Apenas as Opções (S - Sim ou N - Não): ")
                    vt = input("O Funcionário Irá Usar Vale Transporte (S - Sim / N - Não): ")
                    vt = vt.upper()

        employee_get_set = EmployeeGetSet(name_employee, birthday_validate, int(age), sex_validate, rg, cpf,
                                          telephone, cellphone, street, number, complement, cep, int(qty_days),
                                          entry_time_format, departure_hour_format, gross_salary_format, job_role, vt
                                          , user_id)

        datas_employee.append(employee_get_set.name)
        datas_employee.append(employee_get_set.birthday)
        datas_employee.append(employee_get_set.age)
        datas_employee.append(employee_get_set.sex)
        datas_employee.append(employee_get_set.rg)
        datas_employee.append(employee_get_set.cpf)
        datas_employee.append(employee_get_set.telephone)
        datas_employee.append(employee_get_set.cellphone)
        datas_employee.append(employee_get_set.street)
        datas_employee.append(employee_get_set.number)
        datas_employee.append(employee_get_set.complement)
        datas_employee.append(employee_get_set.cep)
        datas_employee.append(employee_get_set.quantity_days)
        datas_employee.append(employee_get_set.entry_hour)
        datas_employee.append(employee_get_set.departure_hour)
        datas_employee.append(employee_get_set.salary)
        datas_employee.append(employee_get_set.job_role)
        datas_employee.append(employee_get_set.vt)
        datas_employee.append(employee_get_set.user_id)

        self.insert(datas_employee)

    def update_datas_employee(self, user_id):
        print("_" * 80)
        choice = input("\t \t \t Menu de Alterações de Dados de Funcionário\n\n " + "_"*80 + "\n "
                       "1º Alterar o Nome\n 2º Alterar a Data de Nascimento\n 3º Alterar a Idade\n 4º Alterar o Sexo\n"
                       " 5º Alterar o RG\n 6º Alterar o CPF\n 7º Alterar o Telefone\n "
                       "8º Alterar o Celular\n 9º Alterar a Rua\n "
                       "10º Alterar o Número do Endereço\n 11º Alterar o Complemento do Endereço\n 12º Alterar o CEP\n"
                       " 13º Alterar a Quantidade de Dias a Trabalhar por Semana\n 14º Alterar o Horário de Entrada\n"
                       " 15º Alterar o Horário de Saída\n 16º Alterar o Salário Bruto\n "
                       "17º Alterar o Cargo do Funcionário\n"
                       " 18º Alterar Se o Funcionário Utiliza Vale Transporte(VT)\n 19º Sair do Sistema\n"
                       " Escolha a sua opção --> ")

        if choice in("1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"):

            gross_salary_format = 0
            print("_" * 80)
            cpf_current_employee = validate.validate_employee_cpf()

            if choice == "1":
                name_employee = input("Digite o Nome do Novo Funcionário: ")
                while name_employee is "" or name_employee.isdigit():
                    print("_" * 80)
                    print("Por favor Preencha o Nome do Funcionário.")
                    name_employee = input("Digite o Nome do Novo Funcionário: ")
                self.update_name(cpf_current_employee, name_employee, user_id)

            elif choice == "2":
                birthday = input("Digite a Data de Nascimento: ")
                birthday_validate = validate.validation_date_insert(birthday)
                while birthday_validate is None:
                    print("_" * 80)
                    print("Por Favor Digite uma Data de Nascimento válida.")
                    birthday = input("Digite a Data de Nascimento: ")
                    birthday_validate = validate.validation_date_insert(birthday)
                self.update_birthday(cpf_current_employee, birthday_validate, user_id)

            elif choice == "3":
                age = input("Digite a Idade do Funcionário: ")
                while age.isdigit() is False:
                    print("_" * 80)
                    print("Por Favor Digite a Idade do Funcionário Corretamente.")
                    age = input("Digite a Idade do Funcionário: ")
                self.update_age(cpf_current_employee, age, user_id)

            elif choice == "4":
                sex = input("Digite o Sexo do Funcionário: ")
                sex = sex.title()
                while sex not in ("Masculino", "Feminino"):
                    print("_" * 80)
                    print("Por Favor Digite o Sexo do Funcionário Corretamente.")
                    sex = input("Digite o Sexo do Funcionário: ")
                    sex = sex.title()

                if sex == "Feminino":
                    sex_validate = "F"

                else:
                    sex_validate = "M"
                self.update_sex(cpf_current_employee, sex_validate, user_id)

            if choice == "5":
                rg = input("Digite o Número do RG do Funcionário: ")
                rg = rg.replace(".", "")
                rg = rg.replace("-", "")
                check_rg = self.check_rg(rg)
                while rg.isdigit() is False or len(rg) != 9 or check_rg is not None:
                    print("_" * 80)
                    print("Por favor digite o Número do RG do Funcionário corretamente ou\n"
                          "Este RG já está sendo usado no Sistema.")
                    rg = input("Digite o Número do RG do Cliente: ")
                    rg = rg.replace(".", "")
                    rg = rg.replace("-", "")
                    check_rg = self.check_rg(rg)

                self.update_rg(cpf_current_employee, rg, user_id)

            elif choice == "6":
                print("_"*80)
                cpf_new = input("Digite o Novo Número do CPF do Funcionário: ")
                cpf_new = cpf_new.replace(".", "")
                cpf_new = cpf_new.replace("-", "")
                cpf_validate = self.return_id(cpf_new)
                analsying_cpf = validate.validate_number_cpf_employee(cpf_new)
                while cpf_new.isdigit() is False or len(cpf_new) != 11 or \
                        cpf_validate is not None or analsying_cpf == 0:
                    print("_" * 80)
                    print("Por favor digite o Número do CPF do Funcionário corretamente ou\n"
                          "Este CPF já está sendo usado no Sistema.")
                    cpf_new = input("Digite o Novo Número do CPF do Cliente: ")
                    cpf_new = cpf_new.replace(".", "")
                    cpf_new = cpf_new.replace("-", "")
                    cpf_validate = self.return_id(cpf_new)
                    analsying_cpf = validate.validate_number_cpf_employee(cpf_new)

                self.update_cpf(cpf_current_employee, cpf_new, user_id)

            elif choice == "7":
                telephone = input("Digite o Número do Telefone do Funcionário: ")
                telephone = telephone.replace(".", "")
                telephone = telephone.replace("-", "")
                telephone = telephone.replace("/", "")
                while telephone.isdigit() is False:
                    print("_" * 80)
                    print("Por Favor Digite o Número do Telefone corretamente.")
                    telephone = input("Digite o Número do Telefone do Funcionário: ")
                    telephone = telephone.replace(".", "")
                    telephone = telephone.replace("-", "")
                    telephone = telephone.replace("/", "")
                self.update_telephone(cpf_current_employee, telephone, user_id)

            elif choice == "8":
                cellphone = input("Digite o Número do Celular do Funcionário: ")
                cellphone = cellphone.replace(".", "")
                cellphone = cellphone.replace("-", "")
                cellphone = cellphone.replace("/", "")
                while cellphone.isdigit() is False or cellphone[0].count("9") == 0:
                    print("_" * 80)
                    print("Por Favor Digite o Número do Celular corretamente.")
                    cellphone = input("Digite o Número do Celular do Funcionário: ")
                    cellphone = cellphone.replace(".", "")
                    cellphone = cellphone.replace("-", "")
                    cellphone = cellphone.replace("/", "")
                self.update_cellphone(cpf_current_employee, cellphone, user_id)

            elif choice == "9":
                street = input("Digite o Nome da Rua do Funcionário: ")
                street = street.title()
                while street is "":
                    print("_" * 80)
                    print("Por Favor Digite o Nome da Rua.")
                    street = input("Digite o Nome da Rua do Funcionário: ")
                    street = street.title()
                self.update_street(cpf_current_employee, street, user_id)

            elif choice == "10":
                number = input("Digite o Número da Casa do Funcionário: ")
                while number.isdigit() is False or number == "0":
                    print("_" * 80)
                    print("Por Favor Digite o Número da Casa do Funcionário.")
                    number = input("Digite o Número da Casa do Funcionário: ")
                self.update_number_street(cpf_current_employee, number, user_id)

            elif choice == "11":
                complement = input("Digite o Complemento do Endereço do Funcionário: ")
                while complement is "":
                    print("_"*80)
                    print("Por Favor Digite um Complemento para O Endereço.")
                    complement = input("Digite o Complemento do Endereço do Funcionário: ")
                self.update_complement(cpf_current_employee, complement, user_id)

            elif choice == "12":
                cep = input("Digite o CEP do Funcionário: ")
                cep = cep.replace(".", "").replace("-", "").replace("/", "").replace("\\", "")
                while cep.isdigit() is False or cep is "" or len(cep) != 8:
                    print("_" * 80)
                    print("Por favor digite o CEP do Funcionário corretamente.")
                    cep = input("Digite o CEP do Funcionário: ")
                    cep = cep.replace(".", "").replace("-", "").replace("/", "").replace("\\", "")
                self.update_cep(cpf_current_employee, cep, user_id)

            elif choice == "13":
                qty_days = input("Digite a Quantidade de Dias que o Funcionário Irá Trabalhar: ")
                while qty_days.isdigit() is False or qty_days == "0":
                    print("_" * 80)
                    print("Por Favor Digite Um Valor Válido Para Quantidade de Dias trabalhados.")
                    qty_days = input("Digite a Quantidade de Dias que o Funcionário Irá Trabalhar: ")
                self.update_qty_days(cpf_current_employee, qty_days, user_id)

            elif choice == "14":
                entry_time = input("Digite a Horário de Entrada do Funcionário: ")
                entry_time_format = validate.validate_schedule(entry_time)
                while entry_time_format is None:
                    print("_"*80)
                    print("Por Favor Digite Um Horário de Entrada válido.")
                    entry_time = input("Digite a Data de Entrada do Funcionário: ")
                    entry_time_format = validate.validate_schedule(entry_time)
                self.update_entry_hour(cpf_current_employee, entry_time_format, user_id)

            elif choice == "15":
                departure_hour = input("Digite o Horário de Saída do Funcionário: ")
                departure_hour_format = validate.validate_schedule(departure_hour)
                while departure_hour_format is None:
                    print("_"*80)
                    print("Por Favor Digite um Horário de Saída válido.")
                    departure_hour = input("Digite o Horário de Saída do Funcionário: ")
                    departure_hour_format = validate.validate_schedule(departure_hour)
                self.update_departure_hour(cpf_current_employee, departure_hour_format, user_id)

            elif choice == "16":
                gross_salary = input("Digite o valor do Salário Bruto do Funcionário: ")
                gross_salary = gross_salary.replace(",", ".")

                while gross_salary is "":
                    print("_"*80)
                    print("Por Favor Digite o Valor Do Salário Bruto Corretamente.")
                    gross_salary = input("Digite o valor do Salário Bruto do Funcionário: ")
                    gross_salary = gross_salary.replace(",", ".")

                try:
                    gross_salary_format = float(gross_salary)
                    self.update_salary(cpf_current_employee, gross_salary_format, user_id)
                except ValueError:
                    print("_" * 80)
                    print("Por Favor Digite Somente Números.")

            elif choice == "17":
                job_role = input("Digite o Cargo Do Funcionário: ")
                job_role = job_role.title()
                while job_role is "":
                    print("_"*80)
                    print("Por Favor Digite O Cargo Do Funcionário Corretamente.")
                    job_role = input("Digite o Cargo Do Funcionário: ")
                    job_role = job_role.title()
                self.update_job_role(cpf_current_employee, job_role, user_id)

            elif choice == "18":
                vt = input("O Funcionário Irá Usar Vale Transporte (S - Sim / N - Não): ")
                vt = vt.upper()
                while vt not in ("S", "N"):
                    print("_" * 80)
                    print("Por Favor Digite Apenas as Opções (S - Sim ou N - Não): ")
                    vt = input("O Funcionário Irá Usar Vale Transporte (S - Sim / N - Não): ")
                    vt = vt.upper()
                if vt == "S":
                    vt = "Y"
                self.update_vt(cpf_current_employee, vt, user_id)

            elif choice == "19":
                print("_"*80)
                print("Saindo do Sistema...")
                exit()

        else:
            print("_"*80)
            print("Opção inválida.")

    def delete_employee(self):
        print("_"*80)
        cpf_validate = validate.validate_employee_cpf()
        confirm = input("Deseja Realmente Excluir este Registro ? (S - Sim / N - Não): ")
        confirm = confirm.upper()
        if confirm == "S":
            self.delete(cpf_validate)

        else:
            print("_"*80)
            print("O Registro não foi deletado.")
            print("Saindo do Sistema.")

    def select_all_employee(self):
        print("_" * 80)
        self.select_all()

    def search_for_employee(self):
        print("_" * 80)
        options = input("\t \t \t Escolha Por qual campo buscar o Funcionário \n 1º Buscar por Nome\n "
                        "2º Buscar pelo o Código do Funcionário\n Escolha a sua opção --> ")

        while options not in("1", "2"):
            validate.validate_text_while()
            options = input("\t \t \t Escolha Por qual campo buscar o Funcionário \n 1º Buscar por Nome\n "
                            "2º Buscar pelo o Código do Funcionário\n Escolha a sua opção --> ")

        print("_"*80)
        if options is "1":
            name_employee = input("Digite o nome do Funcionário: ")
            while name_employee is "":
                print("_"*80)
                print("Por favor digite o Nome do Funcionário.")
                name_employee = input("Digite o nome do Funcionário: ")
            self.search_employee(name_employee)

        elif options is "2":
            id_employee = input("Digite o Código do Funcionário: ")
            while id_employee.isdigit() is False:
                print("_" * 80)
                print("Por favor digite o Código do Funcionário.")
                id_employee = input("Digite o Código do Funcionário: ")
            self.search_id_func(id_employee)


"""employee_menu = EmployeeMenu()
employee_menu.employee_menu()"""
