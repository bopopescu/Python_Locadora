from Sistema_Locadora.Connection_DataBase.Connection import Connection
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow
from Sistema_Locadora.Operations_CRUD.Actions_Customer import Customer


class Employee(Connection):

    global date_hour
    now = DateHourNow()
    date_hour = now.get_date_hour_now()

    @staticmethod
    def validate_number_cpf(cpf):
        validate_number_cpf = Customer()
        cpf_number_validate = validate_number_cpf.validate_number_cpf(cpf)
        return cpf_number_validate

    def return_id(self, cpf):
        try:
            sql = "SELECT ID_FUNC FROM FUNCIONARIO WHERE CPF = '{0}';".format(cpf)
            self.cursor.execute(sql)
            id_func = self.cursor.fetchone()

            if id_func is not None:
                return id_func[0]

            else:
                return None

        except():
            print("_"*80)
            print("Erro ao tentar recuperar os dados do funcionário.")

    def return_job_rule(self, cpf):
        id_func = self.return_id(cpf)
        sql = "SELECT RETORNA_CARGO_F({0})".format(id_func)
        self.cursor.execute(sql)
        job_rule = self.cursor.fetchone()

        if job_rule is not None:
            return job_rule[0]

        else:
            return None

    def check_rg(self, rg):
        try:
            rg = rg.replace(".", "")
            rg = rg.replace("-", "")

            sql = "SELECT RG FROM FUNCIONARIO WHERE RG = '{0}';".format(rg)
            self.cursor.execute(sql)
            rg = self.cursor.fetchone()

            if rg is not None:
                return rg

            else:
                return None

        except():
            print("_"*80)
            print("Erro ao Tentar Checar o Número do RG.")
            self.close_connection()

    def insert(self, datas=[]):
        try:
            id_func = self.return_id(datas[5])
            check_rg = self.check_rg(datas[4])

            if id_func is None and check_rg is None:
                sql = ("INSERT INTO FUNCIONARIO(NOME,DATA_NAS,IDADE,SEXO,RG,CPF,TELEFONE,CELULAR,RUA,NUMERO,"
                       "COMPLEMENTO,CEP,QTDE_DIAS,HORARIO_ENTRADA,HORARIO_SAIDA,SALARIO_BRUTO,CARGO,DATA_CRIACAO,"
                       "DATA_ATUALIZACAO,VT, ID_USUARIO)""VALUES('{0}','{1}',{2},'{3}','{4}','{5}','{6}','{7}','{8}',"
                       "'{9}','{10}','{11}',{12}"",'{13}','{14}',{15},'{16}','{17}','{18}','{19}',{20});"
                       .format(datas[0], datas[1], datas[2], datas[3], datas[4], datas[5], datas[6], datas[7],
                               datas[8], datas[9], datas[10], datas[11], datas[12], datas[13], datas[14], datas[15],
                               datas[16], date_hour, date_hour, datas[17], datas[18]))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O Novo Funcionário: {0} foi cadastrado com sucesso.".format(datas[0].title()))

            else:
                print("_"*80)
                print("O registro para o funcionário: {0} já existe cadastrado.".format(datas[0].title()))

        except():
            print("_"*80)
            print("Erro ao tentar cadastrar o novo Funcionário.")

        finally:
            self.close_connection()

    def update_name(self, cpf, name, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET NOME = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(name, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O Nome do Funcionário foi alterado com sucesso.")

            else:
                print("_"*80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_"*80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_birthday(self, cpf, birthday, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET DATA_NAS = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(birthday, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("A Data de Nascimento do Funcionário foi alterada com sucesso.")

            else:
                print("_"*80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_"*80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_age(self, cpf, age, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET IDADE = {0}, DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(age, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A Idade do Funcionário foi alterada com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_sex(self, cpf, sex, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET SEXO = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(sex, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Sexo do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_rg(self, cpf, rg, user_id):
        try:
            id_func = self.return_id(cpf)
            check_rg = self.check_rg(rg)

            if id_func is not None and check_rg is None:
                sql = ("UPDATE FUNCIONARIO SET RG = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(rg, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O RG do Cliente foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_cpf(self, cpf_old, cpf_new, user_id):
        try:
            id_func = self.return_id(cpf_old)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET CPF = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(cpf_new, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O CPF do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_telephone(self, cpf, telephone, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET TELEFONE = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(telephone, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Telefone do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_cellphone(self, cpf, cellphone, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET CELULAR = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(cellphone, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Celular do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_street(self, cpf, street, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET RUA = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(street, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print(" O Nome da Rua do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_number_street(self, cpf, number, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET NUMERO = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(number, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Número da Rua do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_complement(self, cpf, complement, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET COMPLEMENTO = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(complement, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Complemento do Endereço do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_cep(self, cpf, cep, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET CEP = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(cep, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O CEP do Funcionário  foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_qty_days(self, cpf, qty_days, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET QTDE_DIAS = {0}, DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(qty_days, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Quantidade de Dias na Semana de Trabalho foi alterada com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_entry_hour(self, cpf, entry_hour, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET HORARIO_ENTRADA = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(entry_hour, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Horário de Entrada do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_departure_hour(self, cpf, departure_hour, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET HORARIO_SAIDA = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(departure_hour, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Horário de Saída do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_salary(self, cpf, salary, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET SALARIO_BRUTO = {0}, DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(salary, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Salário do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_vt(self, cpf, vt, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET VT = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(vt, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                if vt is 'Y':
                    print("O Vale Transporte do Funcionário foi alterado com sucesso para sim.")
                else:
                    print("O Vale Transporte do Funcionário foi alterado com sucesso para não.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def update_job_role(self, cpf, job_role, user_id):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = ("UPDATE FUNCIONARIO SET CARGO = '{0}', DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_FUNC = {3};".format(job_role, date_hour, user_id, id_func))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Cargo do Funcionário foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe este registro cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar atualizar está informação do funcionário.")
        finally:
            self.close_connection()

    def delete(self, cpf):
        try:
            id_func = self.return_id(cpf)

            if id_func is not None:
                sql = "DELETE FROM FUNCIONARIO WHERE ID_FUNC = {0};".format(id_func)
                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O registro foi deletado com sucesso.")

            else:
                print("_"*80)
                print("Não existe esse registro cadastrado no sistema.")

        except():
            print("_"*80)
            print("Erro ao tentar deletar o registro do funcionário.")
        finally:
            self.close_connection()

    def select_all(self):
        try:
            sql = "SELECT * FROM FUNCIONARIOS_CADASTRADOS ORDER BY NOME;"
            self.cursor.execute(sql)
            registers_all = self.cursor.fetchall()

            print("\t \t \t Funcionários")
            print("_"*80)
            for datas in registers_all:
                id_func = datas[0]
                name = datas[1]
                birthday = datas[2]
                age = datas[3]
                sex = datas[4]
                rg = datas[5]
                cpf = datas[6]
                telephone = datas[7]
                cellphone = datas[8]
                street = datas[9]
                number = datas[10]
                complement = datas[11]
                cep = datas[12]
                qtd_days = datas[13]
                entry_time = datas[14]
                departure_time = datas[15]
                job_role = datas[16]
                vl_transp_vourcher = datas[17]
                vl_pay_inss = datas[18]
                salary_gross = datas[19]
                net_salary = datas[20]
                daily_workload = datas[21]
                weekly_worload = datas[22]
                monthly_workoload = datas[23]
                create_date = datas[24]
                update_date = datas[25]
                user_id = datas[26]

                print(f"Código do Funcionário: {id_func}")
                print(f"Nome: {name.title()}")
                print(f"Data de Nascimento: {birthday}")
                print(f"Idade: {age}")

                if sex is "M":
                    print("Sexo: Masculino")

                else:
                    print("Sexo: Feminino")

                print(f"RG: {rg}")
                print(f"CPF: {cpf}")
                print(f"Telefone: {telephone}")
                print(f"Celular: {cellphone}")
                print(f"Rua: {street.title()}")
                print(f"Número: {number}")

                if complement is not None:
                    print(f"Complemento: {complement.title()}")

                else:
                    print(f"Complemento: {complement}")

                print(f"CEP: {cep}")
                print(f"Quantidade de Dias a trabalhar por semana: {qtd_days}")
                print(f"Horário de Entrada: {entry_time}")
                print(f"Horário de Saída: {departure_time}")
                print(f"Salário Bruto: {salary_gross}")
                print(f"Salário Líquido: {net_salary}")
                print(f"Valor Pago por Mês VT: {vl_transp_vourcher}")
                print(f"Valor Pago por Mês INSS: {vl_pay_inss}")
                print(f"Carga Hóraria Diária: {daily_workload} ")
                print(f"Carga Hóraria Semanal: {weekly_worload}")
                print(f"Carga Hóraria Mensal: {monthly_workoload}")
                print(f"Cargo: {job_role.title()}")
                print(f"Data de Criação: {create_date}")
                print(f"Data de Atualização: {update_date}")
                print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                print("_"*80)

            if len(registers_all) > 1:
                print(f"Quantidade de funcionários: {len(registers_all)}")

            elif len(registers_all) == 1:
                print("Você possuí somente um funcionário cadastrado no sistema.")

            else:
                print("Você não possuí nenhum funcionário cadastrado.")

        except():
            print("_"*80)
            print("Erro ao tentar consultar todos os registros de todos os funcionários.")

        finally:
            self.close_connection()

    def search_employee(self, nome):
        try:
            sql = f"SELECT * FROM FUNCIONARIOS_CADASTRADOS WHERE UPPER(NOME) LIKE '%{nome.upper()}%' ORDER BY NOME;"
            self.cursor.execute(sql)
            registers_all = self.cursor.fetchall()

            print("\t \t \t Funcionários")
            print("_" * 80)
            if registers_all is not None:
                for datas in registers_all:
                    id_func = datas[0]
                    name = datas[1]
                    birthday = datas[2]
                    age = datas[3]
                    sex = datas[4]
                    rg = datas[5]
                    cpf = datas[6]
                    telephone = datas[7]
                    cellphone = datas[8]
                    street = datas[9]
                    number = datas[10]
                    complement = datas[11]
                    cep = datas[12]
                    qtd_days = datas[13]
                    entry_time = datas[14]
                    departure_time = datas[15]
                    job_role = datas[16]
                    vl_transp_vourcher = datas[17]
                    vl_pay_inss = datas[18]
                    salary_gross = datas[19]
                    net_salary = datas[20]
                    daily_workload = datas[21]
                    weekly_worload = datas[22]
                    monthly_workoload = datas[23]
                    create_date = datas[24]
                    update_date = datas[25]
                    user_id = datas[26]

                    print(f"Código do Funcionário: {id_func}")
                    print(f"Nome: {name.title()}")
                    print(f"Data de Nascimento: {birthday}")
                    print(f"Idade: {age}")

                    if sex is "M":
                        print("Sexo: Masculino")

                    else:
                        print("Sexo: Feminino")

                    print(f"RG: {rg}")
                    print(f"CPF: {cpf}")
                    print(f"Telefone: {telephone}")
                    print(f"Celular: {cellphone}")
                    print(f"Rua: {street.title()}")
                    print(f"Número: {number}")

                    if complement is not None:
                        print(f"Complemento: {complement.title()}")

                    else:
                        print(f"Complemento: {complement}")

                    print(f"CEP: {cep}")
                    print(f"Quantidade de Dias a trabalhar por semana: {qtd_days}")
                    print(f"Horário de Entrada: {entry_time}")
                    print(f"Horário de Saída: {departure_time}")
                    print(f"Salário Bruto: {salary_gross}")
                    print(f"Salário Líquido: {net_salary}")
                    print(f"Valor Pago por Mês VT: {vl_transp_vourcher}")
                    print(f"Valor Pago por Mês INSS: {vl_pay_inss}")
                    print(f"Carga Hóraria Diária: {daily_workload} ")
                    print(f"Carga Hóraria Semanal: {weekly_worload}")
                    print(f"Carga Hóraria Mensal: {monthly_workoload}")
                    print(f"Cargo: {job_role.title()}")
                    print(f"Data de Criação: {create_date}")
                    print(f"Data de Atualização: {update_date}")
                    print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                    print("_" * 80)

                if len(registers_all) > 1:
                    print(f"Quantidade de funcionários: {len(registers_all)}")

                elif len(registers_all) == 1:
                    print("Você possuí somente um funcionário cadastrado no sistema.")

                else:
                    print("Você não possuí nenhum funcionário cadastrado com este nome.")

        except():
            print("_" * 80)
            print("Erro ao tentar consultar todos os registros de todos os funcionários.")

        finally:
            self.close_connection()

    def search_id_func(self, id_employee):
        try:
            sql = f"SELECT * FROM FUNCIONARIOS_CADASTRADOS WHERE ID_FUNC = {id_employee};"
            self.cursor.execute(sql)
            datas = self.cursor.fetchone()

            print("\t \t \t Funcionários")
            print("_" * 80)
            if datas is not None:
                id_func = datas[0]
                name = datas[1]
                birthday = datas[2]
                age = datas[3]
                sex = datas[4]
                rg = datas[5]
                cpf = datas[6]
                telephone = datas[7]
                cellphone = datas[8]
                street = datas[9]
                number = datas[10]
                complement = datas[11]
                cep = datas[12]
                qtd_days = datas[13]
                entry_time = datas[14]
                departure_time = datas[15]
                job_role = datas[16]
                vl_transp_vourcher = datas[17]
                vl_pay_inss = datas[18]
                salary_gross = datas[19]
                net_salary = datas[20]
                daily_workload = datas[21]
                weekly_worload = datas[22]
                monthly_workoload = datas[23]
                create_date = datas[24]
                update_date = datas[25]
                user_id = datas[26]

                print(f"Código do Funcionário: {id_func}")
                print(f"Nome: {name.title()}")
                print(f"Data de Nascimento: {birthday}")
                print(f"Idade: {age}")

                if sex is "M":
                    print("Sexo: Masculino")

                else:
                    print("Sexo: Feminino")

                print(f"RG: {rg}")
                print(f"CPF: {cpf}")
                print(f"Telefone: {telephone}")
                print(f"Celular: {cellphone}")
                print(f"Rua: {street.title()}")
                print(f"Número: {number}")

                if complement is not None:
                    print(f"Complemento: {complement.title()}")

                else:
                    print(f"Complemento: {complement}")

                print(f"CEP: {cep}")
                print(f"Quantidade de Dias a trabalhar por semana: {qtd_days}")
                print(f"Horário de Entrada: {entry_time}")
                print(f"Horário de Saída: {departure_time}")
                print(f"Salário Bruto: {salary_gross}")
                print(f"Salário Líquido: {net_salary}")
                print(f"Valor Pago por Mês VT: {vl_transp_vourcher}")
                print(f"Valor Pago por Mês INSS: {vl_pay_inss}")
                print(f"Carga Hóraria Diária: {daily_workload} ")
                print(f"Carga Hóraria Semanal: {weekly_worload}")
                print(f"Carga Hóraria Mensal: {monthly_workoload}")
                print(f"Cargo: {job_role.title()}")
                print(f"Data de Criação: {create_date}")
                print(f"Data de Atualização: {update_date}")
                print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                print("_" * 80)

        except():
            print("_" * 80)
            print("Erro ao tentar consultar todos os registros de todos os funcionários.")

        finally:
            self.close_connection()


"""
dados =[]
dados.append("Beatriz Ferreira de Souza.")
dados.append("1994.06.11")
dados.append(25)
dados.append("F")
dados.append("912345654")
dados.append("12345561890")
dados.append("Null")
dados.append("Null")
dados.append("Bernades de Souza")
dados.append(2102)
dados.append("Null")
dados.append("04212098")
dados.append("Default")
dados.append("18:00:00")
dados.append("22:00:00")
dados.append(990.00)
dados.append("Supervisora de Atendente")
dados.append("Y")
"""

# employee = Employee()
# employee.return_id('12345567890')
# employee.insert(dados)
# employee.select_all()
# employee.search_employee("anA")
# employee.update(dados)
# employee.delete(dados[5])
