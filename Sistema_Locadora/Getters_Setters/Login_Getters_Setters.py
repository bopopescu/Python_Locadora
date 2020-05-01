

class LoginGetSet:

    def __init__(self, cpf, password, question,answer):

        if cpf.isdigit() and len(cpf) == 11:
            self.__cpf = cpf

        else:
            print("_"*80)
            print("Por favor digite o CPF corretamente.")

        self.__password = password
        self.__question = question
        self.__answer = answer

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf.isdigit() and len(cpf) == 11:
            self.__cpf = cpf
        else:
            print("_"*80)
            print("Por favor digite o CPF corretamente.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question):
        self.__question = question

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        self.__answer = answer
