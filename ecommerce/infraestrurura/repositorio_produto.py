from abc import ABC, abstractmethod

from ecommerce.dominio.produto import Produto


# class ProdutoNaoEncontradoError(Exception):
#     pass


class RepositorioProduto(ABC):

    @abstractmethod
    def adicionar(self, Produto: Produto) -> None: ...

    @abstractmethod
    def obter(self, id: int) -> Produto: ...