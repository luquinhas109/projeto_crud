import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "agrotech"))


# pyrefly: ignore[missing-import]
from views.safra_view import menu_safra

def main():
    while True:
        print("\n" + "="*40)
        print("SISTEMA AGROTECH")
        print("="*40)
        print("1 - Gerenciar Safras")
        print("0 - Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_safra()
        elif opcao == "0":
            print("\nEncerrando o programa.")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()