
from mysql.connector import Error

from database.connector import connect
from models.aplicacao_insumo import AplicacaoInsumo


class AplicacaoInsumoRepository:

    def salvar(self, aplicacao: AplicacaoInsumo):
        conexao = None
        cursor = None

        try:
            conexao = connect()
            cursor = conexao.cursor()

            sql = """
                INSERT INTO AplicacaoInsumo
                (id_safra, id_insumo, quantidade_aplicada,
                 data_aplicacao, custo_total)
                VALUES (%s, %s, %s, %s, %s)
            """

            valores = (
                aplicacao.id_safra,
                aplicacao.id_insumo,
                aplicacao.quantidade_aplicada,
                aplicacao.data_aplicacao,
                aplicacao.custo_total
            )

            cursor.execute(sql, valores)
            conexao.commit()

            aplicacao.id_aplicacao = cursor.lastrowid

            return aplicacao

        except Error:
            if conexao:
                conexao.rollback()
            raise

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def listar(self) -> list[AplicacaoInsumo]:
        conexao = None
        cursor = None

        try:
            conexao = connect()
            cursor = conexao.cursor(dictionary=True)

            cursor.execute("SELECT * FROM AplicacaoInsumo")
            linhas = cursor.fetchall()

            lista = []

            for linha in linhas:
                aplicacao = AplicacaoInsumo(
                    id_aplicacao=linha["id_aplicacao"],
                    id_safra=linha["id_safra"],
                    id_insumo=linha["id_insumo"],
                    quantidade_aplicada=float(
                        linha["quantidade_aplicada"]
                    ),
                    data_aplicacao=linha["data_aplicacao"],
                    custo_total=float(linha["custo_total"])
                )

                lista.append(aplicacao)

            return lista

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def buscar_por_id(
        self, id_aplicacao: int
    ) -> AplicacaoInsumo | None:

        conexao = None
        cursor = None

        try:
            conexao = connect()
            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT * FROM AplicacaoInsumo
                WHERE id_aplicacao = %s
            """

            cursor.execute(sql, (id_aplicacao,))
            linha = cursor.fetchone()

            if not linha:
                return None

            return AplicacaoInsumo(
                id_aplicacao=linha["id_aplicacao"],
                id_safra=linha["id_safra"],
                id_insumo=linha["id_insumo"],
                quantidade_aplicada=float(
                    linha["quantidade_aplicada"]
                ),
                data_aplicacao=linha["data_aplicacao"],
                custo_total=float(linha["custo_total"])
            )

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def update(self, aplicacao: AplicacaoInsumo) -> bool:
        conexao = None
        cursor = None

        try:
            conexao = connect()
            cursor = conexao.cursor()

            sql = """
                UPDATE AplicacaoInsumo
                SET id_safra = %s,
                    id_insumo = %s,
                    quantidade_aplicada = %s,
                    data_aplicacao = %s,
                    custo_total = %s
                WHERE id_aplicacao = %s
            """

            valores = (
                aplicacao.id_safra,
                aplicacao.id_insumo,
                aplicacao.quantidade_aplicada,
                aplicacao.data_aplicacao,
                aplicacao.custo_total,
                aplicacao.id_aplicacao
            )

            cursor.execute(sql, valores)
            conexao.commit()

            return cursor.rowcount > 0

        except Error:
            if conexao:
                conexao.rollback()
            raise

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def delete(self, id_aplicacao: int) -> bool:
        conexao = None
        cursor = None

        try:
            conexao = connect()
            cursor = conexao.cursor()

            sql = """
                DELETE FROM AplicacaoInsumo
                WHERE id_aplicacao = %s
            """

            cursor.execute(sql, (id_aplicacao,))
            conexao.commit()

            return cursor.rowcount > 0

        except Error:
            if conexao:
                conexao.rollback()
            raise

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
