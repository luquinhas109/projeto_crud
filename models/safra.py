class Safra:
    def __init__(
        self,
        nome_safra: str,
        cultura: str,
        ano_agricola: str,
        area_hectare: float,
        id_safra: int = None
    ):
        self.id_safra = id_safra
        self.nome_safra = nome_safra
        self.cultura = cultura
        self.ano_agricola = ano_agricola
        self.area_hectare = area_hectare

    def validar(self):
       
            if not self.nome_safra or not str(self.nome_safra).strip():
                raise ValueError("O nome da safra não pode ser vazio.")

            if not self.cultura or not str(self.cultura).strip():
                raise ValueError("A cultura (ex: Soja, Milho, Café) não pode ser vazia.")

            if not self.ano_agricola or not str(self.ano_agricola).strip():
                raise ValueError("O ano agrícola não pode ser vazio (ex: '2024/2025' ou '2025').")

            try:
                self.area_hectare = float(self.area_hectare)
            except (ValueError, TypeError):
                raise ValueError("A área em hectares deve ser um valor numérico.")


    def to_dict(self):
        
            return {
                "id_safra": self.id_safra,
                "nome_safra": self.nome_safra,
                "cultura": self.cultura,
                "ano_agricola": self.ano_agricola,
                "area_hectare": self.area_hectare
        }


    def __str__(self):
            
            id_txt = f"#{self.id_safra}" if self.id_safra is not None else "(Sem ID)"
            return (
                f"[{id_txt}] Safra: {self.nome_safra} | Cultura: {self.cultura} | "
                f"Ano: {self.ano_agricola} | Área: {self.area_hectare:.2f} ha"
            )