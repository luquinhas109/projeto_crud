from models.insumo import Insumo
from repositories.insumo_database_repository import InsumoRepository

def menu_insumo():

    repo = InsumoRepository()

    while True:
        print("\n" + "=" * 40)
        print("GESTÃO DE INSUMOS - AGROTECH")
        print("=" * 40)
        print("1 - Cadastrar Insumo")
        print("2 - Listar Insumos")
        print("3 - Buscar Insumo por ID")
        print("4 - Atualizar Insumo")
        print("5 - Excluir Insumo")
        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Novo Cadastro de Insumo ---")

            try:
                nome = input("Nome comercial: ").strip()
                tipo = input("Tipo de insumo: ").strip()
                custo = float(input("Custo unitário por Litro (ex: 100): R$ "))
                quantidade = float(input("Quantidade total em estoque (Litros): "))

                if not nome or not tipo:
                    raise ValueError("Preencha todos os campos.")

                if custo < 0:
                    raise ValueError("O custo não pode ser negativo.")

                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa.")

                novo_insumo = Insumo(
                    nome_comercial=nome,
                    tipo_insumo=tipo,
                    custo_unitario=custo,
                    quantidade_litros=quantidade
                )

                repo.salvar(novo_insumo)

                print(f"Insumo cadastrado com sucesso! ID: {novo_insumo.id_insumo}")

            except ValueError as e:
                print(f"Erro de validação: {e}")

            except Exception as e:
                print(f"Erro ao cadastrar insumo: {e}")

        elif opcao == "2":
            print("\n--- Lista de Insumos ---")

            try:
                insumos = repo.listar()

                if not insumos:
                    print("Nenhum insumo cadastrado.")

                else:
                    for insumo in insumos:
                        print(insumo)

            except Exception as e:
                print(f"Erro ao listar insumos: {e}")

        elif opcao == "3":
            try:
                id_busca = int(input("Informe o ID do insumo: "))

                insumo = repo.buscar_por_id(id_busca)

                if insumo:
                    print("\nInsumo encontrado:")
                    print(insumo)

                else:
                    print("Insumo não encontrado.")

            except ValueError:
                print("Digite um ID numérico válido.")

            except Exception as e:
                print(f"Erro ao buscar insumo: {e}")

        elif opcao == "4":
            try:
                id_atualizar = int(input("Informe o ID do insumo: "))

                insumo_existente = repo.buscar_por_id(id_atualizar)

                if not insumo_existente:
                    print("Insumo não encontrado.")
                    continue

                print(f"Dados atuais: {insumo_existente}")

                nome = input("Novo nome: ").strip()
                tipo = input("Novo tipo: ").strip()
                custo = float(input("Novo custo unitário por Litro: R$ "))
                quantidade = float(input("Nova quantidade em estoque (Litros): "))

                if not nome or not tipo:
                    raise ValueError("Preencha todos os campos.")

                if custo < 0:
                    raise ValueError("O custo não pode ser negativo.")

                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa.")

                insumo_atualizado = Insumo(
                    id_insumo=id_atualizar,
                    nome_comercial=nome,
                    tipo_insumo=tipo,
                    custo_unitario=custo,
                    quantidade_litros=quantidade
                )

                if repo.update(insumo_atualizado):
                    print("Insumo atualizado com sucesso!")

                else:
                    print("Falha ao atualizar insumo.")

            except ValueError as e:
                print(f"Erro de validação: {e}")

            except Exception as e:
                print(f"Erro ao atualizar: {e}")

        elif opcao == "5":
            try:
                id_excluir = int(input("Informe o ID do insumo: "))

                confirmacao = input(
                    "Tem certeza que deseja excluir? (s/n): "
                ).strip().lower()

                if confirmacao == "s":

                    if repo.delete(id_excluir):
                        print("Insumo excluído com sucesso!")

                    else:
                        print("Insumo não encontrado.")

                else:
                    print("Operação cancelada.")

            except ValueError:
                print("Digite um ID numérico válido.")

            except Exception as e:
                print(f"Erro ao excluir insumo: {e}")

        elif opcao == "0":
            print("Saindo do gerenciamento de insumos.")
            break

        else:
            print("Opção inválida! Escolha de 0 a 5.")


if __name__ == "__main__":
    menu_insumo()