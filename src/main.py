from informacao import informacoes
from checkin import check_in
from menu import mostrar_menu
from checkout import check_out


def encerrar():
    print("Encerrando sistema")




opcao = ""
while opcao != "4":

    opcao = mostrar_menu()
        
    if opcao == "1":
                check_in()
    elif opcao =="2":
                check_out()
    elif opcao == "3":
                informacoes()
    elif opcao =="4":
                encerrar()
                         
                        