
import re

from models.safra import Safra
from repositories.safra_database_repository import SafraRepository


def validar_ano_agricola(valor):
    if not re.fullmatch(r"\d{4}/\d{4}", valor):
        raise ValueError(
            "Ano agrícola inválido! Use AAAA/AAAA (ex: 2026/2027)."
        )
    return valor


def menu_safra():
    repo = SafraRepository()

    while True:
        print("\n" + "=" * 40)
        print("GESTÃO DE SAFRAS - AGROTECH")
        print("=" * 40)
        print("1 - Cadastrar Safra")
        print("2 - Listar Safras")
        print("3 - Buscar Safra por ID")
        print("4 - Atualizar Safra")
        print("5 - Excluir Safra")
        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Novo Cadastro de Safra ---")
            try:
                nome = input("Nome da Safra: ").strip()
                cultura = input("Cultura: ").strip()
                ano = validar_ano_agricola(
                    input("Ano Agrícola (AAAA/AAAA): ").strip()
                )
                area = float(input("Área em Hectares: "))

                nova_safra = Safra(
                    nome_safra=nome,
                    cultura=cultura,
                    ano_agricola=ano,
                    area_hectare=area
                )

                repo.salvar(nova_safra)
                print(
                    f"Safra cadastrada com sucesso! "
                    f"ID gerado: {nova_safra.id_safra}"
                )

            except ValueError as erro:
                print(f"Erro de validação: {erro}")
            except Exception as erro:
                print(f"Erro ao salvar: {erro}")

        elif opcao == "2":
            print("\n--- Lista de Safras Cadastradas ---")
            try:
                safras = repo.listar()

                if not safras:
                    print("Nenhuma safra cadastrada.")
                else:
                    for safra in safras:
                        print(safra)

            except Exception as erro:
                print(f"Erro ao listar: {erro}")

        elif opcao == "3":
            try:
                id_busca = int(input("Informe o ID da safra: "))
                safra = repo.buscar_por_id(id_busca)

                if safra:
                    print("\nSafra encontrada:")
                    print(safra)
                else:
                    print("Safra não encontrada.")

            except ValueError:
                print("Digite um ID inteiro válido.")
            except Exception as erro:
                print(f"Erro ao buscar: {erro}")

        elif opcao == "4":
            try:
                id_atualizar = int(
                    input("ID da safra que deseja atualizar: ")
                )
                safra_existente = repo.buscar_por_id(id_atualizar)

                if not safra_existente:
                    print("Safra não encontrada.")
                    continue

                print(f"Dados atuais: {safra_existente}")

                nome = input("Novo nome: ").strip()
                cultura = input("Nova cultura: ").strip()
                ano = validar_ano_agricola(
                    input("Novo Ano Agrícola (AAAA/AAAA): ").strip()
                )
                area = float(input("Nova área em hectares: "))

                safra_atualizada = Safra(
                    id_safra=id_atualizar,
                    nome_safra=nome,
                    cultura=cultura,
                    ano_agricola=ano,
                    area_hectare=area
                )

                if repo.update(safra_atualizada):
                    print("Safra atualizada com sucesso!")
                else:
                    print("Falha ao atualizar a safra.")

            except ValueError as erro:
                print(f"Erro de validação: {erro}")
            except Exception as erro:
                print(f"Erro ao atualizar: {erro}")

        elif opcao == "5":
            try:
                id_excluir = int(
                    input("ID da safra que deseja excluir: ")
                )
                confirmacao = input(
                    "Tem certeza que deseja excluir? (s/n): "
                ).strip().lower()

                if confirmacao == "s":
                    if repo.delete(id_excluir):
                        print("Safra excluída com sucesso!")
                    else:
                        print("Safra não encontrada.")
                else:
                    print("Operação cancelada.")

            except ValueError:
                print("Digite um ID numérico válido.")
            except Exception as erro:
                print(f"Erro ao excluir: {erro}")

        elif opcao == "0":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_safra()
