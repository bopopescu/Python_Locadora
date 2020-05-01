

class RentDvdGameGetSet:

    def __init__(self, quantity_days_rent, daily_value, cpf_employee, cpf_customer, name_dvd_game, user_id):
        self.__quantity_days_rent = quantity_days_rent
        self.__daily_value = daily_value
        self.__cpf_employee = cpf_employee
        self.__cpf_customer = cpf_customer
        self.__name_dvd_game = name_dvd_game.upper()
        self.__user_id = user_id

    @property
    def quantity_days_rent(self):
        return self.__quantity_days_rent

    @quantity_days_rent.setter
    def quantity_days_rent(self, quantity_days_rent):
        self.__quantity_days_rent = quantity_days_rent

    @property
    def daily_value(self):
        return self.__daily_value

    @daily_value.setter
    def daily_value(self, daily_value):
        self.__daily_value = daily_value

    @property
    def cpf_employee(self):
        return self.__cpf_employee

    @cpf_employee.setter
    def cpf_employee(self, cpf_employee):
        self.__cpf_employee = cpf_employee

    @property
    def cpf_customer(self):
        return self.__cpf_customer

    @cpf_customer.setter
    def cpf_customer(self, cpf_customer):
        self.__cpf_customer = cpf_customer

    @property
    def name_dvd_game(self):
        return self.__name_dvd_game

    @name_dvd_game.setter
    def name_dvd_game(self, name_dvd_game):
        self.__name_dvd_game = name_dvd_game.upper()

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id


"""
rent = RentDvdGameGetSet(7, 2.00, 14.00, "Miguel Da Silva Alvez", "LETICIA VIERA DA SILVA",
                         "MARIO KART DE NINTENDO SWITCH")
print(rent.quantity_rent)
print(rent.daily_value)
print(rent.total_value)
print(rent.employee_name)
print(rent.customer_name)
print(rent.name_dvd_game)
"""
