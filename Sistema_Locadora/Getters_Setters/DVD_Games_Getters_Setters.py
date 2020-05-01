

class DvdGamesGetSet:

    def __init__(self, name_game, genare, classific_age, type_dvd_game, price, date_fabrication, quantity, user_id):
        self.__name_game = name_game.title()
        self.__genare = genare.title()
        self.__classific_age = classific_age
        self.__type_dvd_game = type_dvd_game.title()
        self.__price = price
        self.__date_fabrication = date_fabrication
        self.__quantity = quantity
        self.__user_id = user_id

    @property
    def name_game(self):
        return self.__name_game

    @name_game.setter
    def name_game(self, name_game):
        self.__name_game = name_game.title()

    @property
    def genare(self):
        return self.__genare

    @genare.setter
    def genare(self, genare):
        self.__genare = genare.title()

    @genare.deleter
    def genare(self):
        self.__genare = None

    @property
    def classific_age(self):
        return self.__classific_age

    @classific_age.setter
    def classific_age(self, classific_age):
        self.__classific_age = classific_age.title()

    @property
    def type_dvd_game(self):
        return self.__type_dvd_game

    @type_dvd_game.setter
    def type_dvd_game(self, type_dvd_game):
        self.__type_dvd_game = type_dvd_game.title()

    @type_dvd_game.deleter
    def type_dvd_game(self):
        self.__type_dvd_game = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def date_fabrication(self):
        return self.__date_fabrication

    @date_fabrication.setter
    def date_fabrication(self, date_fabrication):
        self.__date_fabrication = date_fabrication

    @date_fabrication.deleter
    def date_fabrication(self):
        self.__date_fabrication = None

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

"""
dvd_game = DvdGamesGetSet('Fifa 2017', 'Esporte', 10, 'Esporte', 120.00, '02/09/2017', 2)
print(dvd_game.name_game)
print(dvd_game.type_game)
print(dvd_game.classific_age)
print(dvd_game.genare)
print(dvd_game.price)
print(dvd_game.date_fabrication)
print(dvd_game.quantity)
"""

