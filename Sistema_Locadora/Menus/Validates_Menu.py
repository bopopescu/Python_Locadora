from Sistema_Locadora.Operations_CRUD.Actions_Rent_DVD_Game import RentDvdGame
from Sistema_Locadora.Operations_CRUD.Actions_Customer import Customer
from Sistema_Locadora.Operations_CRUD.Actions_Employee import Employee


class Validate:

    global rent_dvd_game
    rent_dvd_game = RentDvdGame()

    @staticmethod
    def validate_number_cpf_employee(cpf):
        cpf_number_validate = Customer()
        cpf_validate = cpf_number_validate.validate_number_cpf(cpf)
        return cpf_validate

    @staticmethod
    def validate_number_cpf_customer(cpf):
        cpf_number_validate = Employee()
        cpf_validate = cpf_number_validate.validate_number_cpf(cpf)
        return cpf_validate

    @staticmethod
    def validate_customer_cpf():
        customer_cpf = input("Digite o CPF Do Cliente: ")
        customer_cpf = customer_cpf.replace(".", "")
        customer_cpf = customer_cpf.replace("-", "")
        customer_cpf = customer_cpf.replace("/", "")
        validate_cpf_customer = rent_dvd_game.return_id_cliente(customer_cpf)

        while customer_cpf.isdigit() is False or len(customer_cpf) != 11 or validate_cpf_customer is None:
            print("_" * 80)
            print("O CPF do Cliente está incorreto ou não existe cadastrado no sistema.")
            customer_cpf = input("Digite o CPF Do Cliente: ")
            customer_cpf = customer_cpf.replace(".", "")
            customer_cpf = customer_cpf.replace("-", "")
            validate_cpf_customer = rent_dvd_game.return_id_cliente(customer_cpf)

        return customer_cpf

    @staticmethod
    def validate_employee_cpf():
        cpf_employee = input("Digite o CPF do funcionário: ")
        cpf_employee = cpf_employee.replace(".", "")
        cpf_employee = cpf_employee.replace("\\", "")
        cpf_employee = cpf_employee.replace("-", "")
        cpf_employee_exists = rent_dvd_game.return_id_func(cpf_employee)

        while len(cpf_employee) != 11 or cpf_employee.isdigit() is False or cpf_employee_exists is None:
            print("_" * 80)
            print(" O CPF do funcionário está incorreto ou não existe cadastrado.")
            cpf_employee = input("Digite o CPF do funcionário: ")
            cpf_employee = cpf_employee.replace(".", "")
            cpf_employee = cpf_employee.replace(".", "")
            cpf_employee_exists = rent_dvd_game.return_id_func(cpf_employee)

        return cpf_employee

    @staticmethod
    def validate_name_dvd_game():
        name_dvd_game = input("Digite o Nome do DVD ou Jogo: ")
        name_dvd_game_exists = rent_dvd_game.return_id_dvd_jogo(name_dvd_game)

        while name_dvd_game is None or name_dvd_game_exists is None:
            print("_" * 80)
            print("Por favor digite corretamente o nome do DVD ou Jogo.")
            name_dvd_game = input("Digite o Nome do DVD ou Jogo: ")
            name_dvd_game_exists = rent_dvd_game.return_id_dvd_jogo(name_dvd_game)

        return name_dvd_game

    @staticmethod
    def validation_date_insert(date):
        date_fabrication = date.replace(".", "")
        date_fabrication = date_fabrication.replace("-", "")
        date_fabrication = date_fabrication.replace("/", "")
        if date_fabrication.isdigit() and len(date_fabrication) == 8:
            year = date_fabrication[len(date_fabrication) - 4:]
            mounth = date_fabrication[2:4]
            day = date_fabrication[0:2]
            date_fabrication_format = year + "-" + mounth + "-" + day
            return date_fabrication_format

        else:
            return None

    @staticmethod
    def validation_date_select(date):
        date = date.replace("/", "")
        date = date.replace("-", "")
        date = date.replace(".", "")

        if date.isdigit() and len(date) == 8:
            year = date[len(date) - 4:]
            mounth = date[2:4]
            day = date[0:2]
            date_format = day + "/" + mounth + "/" + year
            return date_format

        else:
            return None

    @staticmethod
    def validate_text_while():
        print("_" * 80)
        print("Opção inválida.")
        print("Por favor digite uma opção válida.")
        print("_" * 80)

    @staticmethod
    def validate_schedule(schedule):
        schedule = schedule.replace(".", "")
        schedule = schedule.replace(":", "")
        schedule = schedule.replace("\\", "")
        schedule = schedule.replace("/", "")

        if schedule is not "":
            if schedule.isdigit() and len(schedule) == 6:
                hour = schedule[:2]
                minutes = schedule[4: 6]
                seconds = schedule[len(schedule) - 2:]
                schedule_format = hour + ":" + minutes + ":" + seconds
                return schedule_format

        else:
            return None
