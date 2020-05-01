import mysql.connector


class Connection:

    def __init__(self):
        try:
            connection = mysql.connector.connect(user="root",
                                                 password="",
                                                 host="localhost",
                                                 database="BD_LOCADORA")
            cursor = connection.cursor()
            self.connection = connection
            self.cursor = cursor
        except():
            print("Erro ao tentar realizar a conexão em geral.")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            # print("Conexão fechada")
