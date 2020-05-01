from Sistema_Locadora.Operations_CRUD.Actions_Login import Login
from Sistema_Locadora.Getters_Setters.Login_Getters_Setters import LoginGetSet
from Sistema_Locadora.Menus.Validates_Menu import Validate
from Sistema_Locadora.Menus.Secundary_Menu import SecundaryMenu


class MainMenu:

    global login
    login = Login()

    global validate
    validate = Validate()

    def main_menu(self):

        print("_"*80)
        change = input("\n \t \t \t Menu de Login Locadora \n" + "_"*80 +
                       "\n 1º Login\n 2º Cadastrar\n 3º Esqueci a Minha Senha\n 4º Alterar a Pergunta do Login\n "
                       "5º Alterar a Reposta da Pergunta do Login\n 6º Alterar a Senha do Login\n "
                       "7º Exit\n Escolha a sua opção --> ")

        while change not in("1", "2", "3", "4", "5", "6", "7"):
            validate.validate_text_while()
            change = input("\n \t \t \t Menu de Login Locadora \n" + "_" * 80 +
                           "\n 1º Login\n 2º Cadastrar\n 3º Esqueci a Minha Senha\n 4º Alterar a Pergunta do Login\n "
                           "5º Alterar a Reposta da Pergunta do Login\n 6º Alterar a Senha do Login\n "
                           "7º Exit\n Escolha a sua opção --> ")

        if change == "1":
            self.logar()

        elif change == "2":
            self.register()

        elif change == "3":
            self.recover_password()

        elif change == "4":
            self.update_question()

        elif change == "5":
            self.update_answer()

        elif change == "6":
            self.update_password()

        elif change == "7":
            print("_"*80)
            print("Saindo do Sistem de Locadora.")
            exit()

    @staticmethod
    def logar():
        print("_" * 80)
        cpf = input("Digite o seu CPF: ")
        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")
        while cpf is "" or cpf.isdigit() is False or len(cpf) != 11:
            print("_" * 80)
            print("Por favor digite o seu CPF corretamente.")
            cpf = input("Digite o seu CPF: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")

        password = input("Digite a sua senha: ")
        while password is "":
            print("_" * 80)
            print("Por favor digite a sua senha.")
            password = input("Digite a sua senha: ")

        logado = login.logar(cpf, password)
        if logado == "Logado com Sucesso":
            user_id = login.return_id_func(cpf)
            job_role = login.return_job_rule(cpf)
            secundary_menu = SecundaryMenu()
            secundary_menu.secundary_menu(job_role, user_id)

    @staticmethod
    def register():
        print("_"*80)
        print("\t \t \t Cadastro de Logins de Funcionário. \n")
        cpf_validate = validate.validate_employee_cpf()

        password = input("Digite uma senha: ")
        while password is "":
            print("_"*80)
            print("Por favor digite a sua senha.")
            password = input("Digite uma senha: ")

        confirm_password = input("Digite a sua senha novamente: ")
        while confirm_password is "":
            print("_"*80)
            print("Por favor confirme a sua senha.")
            confirm_password = input("Digite a sua senha novamente: ")

        question = input("Digite uma pergunta para recuperar a senha: ")
        while question is "":
            print("_"*80)
            print("Por favor digite a pergunta.")
            question = input("Digite uma pergunta para recuperar a senha: ")

        answer = input("Digite uma resposta para a pergunta acima: ")
        while answer is "":
            print("_"*80)
            print("Por favor digite a resposta da pergunta acima.")
            answer = input("Digite uma resposta para a pergunta acima: ")

        if cpf_validate is not None and password == confirm_password:
            register = LoginGetSet(cpf_validate, password, question, answer)
            login.insert(register.cpf, register.password, register.question, register.answer)

        elif password != confirm_password:
            print("_"*80)
            print("O cadastro não foi feito, pois as senhas não coincidem.")

        elif cpf_validate is None:
            print("_"*80)
            print("Este CPF não está cadastrado no sistema.")

        else:
            print("_"*80)
            print("Não foi possível criar o login.")

    @staticmethod
    def recover_password():
        print("_" * 80)
        print("\t \t \t Esqueci a Minha Senha. \n")
        cpf_validate = validate.validate_employee_cpf()

        if cpf_validate is not None:
            login.recover_password(cpf_validate)
        else:
            print("_"*80)
            print("Este CPF não existe cadastrado no sistema.")
            print("_"*80)

    @staticmethod
    def update_question():
        print("_"*80)
        print("\t \t \t Alterar da Pergunta do Login \n")
        cpf_validate = validate.validate_employee_cpf()
        password_current = input("Digite a Sua Senha: ")
        logar = login.exist_login(cpf_validate, password_current)

        if logar is not None:

            question = input("Digite a Nova pergunta: ")
            while question is "":
                print("_"*80)
                print("Por favor digite a nova Pergunta.")
                question = input("Digite a Nova pergunta: ")

            confirm = input("Deseja realmente alterar a Pergunta(S - Sim ou N - Não): ")
            confirm = confirm.upper()
            if confirm == "S":
                login.update_question(cpf_validate, question)
            else:
                print("_"*80)
                print("A Alteração da Pergunta não foi realizada.")

        else:
            print("_"*80)
            print("O Login está Incorreto a Alteração não foi realizada...")

    @staticmethod
    def update_answer():
        print("_" * 80)
        print("\t \t \t Alterar da Reposta do Login \n")
        cpf_validate = validate.validate_employee_cpf()
        password_current = input("Digite a Sua Senha: ")
        logar = login.exist_login(cpf_validate, password_current)

        if logar is not None:
            answer = input("Digite a Nova Resposta da Pergunta do Login: ")
            while answer is "":
                print("_" * 80)
                print("Por favor digite a nova Resposta.")
                answer = input("Digite a Nova Resposta da Pergunta do Login: ")

            confirm = input("Deseja realmente alterar a Resposta(S - Sim ou N - Não): ")
            confirm = confirm.upper()
            if confirm == "S":
                login.update_answer(cpf_validate, answer)
            else:
                print("_" * 80)
                print("A Alteração da Resposta não foi realizada.")

        else:
            print("_"*80)
            print("O Login está incorreto a Alteração não foi realizada...")

    @staticmethod
    def update_password():
        print("_" * 80)
        print("\t \t \t Alterar da Senha do Login \n")
        cpf_validate = validate.validate_employee_cpf()
        password_current = input("Digite a Sua Senha Atual: ")
        login_validate = login.exist_login(cpf_validate, password_current)

        if login_validate is not None:
            password = input("Digite a Nova Senha do Login: ")
            confirm_password = input("Digite a Nova Senha do Login Novamente: ")
            while password is "":
                print("_" * 80)
                print("Por favor digite a nova Senha.")
                password = input("Digite a Nova Senha do Login: ")

            while confirm_password is "":
                print("_"*80)
                print("Por favor digite a nova Senha Novamente.")
                confirm_password = input("Digite a Nova Senha do Login Novamente: ")

            if password == confirm_password:
                confirm = input("Deseja realmente alterar a Senha(S - Sim ou N - Não): ")
                confirm = confirm.upper()
                if confirm == "S":
                    login.update_password(cpf_validate, password)
                else:
                    print("_" * 80)
                    print("A Alteração da Senha não foi realizada.")

            else:
                print("_"*80)
                print("As senhas não são as mesmas, a alteração não foi realizada.")

        else:
            print("_"*80)
            print("Login incorreto a Alteração não foi realizada...")


main_menu = MainMenu()
main_menu.main_menu()
