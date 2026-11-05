from models.safra import Safra
from database.connector import connect

class SafraRepository:

    def salvar(self, safra: Safra):
        conexao = connect()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO Safra (nome_safra, cultura, ano_agricola, area_hectare)
        VALUES (%s,%s,%s,%s)
        """
        valores = (safra.nome_safra, safra.cultura, safra.ano_agricola, safra.area_hectare)

        cursor.execute(sql,valores)
        conexao.commit()

        safra.id_safra = cursor.lastrowid

        cursor.close()
        conexao.close()
        return safra

    def listar(self) -> list[Safra]:
        conexao = connect()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Safra")
        linhas = cursor.fetchall()

        cursor.close()
        conexao.close()

        lista_safras = []
        for linha in linhas:
            safra = Safra(
                id_safra=linha["id_safra"],
                nome_safra=linha["nome_safra"],
                cultura=linha["cultura"],
                ano_agricola=str(linha["ano_agricola"]),
                area_hectare=float(linha["area_hectare"])
            )
            lista_safras.append(safra)

        return lista_safras
    
    def buscar_por_id(self, id_safra: int) -> Safra | None:
        conexao = connect()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM Safra WHERE id_safra = %s"
        cursor.execute(sql, (id_safra,))
        linha = cursor.fetchone()

        cursor.close()
        conexao.close()

        if not linha:
            return None
        return Safra(
            id_safra=linha["id_safra"],
            nome_safra=linha["nome_safra"],
            cultura=linha["cultura"],
            ano_agricola=str(linha["ano_agricola"]),
            area_hectare=float(linha["area_hectare"])
        )

    def update(self, safra: Safra) -> bool:
        conexao = connect()
        cursor = conexao.cursor()

        sql = """UPDATE Safra 
            SET nome_safra = %s, cultura = %s, ano_agricola = %s, area_hectare = %s
            WHERE id_safra = %s"""
        valores = (
            safra.nome_safra,
            safra.cultura,
            safra.ano_agricola,
            safra.area_hectare,
            safra.id_safra
        )
        cursor.execute(sql, valores)
        conexao.commit()

        sucesso = cursor.rowcount > 0

        cursor.close()
        conexao.close()

        return sucesso

    def delete(self, id_safra: int) -> bool:
        conexao = connect()
        cursor = conexao.cursor()
        
        sql = "DELETE FROM Safra WHERE id_safra = %s"
        cursor.execute(sql, (id_safra,))
        conexao.commit()

        sucesso = cursor.rowcount > 0

        cursor.close()
        conexao.close()
        return sucesso