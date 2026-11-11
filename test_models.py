import pytest
from datetime import date
from models.safra import Safra
from models.insumo import Insumo
from models.aplicacao_insumo import AplicacaoInsumo


class TestSafra:
    def test_criacao_safra_valida(self):
        safra = Safra(
            nome_safra="Safra Verão 2024",
            cultura="Soja",
            ano_agricola="2024/2025",
            area_hectare=150.5,
            id_safra=1
        )
        safra.validar()

        assert safra.nome_safra == "Safra Verão 2024"
        assert safra.cultura == "Soja"
        assert safra.ano_agricola == "2024/2025"
        assert safra.area_hectare == 150.5
        assert safra.id_safra == 1

    def test_safra_nome_vazio_lanca_excecao(self):
        safra = Safra(
            nome_safra="   ",
            cultura="Milho",
            ano_agricola="2024/2025",
            area_hectare=50.0
        )
        with pytest.raises(ValueError, match="O nome da safra não pode ser vazio."):
            safra.validar()

    def test_safra_cultura_vazia_lanca_excecao(self):
        safra = Safra(
            nome_safra="Safra 2024",
            cultura="",
            ano_agricola="2024/2025",
            area_hectare=50.0
        )
        with pytest.raises(ValueError, match="A cultura .* não pode ser vazia."):
            safra.validar()

    def test_safra_ano_agricola_vazio_lanca_excecao(self):
        safra = Safra(
            nome_safra="Safra 2024",
            cultura="Café",
            ano_agricola="",
            area_hectare=50.0
        )
        with pytest.raises(ValueError, match="O ano agrícola não pode ser vazio"):
            safra.validar()

    def test_safra_area_invalida_lanca_excecao(self):
        safra = Safra(
            nome_safra="Safra 2024",
            cultura="Trigo",
            ano_agricola="2024",
            area_hectare="cem"
        )
        with pytest.raises(ValueError, match="A área em hectares deve ser um valor numérico."):
            safra.validar()

    def test_safra_to_dict(self):
        safra = Safra(
            id_safra=2,
            nome_safra="Safra Inverno",
            cultura="Trigo",
            ano_agricola="2024",
            area_hectare=80.0
        )
        dados = safra.to_dict()
        assert dados == {
            "id_safra": 2,
            "nome_safra": "Safra Inverno",
            "cultura": "Trigo",
            "ano_agricola": "2024",
            "area_hectare": 80.0
        }


class TestInsumo:
    def test_criacao_insumo(self):
        insumo = Insumo(
            id_insumo=1,
            nome_comercial="Glifosato",
            tipo_insumo="Herbicida",
            custo_unitario=45.50,
            quantidade_litros=100.0
        )
        assert insumo.id_insumo == 1
        assert insumo.nome_comercial == "Glifosato"
        assert insumo.tipo_insumo == "Herbicida"
        assert insumo.custo_unitario == 45.50
        assert insumo.quantidade_litros == 100.0


class TestAplicacaoInsumo:
    def test_criacao_aplicacao_valida(self):
        aplicacao = AplicacaoInsumo(
            id_safra=1,
            id_insumo=2,
            quantidade_aplicada=15.5,
            data_aplicacao="15/10/2024",
            id_aplicacao=10
        )
        aplicacao.validar()

        assert aplicacao.id_safra == 1
        assert aplicacao.id_insumo == 2
        assert aplicacao.quantidade_aplicada == 15.5
        assert aplicacao.data_aplicacao == date(2024, 10, 15)

    def test_aplicacao_com_data_iso(self):
        aplicacao = AplicacaoInsumo(
            id_safra=1,
            id_insumo=2,
            quantidade_aplicada=10,
            data_aplicacao="2024-10-15"
        )
        aplicacao.validar()
        assert aplicacao.data_aplicacao == date(2024, 10, 15)

    def test_aplicacao_quantidade_invalida(self):
        aplicacao = AplicacaoInsumo(
            id_safra=1,
            id_insumo=2,
            quantidade_aplicada=-5,
            data_aplicacao="15/10/2024"
        )
        with pytest.raises(ValueError, match="A quantidade aplicada deve ser maior que zero."):
            aplicacao.validar()

    def test_aplicacao_data_invalida(self):
        aplicacao = AplicacaoInsumo(
            id_safra=1,
            id_insumo=2,
            quantidade_aplicada=10,
            data_aplicacao="data-invalida"
        )
        with pytest.raises(ValueError, match="Data inválida. Utilize DD/MM/AAAA."):
            aplicacao.validar()

    def test_aplicacao_safra_ou_insumo_invalido(self):
        aplicacao_safra_invalida = AplicacaoInsumo(
            id_safra=0,
            id_insumo=1,
            quantidade_aplicada=10,
            data_aplicacao="15/10/2024"
        )
        with pytest.raises(ValueError, match="Selecione uma safra válida."):
            aplicacao_safra_invalida.validar()

        aplicacao_insumo_invalido = AplicacaoInsumo(
            id_safra=1,
            id_insumo=0,
            quantidade_aplicada=10,
            data_aplicacao="15/10/2024"
        )
        with pytest.raises(ValueError, match="Selecione um insumo válido."):
            aplicacao_insumo_invalido.validar()

    def test_calcular_custo_total(self):
        aplicacao = AplicacaoInsumo(
            id_safra=1,
            id_insumo=2,
            quantidade_aplicada=10.5,
            data_aplicacao="15/10/2024"
        )
        custo = aplicacao.calcular_custo_total(custo_unitario=20.0)
        assert custo == 210.0
        assert aplicacao.custo_total == 210.0

    def test_calcular_custo_total_negativo_lanca_excecao(self):
        aplicacao = AplicacaoInsumo(
            id_safra=1,
            id_insumo=2,
            quantidade_aplicada=10.0,
            data_aplicacao="15/10/2024"
        )
        with pytest.raises(ValueError, match="O custo unitário não pode ser negativo."):
            aplicacao.calcular_custo_total(custo_unitario=-10.0)

