

class CustomersGetSet:

    def __init__(self, name, age, street, number, complement, cep, telephone, cellphone, rg, cpf, user_id):
        self.__name = name.title()
        self.__age = age

        if street is not None:
            self.__street = street.title()

        else:
            self.__street = street

        self.__number = number

        if complement is not None:
            self.__complement = complement.title()

        else:
            self.__complement = complement

        if cep.isdigit() and len(cep) == 8:
            self.__cep = cep

        self.__telephone = telephone

        if cellphone.isdigit():
            self.__cellphone = cellphone

        if rg.isdigit() and len(rg) == 9:
            self.__rg = rg

        if cpf.isdigit() and len(cpf) == 11:
            self.__cpf = cpf

        self.__user_id = user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street.title()

    @street.deleter
    def street(self):
        self.__street = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number.isdigit():
            self.__number = number

    @number.deleter
    def number(self):
        self.__number = None

    @property
    def complement(self):
        return self.__complement

    @complement.setter
    def complement(self, complement):
        self.__complement = complement.title()

    @complement.deleter
    def complement(self):
        self.__complement = None

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        if cep.isdigit() and len(cep) == 8:
            self.__cep = cep
        else:
            print("Por favor digite apenas números.")

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if telephone.isdigit():
            self.__telephone = telephone

    @telephone.deleter
    def telephone(self):
        self.__telephone = None

    @property
    def cellphone(self):
        return self.__cellphone

    @cellphone.setter
    def cellphone(self, cellphone):
        if cellphone.isdigit():
            self.__cellphone = cellphone

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        if rg.isdigit() and len(rg) == 9:
            self.__rg = rg

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf.isdigit() and len(cpf) == 11:
            self.__cpf = cpf

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

"""
client = CustomersGetSet('Breno de Sales', 35, 'MARIA DE MENDES', 133, None, '04877121', None, '987880985', '098765494'
                         , '19876543212')
client.name = "John"
print(client.name)
print(client.age)
print(client.street)
print(client.number)
print(client.complement)
print(client.cep)
print(client.telephone)
print(client.cellphone)
print(client.rg)
print(client.cpf)
del client.street
print(client.street)
"""




