import sqlite3

from .categoria import Categoria 
from ecommerce.produto import Produto
from ecommerce.repositorio_produto import RepositorioProduto


class ProdutoNaoEncontradoError(Exception):
    pass


class RepositorioProdutoSQLite(RepositorioProduto):

    def __init__(self, conexao: sqlite3.Connection) -> None:
        self._conexao = conexao

    def adicionar(self, produto: Produto) -> None:
        with self._conexao:
            cursor = self._conexao.execute(
                "INSERT INTO produto (nome, preco, quantidade_estoque, categoria) "
                "VALUES (?, ?, ?, ?)",
                (produto.nome, produto.preco, produto.quantidade_estoque, produto.categoria.nome),
            )
        produto.atribuir_id(cursor.lastrowid)

    def obter(self, id: int) -> Produto:
        linha = self._conexao.execute(
            "SELECT id, nome, preco, quantidade_estoque, categoria FROM produto WHERE id = ?",
            (id,),
        ).fetchone()
        if linha is None:
            raise ProdutoNaoEncontradoError(f"Produto {id} nao encontrado")
        return self._reconstituir(linha)

    
    @staticmethod
    def _reconstituir(linha: tuple) -> Produto:
        id, nome, preco, quantidade_estoque, categoria = linha
        produto = Produto(nome, preco, quantidade_estoque, Categoria(categoria))
        produto.atribuir_id(id)
        return produto