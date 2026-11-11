
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

        return self.aplicacao_repo.delete(id_aplicacao)
