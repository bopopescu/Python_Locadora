from Sistema_Locadora.Connection_DataBase.Connection import Connection
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow


class DvdGame(Connection):

    global date_hour
    now = DateHourNow()
    date_hour = now.get_date_hour_now()

    def check_qtde_dvd_games_avaible(self, id_dvd_jogo):
        try:
            select_qty_dvd_games = "SELECT QTDE FROM DVD_JOGO WHERE ID_DVD_JOGO = {0};".format(id_dvd_jogo)
            self.cursor.execute(select_qty_dvd_games)
            qty_dvds_games = self.cursor.fetchone()

            if qty_dvds_games is not None:
                return qty_dvds_games[0]

            else:
                return int(0)

        except():
            print("_"*80)
            print("Erro ao tentar recuperar a quantidade de Dvds ou Jogos cadastrados da tabela DVD_JOGOS.")

    def return_id(self, nome_dvd_jogo):
        try:
            select_id_dvd_game = "SELECT ID_DVD_JOGO FROM DVD_JOGO WHERE UPPER(NOME) = '{0}';"\
                                .format(nome_dvd_jogo.upper())

            self.cursor.execute(select_id_dvd_game)
            id_dvd_game = self.cursor.fetchone()

            if id_dvd_game is not None:
                return id_dvd_game[0]

            else:
                return None

        except():
            self.close_connection()
            print("_"*80)
            print("Erro ao tentar recuperar o registro do id_dvd_game.")

    def insert(self, datas=[]):
        try:
            id_dvd_game = self.return_id(datas[0])

            if id_dvd_game is None:
                sql = ("INSERT INTO DVD_JOGO(NOME,GENERO,CLASSIFICACAO_IDADE,TIPO,PRECO,DATA_FABRICACAO,QTDE"
                       ",DATA_CRIACAO,DATA_ATUALIZACAO, ID_USUARIO)" 
                       f"VALUES('{datas[0]}','{datas[1]}',{datas[2]},'{datas[3]}',{datas[4]},"
                       f"'{datas[5]}',{datas[6]},'{date_hour}','{date_hour}',{datas[7]});")

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O Registro do (Dvd ou Jogo) foi cadastrado com sucesso.\nNome: {0}".format(datas[0].title()))
            else:
                print("_"*80)
                print("Este DVD ou jogo cujo o nome é: {0} já se encontra cadastrado.".format(datas[0].title()))

        except():
            print("_" * 80)
            print("Erro ao tentar inserir um novo Dvd ou jogo. ")

        finally:
            self.close_connection()

    def insert_multiple(self, datas=[]):
        try:
            id_dvd_game = self.return_id(datas[0])

            if id_dvd_game is None:
                self.cursor.callproc("INSERT_CARGA_CSV_P", [datas[0], datas[1], datas[2], datas[3], datas[4], datas[5],
                                                            datas[6]])
                print("_"*80)
                print("O Registro do (Dvd ou Jogo) foi cadastrado com sucesso.\nNome: {0}".format(datas[0].title()))
            else:
                print("_"*80)
                print("Este DVD ou jogo cujo o nome é: {0} já se encontra cadastrado.".format(datas[0].title()))

        except():
            print("_" * 80)
            print("Erro ao tentar inserir um novo Dvd ou jogo. ")
            self.close_connection()

    def update_name(self, name_old, new_name, user_id):
        try:
            id_dvd_game = self.return_id(name_old)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET NOME = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(new_name, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O Nome do Dvd ou Jogo foi alterado com sucesso.")

            else:
                print("_"*80)
                print("Não existe este DVD ou Jogo cadastrado no sistema.")

        except():
            print("_"*80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def update_genare(self, name_dvd_game, genare, user_id):
        try:
            id_dvd_game = self.return_id(name_dvd_game)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET GENERO = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(genare, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O Gênero do DVD ou Jogo foi alterado com sucesso.")

            else:
                print("_"*80)
                print("Não existe registro do DVD ou Jogo cadastrado no sistema.")

        except():
            print("_"*80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def update_classification_age(self, name_dvd_game, classification_age, user_id):
        try:
            id_dvd_game = self.return_id(name_dvd_game)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET CLASSIFICACAO_IDADE = {0},DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(classification_age, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A Classificação de Idade foi alterada com sucesso.")

            else:
                print("_" * 80)
                print("Não existe registro do DVD ou Jogo cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def update_type_dvd_game(self, name_dvd_game, type_dvd_game, user_id):
        try:
            id_dvd_game = self.return_id(name_dvd_game)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET TIPO = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(type_dvd_game, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Tipo do DVD ou Jogo foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe registro do DVD ou Jogo cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def update_price(self, name_dvd_game, price, user_id):
        try:
            id_dvd_game = self.return_id(name_dvd_game)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET PRECO = {0},DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(price, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("O Preço do DVD ou Jogo foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe registro do DVD ou Jogo cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def update_fabrication_date(self, name_dvd_game, fabrication_date, user_id):
        try:
            id_dvd_game = self.return_id(name_dvd_game)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET DATA_FABRICACAO = '{0}',DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(fabrication_date, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A Data de Fabricação do DVD ou Jogo foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe registro do DVD ou Jogo cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def update_quantity(self, name_dvd_game, quantity, user_id):
        try:
            id_dvd_game = self.return_id(name_dvd_game)
            if id_dvd_game is not None:
                sql = ("UPDATE DVD_JOGO SET QTDE = {0},DATA_ATUALIZACAO = '{1}', ID_USUARIO = {2}"
                       " WHERE ID_DVD_JOGO = {3};".format(quantity, date_hour, user_id, id_dvd_game))

                self.cursor.execute(sql)
                self.connection.commit()
                print("_" * 80)
                print("A Quantidade de DVD ou Jogo foi alterado com sucesso.")

            else:
                print("_" * 80)
                print("Não existe registro do DVD ou Jogo cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar realizar o update do Dvd Ou Jogo.")
        finally:
            self.close_connection()

    def delete(self, nome_dvd_jogo):
        try:
            id_dvd_game = self.return_id(nome_dvd_jogo)

            if id_dvd_game is not None:
                sql = ("DELETE FROM DVD_JOGO WHERE ID_DVD_JOGO = {0};".format(id_dvd_game))
                self.cursor.execute(sql)
                self.connection.commit()
                print("_"*80)
                print("O registro do Dvd Ou Jogo:{0} foi deletado com sucesso.".format(nome_dvd_jogo.title()))

            else:
                print("_"*80)
                print("Não existe registro pra este Dvd Ou Jogo.")

        except():
            print("_"*80)
            print("Erro ao tentar deletar este registro:{0}".format(nome_dvd_jogo))
        finally:
            self.close_connection()

    def select_all(self):
        try:
            sql = "SELECT * FROM DVD_JOGOS_V ORDER BY NOME;"
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()

            print("\t \t \t Dvd's e Jogos")
            print("_"*80)
            for registers in datas:
                id_dvd_jogo = registers[0]
                name = registers[1]
                genare = registers[2]
                classification_age = registers[3]
                type_reg = registers[4]
                price = registers[5]
                date_fab = registers[6]
                date_insert = registers[7]
                quantity = registers[8]
                update_date = registers[10]
                user_id = registers[11]

                print("Código do (Dvd ou Jogo): {0}".format(id_dvd_jogo))
                print("Nome: {0} ".format(name.title()))
                print("Gênero: {0} ".format(genare.title()))
                print("Classificação de Idade: {0} ".format(classification_age))
                print("Tipo: {0} ".format(type_reg.title()))
                print("Preço: {0} ".format(price))
                print("Data de Fabricação: {0} ".format(date_fab))
                print("Data de Cadastro: {0} ".format(date_insert))
                print("Quantidade: {0} ".format(quantity))
                print("Data de Atualização: {0}".format(update_date))
                print("Código Do Usuário que Realizou a Última Atualização: {0}".format(user_id))
                print("_"*80)

            if len(datas) > 1:
                print("Quantidade de registros: {0} ".format(len(datas)))

            elif len(datas) == 1:
                print("Você possuí somente: {0} registro cadastrado. ".format(len(datas)))

            else:
                print("Não existe nenhum dvd ou jogo cadastrado.")

        except():
            print("_"*80)
            print("Erro ao tentar retornar todos os registros.")
        finally:
            self.close_connection()

    def search_dvd_game(self, name_dvd_game):
        try:
            sql = f"SELECT * FROM DVD_JOGOS_V WHERE UPPER(NOME) LIKE '%{name_dvd_game.upper()}%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()

            print("\t \t \t Dvd e Jogos")
            print("_"*80)
            if records is not None:
                for datas in records:
                    print("_"*80)
                    id_dvd_jogo = datas[0]
                    name = datas[1]
                    genare = datas[2]
                    classification_age = datas[3]
                    type_reg = datas[4]
                    price = datas[5]
                    date_fab = datas[6]
                    date_insert = datas[7]
                    quantity = datas[8]
                    update_date = datas[10]
                    user_id = datas[11]

                    print("Código do (Dvd ou Jogo): {0}".format(id_dvd_jogo))
                    print("Nome: {0} ".format(name.title()))
                    print("Gênero: {0} ".format(genare.title()))
                    print("Classificação de Idade: {0} ".format(classification_age))
                    print("Tipo: {0} ".format(type_reg.title()))
                    print("Preço: {0} ".format(price))
                    print("Data de Fabricação: {0} ".format(date_fab))
                    print("Data de Cadastro: {0} ".format(date_insert))
                    print("Quantidade: {0} ".format(quantity))
                    print("Data de Atualização: {0}".format(update_date))
                    print("Código Do Usuário que Realizou a Última Atualização: {0}".format(user_id))

            else:
                print("Não existe este Dvd ou Jogo cadastrado no sistema.")

        except():
            print("_" * 80)
            print("Erro ao tentar retornar todos os registros.")
        finally:
            self.close_connection()


"""
data=[]
data.append('Fifa 2018')
data.append('Esporte')
data.append(10)
data.append('Esporte')
data.append(250.00)
data.append('2017.06.02')
data.append(2)
"""
# dvd_game = DvdGame()
# dvd_game.return_id("Fifa 2018")
# dvd_game.insert(data)
# dvd_game.select_all()
# dvd_game.search_dvd_game('Fifa 2018')
# dvd_game.update(data)
# dvd_game.delete("Fifa 2018")
