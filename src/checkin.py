def check_in():
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