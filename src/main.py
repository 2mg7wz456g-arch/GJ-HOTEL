def encerrar():
        print("Encerrando sistema")

from checkin import check_in
from menu import mostrar_menu
from checkout import check_out

opcao = mostrar_menu()

print(opcao)


opcao = ""
while opcao != "3":

    opcao = mostrar_menu()
        
    if opcao == "1":
                check_in()
    elif opcao =="2":
                check_out()
    elif opcao == "3":
                encerrar()
                         
                        