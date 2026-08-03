def informacoes():
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