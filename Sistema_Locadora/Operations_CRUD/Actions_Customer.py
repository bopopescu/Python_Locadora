from Sistema_Locadora.Connection_DataBase.Connection import Connection
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow


class Customer(Connection):

    global date_hour
    date_hours = DateHourNow()
    date_hour = date_hours.get_date_hour_now()

    def validate_number_cpf(self, cpf):
        try:
            sql = f"SELECT VALIDAR_CPF_F('{cpf}');"
            self.cursor.execute(sql)
            cpf_validate = self.cursor.fetchone()

            if cpf_validate is not None:
                return cpf_validate[0]
            else:
                return None
        except():
            print("_"*80)
            print("Erro ao tentar chamar a função de validar o CPF.")
            self.close_connection()

    def return_id(self, cpf):
        try:
            select_customer_id = "SELECT ID_CLIENTE FROM CLIENTE WHERE CPF = '{0}';".format(cpf)
            self.cursor.execute(select_customer_id)
            customer_id = self.cursor.fetchone()

            if customer_id is not None:
                return customer_id[0]
            else:
                return None

        except():
            print("_"*80)
            print("Erro ao recuperar o ID do Cliente.")
            self.close_connection()

    def check_rg(self, rg):
        try:
            rg = rg.replace(".", "")
            rg = rg.replace("-", "")

            sql = "SELECT RG FROM CLIENTE WHERE RG = '{0}';".format(rg)
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
            checking_rg = self.check_rg(datas[8])
            customer_id = self.return_id(datas[9])

            if customer_id is None and checking_rg is None:
                sql = ("INSERT INTO CLIENTE(NOME,IDADE,RUA,NUMERO,COMPLEMENTO,CEP,TELEFONE,CELULAR,RG,CPF,DATA_CRIACAO,"
                       "DATA_ATUALIZACAO, ID_USUARIO)"
                       "VALUES('{0}',{1},'{2}','{3}','{4}'" 
                       ",'{5}','{6}','{7}','{8}','{9}','{10}','{11}',{12});".
                       format(datas[0], datas[1], datas[2], datas[3], datas[4], datas[5], datas[6], datas[7],
                              datas[8], datas[9], date_hour, date_hour, datas[10]))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Registro do Cliente: {0} foi cadastrado com sucesso." .format(datas[0]))

            elif customer_id is not None:
                print("_" * 80)
                print(f"Já Existe um Cliente usando este CPF: "
                      f"{datas[9]} já está cadastrado no sistema, por favor verifique! ")

            elif checking_rg is not None:
                print("_"*80)
                print(f"Este RG: {datas[8]} já está sendo usado por um Usuário no Sistema, por favor verifique!")

            elif customer_id is not None and checking_rg is not None:
                print("_"*80)
                print("Já existe um Cliente Utilizando tanto este CPF quanto este RG.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o insert na tabela de Cliente")
        finally:
            self.close_connection()

    def update_name(self, cpf, name, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET NOME = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(name, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Nome do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_age(self, cpf, age, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET IDADE = {0},DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(age, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A Idade do cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_street(self, cpf, street, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET RUA = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(street, date_hour,  user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Nome da Rua do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_number(self, cpf, number, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET NUMERO = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(number, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Número da Rua do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_complement(self, cpf, complement, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET COMPLEMENTO = '{0}' , DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(complement, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Complemento do Endereço do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_cep(self, cpf, cep, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET CEP = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(cep, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O CEP do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_telephone(self, cpf, telephone, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET TELEFONE = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(telephone, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Telefone do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_cellphone(self, cpf, cellphone, user_id):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET CELULAR = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(cellphone, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Número do Celular do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_rg(self, cpf, rg, user_id):
        try:
            customer_id = self.return_id(cpf)
            check_rg = self.check_rg(rg)

            if customer_id is not None and check_rg is None:
                sql = ("UPDATE CLIENTE "
                       "SET RG = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(rg, date_hour, user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Número do RG do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def update_cpf(self, cpf_current, cpf_changed, user_id):
        try:
            customer_id = self.return_id(cpf_current)

            if customer_id is not None:
                sql = ("UPDATE CLIENTE "
                       "SET CPF = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2} "
                       "WHERE 1 = 1 AND ID_CLIENTE = {3}; "
                       .format(cpf_changed, date_hour,  user_id, customer_id))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Número do CPF do Cliente foi alterado com sucesso ")

            else:
                print("_" * 80)
                print("Este Cliente não está cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update na tabela de Cliente.")
        finally:
            self.close_connection()

    def delete(self, cpf):
        try:
            customer_id = self.return_id(cpf)

            if customer_id is not None:
                sql = ("DELETE FROM CLIENTE WHERE ID_CLIENTE = {0};".format(customer_id))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O cliente foi deletado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe registro para este cliente.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o delete na tabela de Cliente.")
        finally:
            self.close_connection()

    def select_all(self):
        try:
            sql = "SELECT * FROM CLIENTES_CADASTRADOS ORDER BY NOME,ID_CLIENTE;"
            self.cursor.execute(sql)
            registers_all = self.cursor.fetchall()

            print("\t \t \t Clientes")
            print("_" * 80)
            for registers in registers_all:
                customer_id = registers[0]
                name = registers[1]
                age = registers[2]
                street = registers[3]
                number = registers[4]
                complement = registers[5]
                cep = registers[6]
                telephone = registers[7]
                cellphone = registers[8]
                rg = registers[9]
                cpf = registers[10]
                create_date = registers[11]
                update_date = registers[12]
                user_id = registers[13]

                print(f"Código do Cliente: {customer_id} ")
                print(f"Nome do Cliente: {name.title()}")
                print(f"Idade: {age}")
                print(f"Rua: {street.title()}")
                print(f"Número: {number}")

                if complement is None:
                    print(f"Complemento: {complement}")
                else:
                    print(f"Complemento: {complement.title()}")

                print(f"CEP: {cep}")
                print(f"Telefone: {telephone}")
                print(f"Celular: {cellphone}")
                print(f"RG: {rg}")
                print(f"CPF: {cpf}")
                print(f"Data de Criação: {create_date}")
                print(f"Data de Alteração: {update_date}")
                print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                print("_" * 80)

            if len(registers_all) > 1:
                print(f"Quantidade de Clientes Cadastrados: {len(registers_all)} ")

            elif len(registers_all) == 1:
                print(f"Você tem somente 1 cliente cadastrado: {len(registers_all)} ")

            else:
                print("Nenhum cliente cadastrado.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o select na tabela de Cliente.")
        finally:
            self.close_connection()

    def search_customer(self, name):
        try:
            sql = f"SELECT * FROM CLIENTES_CADASTRADOS WHERE UPPER(NOME) LIKE '%{name.upper()}%' ORDER BY NOME;"
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()
            if datas is not None:
                print("_" * 80)
                for registers in datas:
                    customer_id = registers[0]
                    name = registers[1]
                    age = registers[2]
                    street = registers[3]
                    number = registers[4]
                    complement = registers[5]
                    cep = registers[6]
                    telephone = registers[7]
                    cellphone = registers[8]
                    rg = registers[9]
                    cpf = registers[10]
                    create_date = registers[11]
                    update_date = registers[12]
                    user_id = registers[13]

                    print(f"Código do Cliente: {customer_id} ")
                    print(f"Nome do Cliente: {name.title()}")
                    print(f"Idade: {age}")
                    print(f"Rua: {street.title()}")
                    print(f"Número: {number}")

                    if complement is None:
                        print(f"Complemento: {complement}")
                    else:
                        print(f"Complemento: {complement.title()}")

                    print(f"CEP: {cep}")
                    print(f"Telefone: {telephone}")
                    print(f"Celular: {cellphone}")
                    print(f"RG: {rg}")
                    print(f"CPF: {cpf}")
                    print(f"Data de Criação: {create_date}")
                    print(f"Data de Alteração: {update_date}")
                    print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                    print("_" * 80)

                if len(datas) > 1:
                    print(f"Quantidade de Clientes Cadastrados: {len(datas)} ")

                elif len(datas) == 1:
                    print(f"Você tem somente 1 cliente cadastrado: {len(datas)} ")

                else:
                    print("Nenhum cliente cadastrado.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar a busca pelo o cliente{0}".format(name))
        finally:
            self.close_connection()


"""
lista=[]
lista.append('Breno de Sales')
lista.append(35)
lista.append('MARIA DE MENDES')
lista.append(133)
lista.append(None)
lista.append('04877121')
lista.append(None)
lista.append('987880985')
lista.append('098765494')
lista.append('19876543212')
"""
# customer = Customer()
# customer.return_id('19876543212')
# customer.insert(lista)
# customer.select_all()
# customer.update(lista)
# customer.search_customer("a")
# customer.delete('19876543212')
