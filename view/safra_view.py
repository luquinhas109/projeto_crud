from datetime import datetime
from models.safra import Safra
from repositories.safra_database_repository import SafraRepository

def menu_safra():
    
    repo = SafraRepository()

    while True:
        print("\n" + "="*40)
        print("GESTÃO DE SAFRAS - AGROTECH")
        print("="*40)
        print("1 - Cadastrar Safra")
        print("2 - Listar Safras")
        print("3 - Buscar Safra por ID")
        print("4 - Atualizar Safra")
        print("5 - Excluir Safra")
        print("0 - Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        
        if opcao == "1":
            print("\n--- Novo Cadastro de Safra ---")
            try:
                nome = input("Nome da Safra (ex: Safra Verão 2025): ").strip()
                cultura = input("Cultura (ex: Soja, Milho, Café): ").strip()
                data_usuario = input("Data de início/Ano Agrícola (DD/MM/AAAA): ").strip()
                try:
                    ano = datetime.strptime(data_usuario, "%d/%m/%Y").strftime("%Y-%m-%d")
                except ValueError:
                    raise ValueError("Data inválida! Use o formato DD/MM/AAAA (ex: 01/01/2026).")
                area = float(input("Área em Hectares: "))

                
                nova_safra = Safra(nome_safra=nome, cultura=cultura, ano_agricola=ano, area_hectare=area)
                
                
                repo.salvar(nova_safra)
                print(f"Safra cadastrada com sucesso! ID gerado: {nova_safra.id_safra}")

            except ValueError as e:
                print(f" Erro de validação: {e}")
            except Exception as e:
                print(f" Ocorreu um erro ao salvar: {e}")

        
        elif opcao == "2":
            print("\n--- Lista de Safras Cadastradas ---")
            try:
                safras = repo.listar()
                if not safras:
                    print("Nenhuma safra cadastrada até o momento.")
                else:
                    for s in safras:
                        print(s) 
            except Exception as e:
                print(f" Erro ao listar: {e}")

      
        elif opcao == "3":
            try:
                id_busca = int(input("\nInforme o ID da safra: "))
                safra = repo.buscar_por_id(id_busca)
                if safra:
                    print("\nSafra Encontrada:")
                    print(safra)
                else:
                    print(f" Nenhuma safra encontrada com o ID {id_busca}.")
            except ValueError:
                print("❌ Digite um número inteiro válido para o ID.")

        
        elif opcao == "4":
            try:
                id_atualizar = int(input("\nInforme o ID da safra que deseja atualizar: "))
                safra_existente = repo.buscar_por_id(id_atualizar)

                if not safra_existente:
                    print(f" Nenhuma safra encontrada com o ID {id_atualizar}.")
                    continue

                print(f"Dados atuais: {safra_existente}")
                print("Digite os novos dados (ou repita os atuais):")
                
                nome = input("Novo Nome: ").strip()
                cultura = input("Nova Cultura: ").strip()
                data_usuario = input("Nova Data de início/Ano Agrícola (DD/MM/AAAA): ").strip()
                try:
                    ano = datetime.strptime(data_usuario, "%d/%m/%Y").strftime("%Y-%m-%d")
                except ValueError:
                    raise ValueError("Data inválida! Use o formato DD/MM/AAAA (ex: 01/01/2026).")
                area = float(input("Nova Área em Hectares: "))

                
                safra_atualizada = Safra(
                    id_safra=id_atualizar,
                    nome_safra=nome,
                    cultura=cultura,
                    ano_agricola=ano,
                    area_hectare=area
                )

                if repo.update(safra_atualizada):
                    print(" Safra atualizada com sucesso!")
                else:
                    print(" Falha ao atualizar a safra.")

            except ValueError as e:
                print(f" Erro de validação: {e}")

       
        elif opcao == "5":
            try:
                id_excluir = int(input("\nInforme o ID da safra a ser excluída: "))
                confirmacao = input(f"Tem certeza que deseja excluir a safra #{id_excluir}? (s/n): ").strip().lower()

                if confirmacao == "s":
                    if repo.delete(id_excluir):
                        print(" Safra excluída com sucesso!")
                    else:
                        print(f" Nenhuma safra encontrada com o ID {id_excluir}.")
                else:
                    print("Operação cancelada.")
            except ValueError:
                print(" Digite um ID numérico válido.")

        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break

        else:
            print(" Opção inválida! Escolha um número de 0 a 5.")

if __name__ == "__main__":
    menu_safra()