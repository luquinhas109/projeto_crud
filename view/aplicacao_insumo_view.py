
from datetime import datetime

from models.aplicacao_insumo import AplicacaoInsumo
from services.aplicacao_insumo_service import AplicacaoInsumoService


service = AplicacaoInsumoService()


def cadastrar():
    try:
        print("\n--- CADASTRAR APLICAÇÃO ---")

        id_safra = int(input("ID da safra: "))
        id_insumo = int(input("ID do insumo: "))
        quantidade = float(input("Quantidade aplicada: "))
        data = input("Data (DD/MM/AAAA): ")

        aplicacao = AplicacaoInsumo(
            id_safra=id_safra,
            id_insumo=id_insumo,
            quantidade_aplicada=quantidade,
            data_aplicacao=data
        )

        service.salvar(aplicacao)
        print("Aplicação cadastrada com sucesso!")

    except (ValueError, Exception) as erro:
        print(f"Erro ao cadastrar: {erro}")


def listar():
    try:
        aplicacoes = service.listar()

        print("\n--- APLICAÇÕES CADASTRADAS ---")

        if not aplicacoes:
            print("Nenhuma aplicação encontrada.")
            return

        for aplicacao in aplicacoes:
            print(aplicacao)

    except Exception as erro:
        print(f"Erro ao listar: {erro}")


def buscar():
    try:
        id_aplicacao = int(input("ID da aplicação: "))
        aplicacao = service.buscar_por_id(id_aplicacao)
        print(aplicacao)

    except Exception as erro:
        print(f"Erro ao buscar: {erro}")


def atualizar():
    try:
        id_aplicacao = int(input("ID da aplicação que deseja atualizar: "))
        aplicacao = service.buscar_por_id(id_aplicacao)

        print("Informe os novos dados:")

        aplicacao.id_safra = int(input("Novo ID da safra: "))
        aplicacao.id_insumo = int(input("Novo ID do insumo: "))
        aplicacao.quantidade_aplicada = float(
            input("Nova quantidade aplicada: ")
        )
        aplicacao.data_aplicacao = input("Nova data (DD/MM/AAAA): ")

        service.update(aplicacao)
        print("Aplicação atualizada com sucesso!")

    except Exception as erro:
        print(f"Erro ao atualizar: {erro}")


def excluir():
    try:
        id_aplicacao = int(input("ID da aplicação que deseja excluir: "))
        service.delete(id_aplicacao)
        print("Aplicação excluída com sucesso!")

    except Exception as erro:
        print(f"Erro ao excluir: {erro}")


def menu_aplicacao_insumo():
    while True:
        print("\n===== APLICAÇÕES DE INSUMOS =====")
        print("1 - Cadastrar aplicação")
        print("2 - Listar aplicações")
        print("3 - Buscar aplicação")
        print("4 - Atualizar aplicação")
        print("5 - Excluir aplicação")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            atualizar()
        elif opcao == "5":
            excluir()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

