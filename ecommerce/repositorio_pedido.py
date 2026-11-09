from abc import ABC, abstractmethod

from ecommerce.pedido import Pedido


class PedidoNaoEncontradoError(Exception):
    pass


class RepositorioPedido(ABC):

    @abstractmethod
    def adicionar(self, pedido: Pedido) -> None: ...

    @abstractmethod
    def obter(self, id: int) -> Pedido: ...

    @abstractmethod
    def listar(self) -> list[Pedido]: ...

    @abstractmethod
    def atualizar(self, pedido: Pedido) -> None:
        """Registra as mudancas feitas em um pedido que ja foi guardado."""