

class EmployeeGetSet:

    def __init__(self, name, birthday, age, sex, rg, cpf, telephone, cellphone, street, number, complement, cep,
                 quantity_days, entry_hour, departure_hour, salary, job_role, vt, user_id):

        self.__name = name.title()
        self.__birthday = birthday
        self.__age = age
        self.__sex = sex.upper()
        if rg.isdigit():
            self.__rg = rg
        if cpf.isdigit():
            self.__cpf = cpf
        self.__telephone = telephone
        self.__cellphone = cellphone
        self.__street = street.title()
        if number.isdigit():
            self.__number = number
        self.__complement = complement
        if cep.isdigit():
            self.__cep = cep
        self.__quantity_days = quantity_days
        self.__entry_hour = entry_hour
        self.__departure_hour = departure_hour
        self.__salary = salary
        self.__job_role = job_role.title()
        if vt in("Y", "N", "DEFAULT"):
            self.__vt = vt
        self.__user_id = user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        self.__age = None

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex.upper()

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
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if telephone.isdigit() and telephone.find("9") >= 1:
            self.__telephone = telephone

    @telephone.deleter
    def telephone(self):
        self.__telephone = None

    @property
    def cellphone(self):
        return self.__cellphone

    @cellphone.setter
    def cellphone(self, cellphone):
        if cellphone.isdigit() and cellphone.find("9") >= 1:
            self.__cellphone = cellphone

    @cellphone.deleter
    def cellphone(self):
        self.__cellphone = None

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number.isdigit():
            self.__number = number

    @property
    def complement(self):
        return self.__complement

    @complement.setter
    def complement(self, complement):
        self.__complement = complement.title()

    @complement.deleter
    def comlement(self):
        self.__complement = None

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        if cep.isdigit() and len(cep) == 8:
            self.__cep = cep

    @property
    def quantity_days(self):
        return self.__quantity_days

    @quantity_days.setter
    def quantity_days(self, quantity_days):
        self.__quantity_days = quantity_days

    @property
    def entry_hour(self):
        return self.__entry_hour

    @entry_hour.setter
    def entry_hour(self, entry_hour):
        self.__entry_hour = entry_hour

    @property
    def departure_hour(self):
        return self.__departure_hour

    @departure_hour.setter
    def departure_hour(self, departure_hour):
        self.__departure_hour = departure_hour

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def job_role(self):
        return self.__job_role

    @job_role.setter
    def job_role(self, job_role):
        self.__job_role = job_role.title()

    @property
    def vt(self):
        return self.__vt

    @vt.setter
    def vt(self, vt):
        if vt in("Y", "N", "DEFAULT"):
            self.__vt = vt

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id


"""
employee = EmployeeGetSet("Beatriz Ferreira de Souza.", "1994/06/11", 25, "F", "912345654", "12345561890",
                          "1156629870", "11987650982", "Bernades de Souza", "2102", "", "04212098", 5, "18:00:00",
                          "22:00:00", 990.00, "Supervisora de Atendente","Y")

print(employee.name)
print(employee.birthday)
print(employee.age)
print(employee.sex)
print(employee.rg)
print(employee.cpf)
print(employee.telephone)
print(employee.cellphone)
print(employee.street)
print(employee.number)
print(employee.complement)
print(employee.cep)
print(employee.quantity_days)
print(employee.entry_hour)
print(employee.departure_hour)
print(employee.salary)
print(employee.job_role)
print(employee.vt)
"""
