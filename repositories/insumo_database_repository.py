from models.insumo import Insumo
from database.connector import connect




class InsumoRepository:
    def salvar(self, insumo: Insumo):
        conexao = connect()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO Insumo (nome_comercial, tipo_insumo, custo_unitario, quantidade_litros)
        VALUES (%s, %s, %s, %s)
        """

        valores = (
            insumo.nome_comercial,
            insumo.tipo_insumo,
            insumo.custo_unitario,
            insumo.quantidade_litros
        )

        cursor.execute(sql, valores)
        conexao.commit()

        insumo.id_insumo = cursor.lastrowid

        cursor.close()
        conexao.close()

        return insumo

    def listar(self) -> list[Insumo]:
        conexao = connect()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Insumo")
        linhas = cursor.fetchall()

        cursor.close()
        conexao.close()

        lista_insumos = []

        for linha in linhas:
            insumo = Insumo(
                id_insumo = linha["id_insumo"],
                nome_comercial = linha["nome_comercial"],
                tipo_insumo = linha["tipo_insumo"],
                custo_unitario = float(linha["custo_unitario"]),
                quantidade_litros = float(linha.get("quantidade_litros") or 0.0)
            )

            lista_insumos.append(insumo)

        return lista_insumos

    def buscar_por_id(self, id_insumo: int) -> Insumo | None:
        conexao = connect()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM Insumo WHERE id_insumo = %s"

        cursor.execute(sql, (id_insumo,))
        linha = cursor.fetchone()

        cursor.close()
        conexao.close()

        if not linha:
            return None

        return Insumo(
            id_insumo = linha["id_insumo"],
            nome_comercial=linha["nome_comercial"],
            tipo_insumo = linha["tipo_insumo"],
            custo_unitario = float(linha["custo_unitario"]),
            quantidade_litros = float(linha.get("quantidade_litros") or 0.0)
        )

    def update(self, insumo: Insumo) -> bool:
        conexao = connect()
        cursor = conexao.cursor()

        sql = """
        UPDATE Insumo
        SET nome_comercial = %s,
            tipo_insumo = %s,
            custo_unitario = %s,
            quantidade_litros = %s
        WHERE id_insumo = %s
        """

        valores = (
            insumo.nome_comercial,
            insumo.tipo_insumo,
            insumo.custo_unitario,
            insumo.quantidade_litros,
            insumo.id_insumo
        )

        cursor.execute(sql, valores)
        conexao.commit()

        sucesso = cursor.rowcount > 0

        cursor.close()
        conexao.close()

        return sucesso

    def delete(self, id_insumo: int) -> bool:
        conexao = connect()
        cursor = conexao.cursor()

        sql = "DELETE FROM Insumo WHERE id_insumo = %s"

        cursor.execute(sql, (id_insumo,))
        conexao.commit()

        sucesso = cursor.rowcount > 0

        cursor.close()
        conexao.close()

        return sucesso