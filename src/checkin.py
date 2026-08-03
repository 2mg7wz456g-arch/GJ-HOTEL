from models import Hospede
from models import Reserva
from models import quarto
from quartos import quartos


def check_in():
        print("Você escolheu check-in")
    
        possui_reserva = input("O senhor possui reserva? ").strip().lower()
    
        if possui_reserva == "sim":
                print("Vamos localizar sua reserva")
                nome_do_hospede=input("Informe seu nome completo   ").strip().title()
                cpf=input("Informe seu CPF   ").strip()
                data_de_nascimento = input("Data de nascimento: ").strip()
                quantidade_de_hospedes=input("Quantos hospedes vão ficar no quarto?   ").strip().lower()
                print("=============")
                print("Nome:", nome_do_hospede)
                print("CPF:", cpf)
                print("Data de nascimento: ", data_de_nascimento)
                print("Quantidade de hospedes:", quantidade_de_hospedes)
                dados_corretos=input("Os dados estão corretos?").strip().lower()
                if dados_corretos== "sim":
                            hospede = Hospede(nome_do_hospede,
                                              cpf,
                                              data_de_nascimento)

                print("Nome:", hospede.nome_do_hospede)
                print("CPF:", hospede.cpf)
                print("Data:", hospede.data_de_nascimento)

                            
                print("=============")
                print("Check-In realizado, obrigado por escolher a blue tree")
        elif possui_reserva == "nao":
                print("Vamos verificar a disponibilidade")
    
        else:
                print("Resposta inválida")

quantidade_de_hospedes = 2
for quarto in quartos:
        if quarto.status =="Disponivel" and quarto.capacidade >= quantidade_de_hospedes:
                print("Quarto localizado","=", quarto.numero_do_quarto)
