
from datetime import date, datetime


class AplicacaoInsumo:
    def __init__(
        self,
        id_safra: int,
        id_insumo: int,
        quantidade_aplicada: float,
        data_aplicacao: date | str,
        custo_total: float = 0.0,
        id_aplicacao: int = None
    ):
        self.id_aplicacao = id_aplicacao
        self.id_safra = id_safra
        self.id_insumo = id_insumo
        self.quantidade_aplicada = quantidade_aplicada
        self.data_aplicacao = data_aplicacao
        self.custo_total = custo_total

    def validar(self):
        # Verifica se a quantidade é numérica e positiva
        try:
            self.quantidade_aplicada = float(self.quantidade_aplicada)
        except (ValueError, TypeError):
            raise ValueError("A quantidade aplicada deve ser numérica.")

        if self.quantidade_aplicada <= 0:
            raise ValueError("A quantidade aplicada deve ser maior que zero.")

        # Verifica se a data está em um formato válido
        if isinstance(self.data_aplicacao, str):
            try:
                self.data_aplicacao = datetime.strptime(
                    self.data_aplicacao, "%d/%m/%Y"
                ).date()
            except ValueError:
                try:
                    self.data_aplicacao = datetime.strptime(
                        self.data_aplicacao, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    raise ValueError(
                        "Data inválida. Utilize DD/MM/AAAA."
                    )

        elif not isinstance(self.data_aplicacao, date):
            raise ValueError("A data da aplicação é inválida.")

        # Verifica os relacionamentos
        if not self.id_safra or self.id_safra <= 0:
            raise ValueError("Selecione uma safra válida.")

        if not self.id_insumo or self.id_insumo <= 0:
            raise ValueError("Selecione um insumo válido.")

    def calcular_custo_total(self, custo_unitario: float):
        if custo_unitario < 0:
            raise ValueError("O custo unitário não pode ser negativo.")

        self.custo_total = round(
            self.quantidade_aplicada * custo_unitario, 2
        )

        return self.custo_total

    def to_dict(self):
        return {
            "id_aplicacao": self.id_aplicacao,
            "id_safra": self.id_safra,
            "id_insumo": self.id_insumo,
            "quantidade_aplicada": self.quantidade_aplicada,
            "data_aplicacao": self.data_aplicacao,
            "custo_total": self.custo_total
        }

    def __str__(self):
        id_txt = (
            f"#{self.id_aplicacao}"
            if self.id_aplicacao is not None
            else "(Sem ID)"
        )

        return (
            f"[{id_txt}] Safra: {self.id_safra} | "
            f"Insumo: {self.id_insumo} | "
            f"Quantidade: {self.quantidade_aplicada} | "
            f"Data: {self.data_aplicacao} | "
            f"Custo total: R${self.custo_total:.2f}"
        )
