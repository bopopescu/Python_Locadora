from Sistema_Locadora.Connection_DataBase.Connection import Connection
from Sistema_Locadora.Operations_CRUD.Actions_Employee import Employee
from Sistema_Locadora.Operations_CRUD.Actions_Customer import Customer
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow
from Sistema_Locadora.Operations_CRUD.Actions_DVD_Game import DvdGame


class RentDvdGame(Connection):

    global date_hour
    now = DateHourNow()
    date_hour = now.get_date_hour_now()

    @staticmethod
    def return_id_cliente(cpf):
        customer = Customer()
        id_customer = customer.return_id(cpf)

        return id_customer

    def check_qty_dvd_game_rent(self, id_dvd_jogo, qty_rent):
        try:
            sql = "SELECT CASE  WHEN SUM(EDJ.QTDE_EMPRESTADO) IS NULL THEN 0 + {0} " \
                  "ELSE SUM(EDJ.QTDE_EMPRESTADO) + {1} END SOMA_QTDE_EMPRESTADA "\
                  "FROM EMPRESTIMO_DVD_JOGO EDJ "\
                  "WHERE EDJ.ID_DVD_JOGO = {2};".format(qty_rent, qty_rent, id_dvd_jogo)
            self.cursor.execute(sql)
            total_qty = self.cursor.fetchone()
            total_qty = total_qty[0]

            if total_qty is None:
                total_qty = 0

            return int(total_qty)

        except():
            print("_"*80)
            print("Erro ao tentar retornar a quantidade de Dvds e Jogos Alugados.")

    @staticmethod
    def check_qty_dvd_game_avaibles(id_dvd_jogo):
        dvd_game = DvdGame()
        check_qty = dvd_game.check_qtde_dvd_games_avaible(id_dvd_jogo)

        if check_qty is not None:
            return check_qty

        else:
            return 0

    @staticmethod
    def return_id_func(cpf):
        employee = Employee()
        id_func = employee.return_id(cpf)
        return id_func

    @staticmethod
    def return_id_dvd_jogo(name_dvd_game):
        dvd_game = DvdGame()
        id_dvd_game = dvd_game.return_id(name_dvd_game)
        return id_dvd_game

    def return_id_empr_dvd_jogo(self, id_cliente, id_dvd_jogo):
        try:
            sql = "SELECT ID_EMP_DVD_JOGO FROM EMPRESTIMO_DVD_JOGO WHERE ID_CLIENTE = {0} " \
                  "AND ID_DVD_JOGO = {1};".format(id_cliente, id_dvd_jogo)
            self.cursor.execute(sql)
            id_emp_dvd_jogo = self.cursor.fetchone()

            if id_emp_dvd_jogo is not None:
                return id_emp_dvd_jogo[0]

            else:
                return None

        except():
            self.close_connection()
            print("_"*80)
            print("Erro ao tentar recuperar o ID do Empréstimo do DVD ou Jogo.")

    def insert(self, datas=[]):
        try:
            id_func = self.return_id_func(datas[2])
            id_cliente = self.return_id_cliente(datas[3])
            id_dvd_jogo = self.return_id_dvd_jogo(datas[4])
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            qty_register_dvd_game = self.check_qty_dvd_game_avaibles(id_dvd_jogo)
            qty_dvd_game_rent = self.check_qty_dvd_game_rent(id_dvd_jogo, 1)

            if id_emp_dvd_jogo is None:

                if qty_dvd_game_rent <= qty_register_dvd_game:
                    sql = "INSERT INTO EMPRESTIMO_DVD_JOGO(QTDE_DIAS_EMPR,VALOR_DIARIA,ID_FUNC,ID_CLIENTE,"\
                          "ID_DVD_JOGO,DATA_CRIACAO, DATA_ATUALIZACAO, ID_USUARIO) " \
                          "VALUES({0},{1},{2},{3},{4},'{5}','{6}',{7});".format(datas[0], datas[1], id_func, id_cliente,
                                                                                id_dvd_jogo, date_hour, date_hour,
                                                                                datas[5])

                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("_"*80)
                    print("Foi adicionado um novo registro com sucesso.")

                else:
                    print("_"*80)
                    print(f"Não foi possível alugar este Dvd ou Jogo ({datas[4]}) \npois a quantidade de Dvds ou Jogos "
                          f"para este aluguel é maior do que a quantidade disponível.")

            else:
                print("_"*80)
                print("Este Dvd ou Jogo já está alugado.")

        except():
            print("_"*80)
            print("Erro ao tentar inserir dados no empréstimo.")
        finally:
            self.close_connection()

    def update_qty_days_emp(self, customer_cpf, name_dvd_game, qty_days_rent, user_id):
        try:
            id_cliente = self.return_id_cliente(customer_cpf)
            id_dvd_jogo = self.return_id_dvd_jogo(name_dvd_game)
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            if id_emp_dvd_jogo is not None:
                sql = ("UPDATE EMPRESTIMO_DVD_JOGO SET QTDE_DIAS_EMPR = {0},DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_EMP_DVD_JOGO = {3};".format(qty_days_rent, date_hour, user_id, id_emp_dvd_jogo))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("A Quantidade de  dias do DVD ou jogo Emprestado foi alterada com sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def update_daily_value(self, customer_cpf, name_dvd_game, daily_value, user_id):
        try:
            id_cliente = self.return_id_cliente(customer_cpf)
            id_dvd_jogo = self.return_id_dvd_jogo(name_dvd_game)
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            if id_emp_dvd_jogo is not None:
                sql = ("UPDATE EMPRESTIMO_DVD_JOGO SET VALOR_DIARIA = {0} ,DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"""
                       " WHERE ID_EMP_DVD_JOGO = {3};".format(daily_value, date_hour, user_id, id_emp_dvd_jogo))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O valor diário foi alterado com sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def update_total_value(self, customer_cpf, name_dvd_game, total_value, user_id):
        try:
            id_cliente = self.return_id_cliente(customer_cpf)
            id_dvd_jogo = self.return_id_dvd_jogo(name_dvd_game)
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            if id_emp_dvd_jogo is not None:
                sql = ("UPDATE EMPRESTIMO_DVD_JOGO SET VALOR_TOTAL = {0},DATA_ATUALIZACAO = '{1}',ID_USUARIO = {2} "
                       "WHERE ID_EMP_DVD_JOGO = {3};".format(total_value, date_hour, user_id, id_emp_dvd_jogo))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O Valor Total foi alterado com sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def update_id_employee(self, customer_cpf, name_dvd_game, employee_cpf, user_id):
        try:
            id_cliente = self.return_id_cliente(customer_cpf)
            id_dvd_jogo = self.return_id_dvd_jogo(name_dvd_game)
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            if id_emp_dvd_jogo is not None:
                id_func = self.return_id_func(employee_cpf)
                sql = ("UPDATE EMPRESTIMO_DVD_JOGO SET ID_FUNC = {0}, DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}  "
                       "WHERE ID_EMP_DVD_JOGO = {3};".format(id_func, date_hour, user_id,
                                                             id_emp_dvd_jogo))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Registro do Funcionário foi alterado com sucesso.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def update_id_customer(self, old_customer_cpf, name_dvd_game, new_customer_cpf, user_id):
        try:
            id_cliente = self.return_id_cliente(old_customer_cpf)
            id_dvd_jogo = self.return_id_dvd_jogo(name_dvd_game)
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            if id_emp_dvd_jogo is not None:

                id_new_cliente = self.return_id_cliente(new_customer_cpf)
                if id_new_cliente is not None:
                    sql = ("UPDATE EMPRESTIMO_DVD_JOGO SET ID_CLIENTE = {0},DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                           " WHERE ID_EMP_DVD_JOGO = {3};".format(id_new_cliente, date_hour, user_id, id_emp_dvd_jogo))

                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("_" * 80)
                    print("O Cliente foi alterado com sucesso.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def update_id_dvd_game(self, customer_cpf, old_name_dvd_game, new_name_dvd_game, user_id):
        try:
            id_cliente = self.return_id_cliente(customer_cpf)
            id_old_dvd_jogo = self.return_id_dvd_jogo(old_name_dvd_game)
            id_emp_dvd_jogo = self.return_id_empr_dvd_jogo(id_cliente, id_old_dvd_jogo)

            if id_emp_dvd_jogo is not None:
                id_new_dvd_jogo = self.return_id_dvd_jogo(new_name_dvd_game)
                qty_register_dvd_game = self.check_qty_dvd_game_avaibles(id_new_dvd_jogo)
                qty_dvd_game_rent = self.check_qty_dvd_game_rent(id_new_dvd_jogo, 0)
                qty_avaible = qty_register_dvd_game - qty_dvd_game_rent

                if id_new_dvd_jogo is not None:

                    if qty_dvd_game_rent <= qty_avaible:
                        sql = ("UPDATE EMPRESTIMO_DVD_JOGO SET ID_DVD_JOGO = {0},DATA_ATUALIZACAO = '{1}', "
                               "ID_USUARIO = {2} WHERE ID_EMP_DVD_JOGO = {3};".format(id_new_dvd_jogo, date_hour,
                                                                                      user_id, id_emp_dvd_jogo))

                        self.cursor.execute(sql)
                        self.connection.commit()
                        print("_"*80)
                        print("O Registro do Jogo ou Dvd do Cliente foi alterado com sucesso.")

                    else:
                        print("_" * 80)
                        print("Não foi possível alugar este Dvd ou Jogo devido a todos está alugados.")

        except():
            print("_"*80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def delete(self, customer_cpf, name_dvd_game):
        try:
            id_cliente = self.return_id_cliente(customer_cpf)
            id_dvd_jogo = self.return_id_dvd_jogo(name_dvd_game)
            id_emprestimo = self.return_id_empr_dvd_jogo(id_cliente, id_dvd_jogo)

            if id_emprestimo is not None:
                sql = "DELETE FROM EMPRESTIMO_DVD_JOGO WHERE ID_EMP_DVD_JOGO = {0};".format(id_emprestimo)
                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print(f"O registro do Aluguel do Cliente foi deletado com sucesso.")

            else:
                print("_"*80)
                print(f"O registro deste Cliente com este \nJogo: {name_dvd_game.title()}"
                      f" não existe cadastrado.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def select_all(self):
        try:
            sql = f"SELECT * FROM DVD_JOGOS_ALUGADO_V;"
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()

            print("\t \t \t  Dvd ou Jogos Alugado")
            print("_" * 80)
            for registers in datas:
                id_emprestimo = registers[0]
                name_dvd_game = registers[1]
                customer_name = registers[2]
                qty_days_rent = registers[3]
                daily_value = registers[4]
                total_value = registers[5]
                qty_rent = registers[6]
                rent_date = registers[7]
                return_date = registers[8]
                update_date = registers[10]
                user_id = registers[11]

                print(f"Código do DVD ou Jogo Alugado: {id_emprestimo}")
                print(f"Nome do Cliente: {customer_name.title()} ")
                print(f"Nome do Dvd ou Jogo: {name_dvd_game.title()}")
                print(f"Quantidade de dias Emprestado: {qty_days_rent}")
                print(f"Valor Diário: {daily_value}")
                print(f"Valor Total: {total_value}")
                print(f"Quantidade de Dvd ou Jogo emprestado: {qty_rent}")
                print(f"Data do Aluguel: {rent_date}")
                print(f"Data de Devolução: {return_date}")
                print(f"Data da Atualização: {update_date} ")
                print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                print("_" * 80)

            if len(registers) > 1:
                print("Quantidade de jogos e dvds alugados no Total: {0} ".format(len(datas)))

            elif len(registers) == 1:
                print("Você tem somente um jogo ou dvd alugado no Total.")

            else:
                print("Não possui nenhum dvd ou jogo alugado no Total.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar a consulta")
        finally:
            self.close_connection()

    def search_rent_dvd_game(self, customer_name, name_dvd_game):
        try:
            sql = "SELECT * FROM DVD_JOGOS_ALUGADO_V WHERE UPPER(NOME_CLIENTE) LIKE '%{0}%' OR" \
                  " ((UPPER(NOME_DVD_JOGO) LIKE '%{1}%')IS NULL AND 1 = 1);"\
                .format(customer_name.upper(), name_dvd_game.upper())
            self.cursor.execute(sql)
            register = self.cursor.fetchall()

            if register is not None:
                print("_"*40)
                print("\t \t \t  Dvd ou Jogos Alugado")
                print("_" * 40)
                for registers in register:
                    id_emprestimo = registers[0]
                    name_dvd_game = registers[1]
                    customer_name = registers[2]
                    qty_days_rent = registers[3]
                    daily_value = registers[4]
                    total_value = registers[5]
                    qty_rent = registers[6]
                    rent_date = registers[7]
                    return_date = registers[8]
                    update_date = registers[10]
                    user_id = registers[11]

                    print(f"Código do DVD ou Jogo Alugado: {id_emprestimo}")
                    print(f"Nome do Cliente: {customer_name.title()} ")
                    print(f"Nome do Dvd ou Jogo: {name_dvd_game.title()}")
                    print(f"Quantidade de dias Emprestado: {qty_days_rent}")
                    print(f"Valor Diário: {daily_value}")
                    print(f"Valor Total: {total_value}")
                    print(f"Quantidade de Dvd ou Jogo emprestado: {qty_rent}")
                    print(f"Data do Empréstimo: {rent_date}")
                    print(f"Data de Devolução: {return_date}")
                    print(f"Data de Atualização: {update_date} ")
                    print(f"Código Do Usuário que Realizou a Última Atualização: {user_id}")
                    print("_" * 40)

        except():
            print("_" * 80)
            print("Erro ao tentar realizar a alteração")
        finally:
            self.close_connection()

    def report_rent_dvd_game(self, start_date, end_date):
        try:
            datas_write = []
            sql = "SELECT  ID_EMP_DVD_JOGO,NOME_FUNCIONARIO,NOME_CLIENTE,NOME_DVD_JOGO,QTDE_DIAS_EMPR,VALOR_DIARIA" \
                  ",VALOR_TOTAL,DATA_EMPRESTIMO,DATA_DEVOLUCAO,DATA_CRIACAO,DATA_ATUALIZACAO " \
                  "FROM HISTORICO_EMPRESTIMO_DVD_JOGO_V" " WHERE 1 = 1 " \
                  "AND DATA_EMPRESTIMO BETWEEN  '{0}'" "AND  '{1}';".format(start_date, end_date)
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()

            if datas is not None:
                print("_" * 80)
                print("\t \t \t Relatório de Empréstimo")
                print("Parâmetros")
                if start_date is not None:
                    print(f"Data Inicial: {start_date}")

                if end_date is not None:
                    print(f"Data Final: {end_date}")

                print("_" * 80)
                for result in datas:
                    datas_write.append("Código do Empréstimo do DVD ou Jogo: {0}\n".format(result[0]))
                    datas_write.append("Nome do Funcionário que realizou o Empréstimo: {0}\n".format(result[1].title()))
                    datas_write.append("Nome do Cliente: {0}\n".format(result[2].title()))
                    datas_write.append("Nome do DVD ou Jogo: {0}\n".format(result[3].title()))
                    datas_write.append("Quantidade de Dias Emprestado: {0}\n".format(result[4]))
                    datas_write.append("Valor da Diária: {0}\n".format(result[5]))
                    datas_write.append("Valor Total: {0}\n".format(result[6]))
                    datas_write.append("Data do Empréstimo: {0}\n".format(result[7]))
                    datas_write.append("Data da Devolução: {0}\n".format(result[8]))
                    datas_write.append("Data da Criação deste  registro: {0}\n".format(result[9]))
                    datas_write.append("Data da última atualização deste registro: {0}\n".format(result[10]))
                    datas_write.append("_"*80+"\n")

                if len(datas) > 1:
                    datas_write.append("Quantidade de Registros Retornados: {0} registros.\n".format(len(datas)))

                else:
                    datas_write.append("Quantidade de Registros Retornados: {0} registro.\n".format(len(datas)))

                for read_datas in datas_write:
                    print(read_datas)

                return datas_write

            else:
                print("_"*80)
                print("Não existe dados para esses parânetros.")
                if start_date is not None:
                    print(f"Data Inicial: {start_date}")

                if end_date is not None:
                    print(f"Data Final: {end_date}")

        except():
            print("_" * 80)
            print("Erro em geral ao tentar executar a procedure do relatório.")

        finally:
            self.close_connection()


"""datas_lista = []
datas_lista.append(8)
datas_lista.append(3.00)
datas_lista.append("12345567890")
datas_lista.append("09876543212")
datas_lista.append("MARIO KART DE NINTENDO SWITCH")
datas_lista.append(3)"""

# rent = RentDvdGame()
# rent.return_id_cliente(datas_lista[3])
# print(rent.return_id_dvd_jogo(datas_lista[5]))
# rent.return_id_empr_dvd_jogo(2, 2)
# rent.return_id_funcionario("datas_lista[4]")
# rent.select_all()
# rent.search_rent_dvd_game("Carlos Henrique De Souza", "FIFA 2019")
# rent.insert(datas_lista)
# rent.check_qty_dvd_game_avaibles(21)
# rent.check_qty_dvd_game_rent(2)
# rent.update_qty_days_emp(datas_lista[4], datas_lista[5], datas_lista[0])
# rent.update_id_dvd_game(datas_lista[4], "MARIO KART DE NINTENDO SWITCH", "Fórmula 1 2017")
# rent.delete(datas_lista[4], datas_lista[5])
# rent.report_rent_dvd_game('10/09/2019', '23/09/2019')

