from Sistema_Locadora.Operations_CRUD.Date_Hour_Now import DateHourNow
from Sistema_Locadora.Operations_CRUD.Actions_Rent_DVD_Game import RentDvdGame


class Report:

    global data_hour_now
    data_hour = DateHourNow()
    data_hour_now = data_hour.get_date_hour_now()

    @staticmethod
    def report_txt(start_date, end_date):
        try:
            convert_data_hour_now = str(data_hour_now)
            convert_data_hour_now = convert_data_hour_now[0:10]

            file_genarate = "C:\\Users\\joaovpinto\\PycharmProject\\Sistema_Locadora\\Sistema_Locadora" \
                            "\\Operations_Files\\Directory_Of_Reports\\report_txt_{0}.txt".format(convert_data_hour_now)

            file = open(file_genarate, "w")
            rent_dvd_game = RentDvdGame()
            datas = rent_dvd_game.report_rent_dvd_game(start_date, end_date)
            file.write("\t \t \t Relatório de Empréstimo\n")
            file.write("Parâmetros\n")
            if start_date is not None:
                file.write(f"Data Inicial: {start_date}\n")

            if end_date is not None:
                file.write(f"Data Final: {end_date}\n")
            file.write("_" * 80+"\n")

            for save_datas in datas:
                file.write(save_datas)

            print("O Relatório foi salvo com sucesso.")
            print("Nome do Arquivo: {0}".format("report_txt_" + convert_data_hour_now))
            print("Diretório do Arquivo: {0}".format("Directory_Of_Reports"))
            print("Data e Horário do Processamento: {0} ".format(data_hour_now))
            print("_" * 80)

            if file.closed:
                file.close()

        except():
            print("_"*80)
            print("Erro ao tentar gerar o arquivo.")


"""test_write = Report()
test_write.report_txt('10/09/2019', '23/09/2019')"""
