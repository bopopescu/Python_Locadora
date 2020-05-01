from Sistema_Locadora.Connection_DataBase.Connection import Connection
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow
from Sistema_Locadora.Operations_CRUD.Actions_Employee import Employee


class Login(Connection):

    global date_hour
    now = DateHourNow()
    date_hour = now.get_date_hour_now()

    def exist_login(self, cpf, password):
        try:
            id_func = self.return_id_func(cpf)
            if id_func is not None:
                sql = "SELECT NOME_FUNCIONARIO FROM LOGINS_V WHERE ID_FUNC = {0} AND SENHA = '{1}';"\
                    .format(id_func, password)

                self.cursor.execute(sql)
                employee_name = self.cursor.fetchone()

                if employee_name is not None:
                    logar = "Logado com Sucesso"
                    print("_"*80)
                    print(logar)
                    print(f"Bem - Vindo(a) {str(employee_name[0]).title()}.")
                    return logar

                else:
                    print("_"*80)
                    print("Login incorreto.")
                    return None

            else:
                print("_"*80)
                print("Não existe este login cadastrado no sistema.")
                return None

        except():
            print("_" * 80)
            print("Erro ao tentar Logar.")

    def return_id_login(self, id_func):
        try:
            sql = "SELECT ID_LOGIN FROM LOGIN WHERE ID_FUNC = {0};".format(id_func)
            self.cursor.execute(sql)
            id_login = self.cursor.fetchone()

            if id_login is not None:
                return id_login[0]

            else:
                return None
        except():
            print("_"*80)
            print("Erro ao tentar recuperar o Id do Login")
            self.close_connection()

    @staticmethod
    def return_id_func(cpf):
        employee = Employee()
        id_func = employee.return_id(cpf)
        return id_func

    @staticmethod
    def return_job_rule(cpf):
        employee = Employee()
        job_rule = employee.return_job_rule(cpf)
        return job_rule

    def insert(self, cpf, password, question, answer):
        try:
            id_func = self.return_id_func(cpf)
            id_login = self.return_id_login(id_func)

            if id_login is None:
                sql = "INSERT INTO LOGIN (ID_FUNC,SENHA,PERGUNTA,RESPOSTA,DATA_CRIACAO,DATA_ATUALIZACAO)" \
                      "VALUES({0},'{1}','{2}','{3}','{4}','{5}');".format(id_func, password, question,
                                                                          answer, date_hour, date_hour)

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("Foi cadastrado com sucesso o novo login.")

            else:
                print("_"*80)
                print("Já existe este login cadastrado.")

        except():
            print("_"*80)
            print("Erro ao tentar cadastrar o novo login.")
        finally:
            self.close_connection()

    def update_password(self, cpf, password):
        try:
            id_func = self.return_id_func(cpf)
            id_login = self.return_id_login(id_func)

            if id_login is not None:
                sql = "UPDATE LOGIN SET SENHA = '{0}' " \
                      "WHERE ID_LOGIN = {1};".format(password, id_login)

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A sua senha foi alterada com sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar alterar a senha.")
        finally:
            self.close_connection()

    def update_question(self, cpf, question):
        try:
            id_func = self.return_id_func(cpf)
            id_login = self.return_id_login(id_func)

            if id_login is not None:
                sql = "UPDATE LOGIN SET PERGUNTA = '{0}' " \
                      "WHERE ID_LOGIN = {1};".format(question.title(), id_login)
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A sua pergunta foi alterada com sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar alterar a pergunta.")
        finally:
            self.close_connection()

    def update_answer(self, cpf, answer):
        try:
            id_func = self.return_id_func(cpf)
            id_login = self.return_id_login(id_func)

            if id_login is not None:
                sql = "UPDATE LOGIN SET RESPOSTA = '{0}' " \
                      "WHERE ID_LOGIN = {1};".format(answer, id_login)
                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A sua resposta foi alterada com sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar alterar a resposta da pergunta.")
        finally:
            self.close_connection()

    def delete(self, cpf):
        try:
            id_func = self.return_id_func(cpf)

            if id_func is not None:
                sql = "DELETE FROM LOGIN WHERE ID_FUNC = {0};".format(id_func)
                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O login do funcionário foi deletado com sucesso.")

            else:
                print("_"*80)
                print("Não existe este login cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar deletar este Login.")
        finally:
            self.close_connection()

    def logar(self, cpf, password):
        try:
            id_func = self.return_id_func(cpf)
            if id_func is not None:
                sql = "SELECT NOME_FUNCIONARIO FROM LOGINS_V WHERE ID_FUNC = {0} AND SENHA = '{1}';"\
                    .format(id_func, password)

                self.cursor.execute(sql)
                employee_name = self.cursor.fetchone()

                if employee_name is not None:
                    logar = "Logado com Sucesso"
                    print("_"*80)
                    print(logar)
                    print(f"Bem - Vindo(a) {str(employee_name[0]).title()}.")
                    return logar

                else:
                    print("_"*80)
                    print("Login incorreto.")
                    return None

            else:
                print("_"*80)
                print("Não existe este login cadastrado no sistema.")
                return None

        except():
            print("_" * 80)
            print("Erro ao tentar Logar.")
        finally:
            self.close_connection()

    def recover_password(self, cpf):
        try:
            id_func = self.return_id_func(cpf)
            sql = "SELECT PERGUNTA FROM LOGIN WHERE ID_FUNC = {0};".format(id_func)
            self.cursor.execute(sql)
            question = self.cursor.fetchone()

            if question is not None:
                print(str(question[0]).title())
                answer = input("Digite a resposta da Pergunta acima: ")
                while answer is "":
                    print("_"*80)
                    print("Por favor digite a reposta da pergunta.")
                    answer = input("Digite a resposta da Pergunta acima: ")

                sql = "SELECT SENHA FROM LOGIN WHERE ID_FUNC = {0} AND RESPOSTA = '{1}';".format(id_func, answer)
                self.cursor.execute(sql)
                password = self.cursor.fetchone()
                print("_"*80)
                if password is not None:
                    print("A sua senha é: {0}".format(str(password[0])))
                    print("_"*80)

                else:
                    print("Resposta incorreta.")

            else:
                print("_"*80)
                print("Não existe esses dados cadastrados no sistema.")
        except():
            print("_" * 80)
            print("Erro ao tentar recuperar a senha do Login.")
        finally:
            self.close_connection()


"""
datas_login = []
datas_login.append("12345567890")
datas_login.append("098765")
datas_login.append("which is the this mounth ? ")
datas_login.append("August")
"""
# login = Login()
# login.return_id_func(datas_login[0])
# login.return_id_login(1)
# login.insert(datas_login[0], datas_login[1], datas_login[2], datas_login[3])
# login.logar(datas_login[0], datas_login[1])
# login.recover_password(datas_login[0])
# login.update_question('12345567891', '2')
# login.update_answer('12345567891', '2')
# login.update_password('12345567891', '123')
# login.delete(datas_login[0])

