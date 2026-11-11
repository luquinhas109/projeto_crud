
from view.safra_view import menu_safra
from view.insumo_view import menu_insumo
from view.aplicacao_insumo_view import menu_aplicacao_insumo


def main():
    while True:
        print("\n========== SISTEMA AGROTECH ==========")
        print("1 - Gerenciar Safras")
        print("2 - Gerenciar Insumos")
        print("3 - Gerenciar Aplicações de Insumos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_safra()
        elif opcao == "2":
            menu_insumo()
        elif opcao == "3":
            menu_aplicacao_insumo()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

