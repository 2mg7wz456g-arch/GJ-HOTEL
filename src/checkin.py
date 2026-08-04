from models import Hospede
from models import Reserva
from models import quarto
from quartos import quartos
from banco import salvar_hospede


def cadastrar_hospede():
        cpf = input("CPF: ").strip()
        nome_completo = input("Nome completo: ").strip() .title()
        data_de_nascimento = input("Data de nascimento: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()

        cep = input("CEP: ").strip()
        logradouro = input("Logradouro: ").strip().title()
        numero = input("Número: ").strip()
        complemento = input("Complemento: ").strip().title()
        bairro = input("Bairro: ").strip().title()
        cidade = input("Cidade: ").strip().title()
        estado = input("Estado: ").strip() .title() .upper()
        pais = input("Pais: ").strip() .title()

        hospede = Hospede(cpf,nome_completo, data_de_nascimento, telefone,
                          email, cep, logradouro, numero, complemento, bairro,
                          cidade, estado, pais)

        return hospede



def check_in():
        print("Você escolheu check-in")
    
        possui_reserva = input("O senhor possui reserva? ").strip().lower()
    
        if possui_reserva == "sim":
                print("Vamos localizar sua reserva")

                # Depois criaremos aqui a busca pelo código da reserva.

        elif possui_reserva == "nao":
                print("Vamos verificar a disponibilidade.")

                hospede = cadastrar_hospede()

                print("===============")
                print("Nome: ", hospede.nome_completo)
                print("CPF: ", hospede.cpf)
                print("Data de nascimento: ", hospede.data_de_nascimento)
                print("Telefone: ", hospede.telefone)
                print("E-mail: ", hospede.email)
                print("Cidade: ", hospede.cidade)
                print("Estado: ", hospede.estado)
                print("===============")

                dados_corretos = input(
                        "Os dados estão corretos? "
                ).strip() .lower()      

                if dados_corretos == "sim":
                        salvar_hospede(hospede)
                        print("===============")
                        print("Check-in realizado, obrigado por escolher a Blue Tree")
                else:
                        print("Cadastro não confirmado")   

        else:
                print("Resposta inválida")                     


