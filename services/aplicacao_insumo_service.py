
from models.aplicacao_insumo import AplicacaoInsumo
from repositories.aplicacao_insumo_repository import AplicacaoInsumoRepository
from repositories.insumo_database_repository import InsumoRepository
from repositories.safra_database_repository import SafraRepository


class AplicacaoInsumoService:

    def __init__(self):
        self.aplicacao_repo = AplicacaoInsumoRepository()
        self.insumo_repo = InsumoRepository()
        self.safra_repo = SafraRepository()

    def salvar(self, aplicacao: AplicacaoInsumo):
        aplicacao.validar()

        safra = self.safra_repo.buscar_por_id(aplicacao.id_safra)
        if safra is None:
            raise ValueError("Safra não encontrada.")

        insumo = self.insumo_repo.buscar_por_id(aplicacao.id_insumo)
        if insumo is None:
            raise ValueError("Insumo não encontrado.")

        # Validação e baixa no estoque de litros do insumo
        qtd_necessaria = float(aplicacao.quantidade_aplicada)
        qtd_disponivel = float(insumo.quantidade_litros)

        if qtd_necessaria > qtd_disponivel:
            raise ValueError(
                f"Estoque insuficiente de '{insumo.nome_comercial}'! "
                f"Disponível: {qtd_disponivel:.2f} L | Solicitado: {qtd_necessaria:.2f} L"
            )

        # Abate do estoque
        insumo.quantidade_litros = round(qtd_disponivel - qtd_necessaria, 2)
        self.insumo_repo.update(insumo)

        aplicacao.calcular_custo_total(
            float(insumo.custo_unitario)
        )

        return self.aplicacao_repo.salvar(aplicacao)

    def listar(self):
        return self.aplicacao_repo.listar()

    def buscar_por_id(self, id_aplicacao: int):
        if id_aplicacao <= 0:
            raise ValueError("Informe um ID válido.")

        aplicacao = self.aplicacao_repo.buscar_por_id(id_aplicacao)

        if aplicacao is None:
            raise ValueError("Aplicação não encontrada.")

        return aplicacao

    def update(self, aplicacao: AplicacaoInsumo):
        aplicacao.validar()

        if aplicacao.id_aplicacao is None:
            raise ValueError("Informe o ID da aplicação.")

        safra = self.safra_repo.buscar_por_id(aplicacao.id_safra)
        if safra is None:
            raise ValueError("Safra não encontrada.")

        insumo = self.insumo_repo.buscar_por_id(aplicacao.id_insumo)
        if insumo is None:
            raise ValueError("Insumo não encontrado.")

        aplicacao.calcular_custo_total(
            float(insumo.custo_unitario)
        )

        return self.aplicacao_repo.update(aplicacao)

    def delete(self, id_aplicacao: int):
        if id_aplicacao <= 0:
            raise ValueError("Informe um ID válido.")

        aplicacao = self.aplicacao_repo.buscar_por_id(id_aplicacao)
        if aplicacao:
            # Estorna a quantidade de volta ao estoque do insumo
            insumo = self.insumo_repo.buscar_por_id(aplicacao.id_insumo)
            if insumo:
                insumo.quantidade_litros = round(
                    float(insumo.quantidade_litros) + float(aplicacao.quantidade_aplicada), 2
                )
                self.insumo_repo.update(insumo)

        return self.aplicacao_repo.delete(id_aplicacao)
