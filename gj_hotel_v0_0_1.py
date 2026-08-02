print("Bem vindo ao Blue Tree Towers Bauru")
def saudacao():
    print("""
=================================
      GJ-AI HOTEL v0.0.1
=================================

1 - Check-in
2 - Check-out
3 - Informações
4 - Encerrar
""")
 

solicitacao = ""

while solicitacao != "4":

    saudacao()

    solicitacao = input("Como posso ajudar o senhor hoje? ").strip()

    if solicitacao == "1":
        print("Você escolheu check-in")

        possui_reserva = input("O senhor possui reserva? ").strip().lower()

        if possui_reserva == "sim":
            print("Vamos localizar sua reserva")
            nome_do_hospede=input("Informe seu nome completo   ").strip().title()
            cpf=input("Informe seu CPF   ").strip()
            quantidade_de_hospedes=input("Quantos hospedes vão ficar no quarto?   ").strip().lower()
            print("=============")
            print("Nome do Hospede:", nome_do_hospede)
            print("CPF:", cpf)
            print("Quantidade de hospedes:", quantidade_de_hospedes)
            dados_corretos=input("Os dados estão corretos?").strip().lower()
            if dados_corretos== "sim":
                        print("=============")
                        print("Check-In realizado, obrigado por escolher a blue tree")
            else:
                    print("Operação cancelada")
        elif possui_reserva == "nao":
            print("Vamos verificar a disponibilidade")

        else:
            print("Resposta inválida")

    elif solicitacao == "2":
        numero_do_quarto=input("Você escolheu check-out, digite o número do quarto: ").strip().lower()
        nome_do_hospede=input("informe seu nome completo: ").strip().title()
        print("===========")
        print("Hospede: ",nome_do_hospede)
        print("Quarto:", numero_do_quarto)
        print("Check-out realizado com sucesso, volte sempre")
        print("===========")

    elif solicitacao == "3":
        print("Qual informação o senhor deseja?")
        print("1.horário do café")
        print("2.Pscina")
        print("3.wifi")
        informacao=input("Selecione a opção desejada: ").strip()
        if informacao=="1":
            print("O café da manhã funciona das 06:00 as 10:00 em dias de semana" \
            "e das 06:30 as 10:30 nos finais de semana")
        elif informacao=="2":
            print("A pscina e academia ficam no 16 andar e funcinam das 07:00 as 22:00 todos os dias.")
        elif informacao=="3":
            print("O login do wifi será seu numero de quarto e a senha seu sobrenome")  

    elif solicitacao == "4":
        print("Encerrando sistema")
    else:
        print("Opção inválida")
 
