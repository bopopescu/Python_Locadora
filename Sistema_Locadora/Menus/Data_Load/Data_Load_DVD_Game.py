import csv
import sys
import os
from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow
from Sistema_Locadora.Operations_CRUD.Actions_DVD_Game import DvdGame
from Sistema_Locadora.Menus.Validates_Menu import Validate


class DataLoad:

    global insert_dvd_game
    insert_dvd_game = DvdGame()

    @staticmethod
    def data_load_csv(user_id):
        try:
            datas = []
            cont_linhas = 0
            date_now = DateHourNow()
            date_hour_now = date_now.get_date_hour_now()
            validate_date = Validate()

            list_files = os.listdir('C:\\Users\\joaovpinto\\PycharmProject\\Sistema_Locadora\\Sistema_Locadora'
                                    '\\Operations_Files\\Directory_Uploads\\CSV')
            name_file = input("Nome do Arquivo sem a extensão: ")
            while name_file is "":
                print("_"*80)
                print("Por favor digite o nome do arquivo.")
                name_file = input("Nome do Arquivo sem a extensão: ")

            if name_file.count(".csv") == 0:
                name_file = name_file + ".csv"

            if name_file in list_files:
                with open("C:\\Users\\joaovpinto\\PycharmProject\\Sistema_Locadora\\Sistema_Locadora\\Operations_Files"
                          "\\Directory_Uploads\\CSV\\" + name_file, "r") as ficheiro:
                    reader = csv.reader(ficheiro)
                    next(reader)
                    print("_"*80)
                    print("\t \t \t Programa de Carga de DVD's e Jogos.")
                    print("Nome do Arquivo: ", name_file)
                    print("Diretório do Arquivo: CSV")
                    print("Data e Horário de Execução do Programa: ", date_hour_now)

                    for line in reader:
                        text = str(line).replace("'", "").replace("[", "").replace("']", "").replace("[ ", "")

                        name_dvd_game = text[:text.find(";")]
                        text = text[text.find(";")+1:]

                        genare = text[:text.find(";")]
                        text = text[text.find(";") + 1:]

                        classification_age = text[:text.find(";")]
                        text = text[text.find(";") + 1:]

                        type_media = text[:text.find(";")]
                        text = text[text.find(";") + 1:]

                        price = text[:text.find(";")]
                        text = text[text.find(";") + 1:]

                        qty = text[:text.find(";")]
                        text = text[text.find(";") + 1:]

                        datas.insert(0, name_dvd_game)
                        datas.insert(1, genare)
                        datas.insert(2, classification_age)
                        datas.insert(3, type_media)
                        datas.insert(4, price)
                        datas.insert(5, qty)
                        datas.insert(6, int(user_id))

                        print("_"*80)
                        print("Nome do Dvd ou Jogo: ", name_dvd_game)
                        print("Genêro: ", genare)
                        print("Classificação de Idade: ", classification_age)
                        print("Tipo: ", type_media)
                        print("Preço: ", price)
                        print("Quantidade: ", qty)

                        insert_dvd_game.insert_multiple(datas)
                        cont_linhas += 1

                    print("_"*80)
                    print("Quantidade de registros cadastrados com sucesso: ", cont_linhas)
                    insert_dvd_game.close_connection()
                    ficheiro.close()

            else:
                print("_"*80)
                print(f"O Arquivo {name_file} não existe salvo dentro do diretório CSV.")
                print("Por favor verifique o diretório!")
                insert_dvd_game.close_connection()

        except csv.Error as e:
            print("_"*80)
            sys.exit("Ficheiro: {0}\n Linha:{1}\n Erro: e" .format(ficheiro, reader.line_num, e))
            ficheiro.close()
            insert_dvd_game.close_connection()

        except():
            print("_"*80)
            print("Erro ao tentar ler o arquivo: ")
            ficheiro.close()
            insert_dvd_game.close_connection()


"""read_csv = DataLoad()
read_csv.data_load_csv()"""
