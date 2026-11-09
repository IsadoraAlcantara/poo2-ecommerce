import sqlite3

from ..dominio.item_pedido import ItemPedido
from .repositorio_pedido import RepositorioPedido
from .repositorio_produto import RepositorioProduto
from ..dominio.pedido import Pedido


class PedidoNaoEncontradoError(Exception):
    pass


class RepositorioPedidoSQLite(RepositorioPedido):
    def __init__(
        self, conexao: sqlite3.Connection, repositorio_produto: RepositorioProduto
    ) -> None:
        self._conexao = conexao
        self._repositorio_produto = repositorio_produto

    def adicionar(self, pedido: Pedido) -> None:
        with self._conexao:
            cursor = self._conexao.execute(
                "INSERT INTO pedido (status) VALUES (?)", (pedido.status,)
            )
            self._gravar_itens(cursor.lastrowid, pedido)
        pedido.atribuir_id(cursor.lastrowid)

    def atualizar(self, pedido: Pedido) -> None:
        with self._conexao:
            cursor = self._conexao.execute(
                "UPDATE pedido SET status = ? WHERE id = ?", (pedido.status, pedido.id)
            )
            if cursor.rowcount == 0:
                raise PedidoNaoEncontradoError("Pedido nunca foi adicionado")
            self._conexao.execute(
                "DELETE FROM item_pedido WHERE pedido_id = ?", (pedido.id,)
            )
            self._gravar_itens(pedido.id, pedido)

    def obter(self, id: int) -> Pedido:
        linha = self._conexao.execute(
            "SELECT id, nome, preco, quantidade_estoque, categoria FROM Pedido WHERE id = ?",
            (id,),
        ).fetchone()
        if linha is None:
            raise PedidoNaoEncontradoError(f"Pedido {id} nao encontrado")
        return self._reconstituir(linha)

    def _reconstituir(self, id: int, status: str) -> Pedido:
        linhas = self._conexao.execute(
            "SELECT produto_id, quantidade, preco_no_momento FROM item_pedido "
            "WHERE pedido_id = ?",
            (id,),
        ).fetchall()
        itens = [
            ItemPedido(self._repositorio_produto.obter(produto_id), quantidade, preco)
            for produto_id, quantidade, preco in linhas
        ]
        return Pedido.reconstituir(id, status, itens)
