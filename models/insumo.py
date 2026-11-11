class Insumo:
    def __init__(
        self,
        id_insumo=None,
        nome_comercial="",
        tipo_insumo="",
        custo_unitario=0.0,
        quantidade_litros=0.0
    ):
        self.id_insumo = id_insumo
        self.nome_comercial = nome_comercial
        self.tipo_insumo = tipo_insumo
        self.custo_unitario = custo_unitario
        self.quantidade_litros = quantidade_litros

    def __str__(self):
        return (
            f"ID: {self.id_insumo} | "
            f"Nome: {self.nome_comercial} | "
            f"Tipo: {self.tipo_insumo} | "
            f"Estoque: {self.quantidade_litros:.2f} L | "
            f"Custo: R$ {self.custo_unitario:.2f}/L"
        )


    